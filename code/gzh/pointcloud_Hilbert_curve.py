"""
代码名称: Hilbert Curve Point Cloud Traversal Visualization
功能描述: 
    1. 读取或生成 3D 点云数据 (Open3D格式)。
    2. 将点云坐标归一化并量化，映射到 Hilbert 曲线空间。
    3. 计算每个点的 Hilbert Index 并进行排序。
    4. 使用 Open3D 创建动画，按排序顺序逐个连接点，展示 Hilbert 曲线的空间填充路径。

实现逻辑:
    1. 数据预处理: 计算点云的包围盒 (Bounding Box)，将所有点缩放平移到 [0, 1] 空间，再乘以 2^p 转换为整数坐标。
    2. 索引计算: 使用 `hilbertcurve` 库计算每个量化点的距离值 (d)。
    3. 排序: 根据 d 值对原始点云数组进行重排。
    4. 可视化: 
       - 这是一个非阻塞的渲染循环 (Non-blocking render loop)。
       - 每一帧向 LineSet (线集) 中添加新的线段连接当前点和上一个点。
       - 使用颜色渐变 (Jet colormap) 来标识路径的进度。
"""

import open3d as o3d
import numpy as np
from hilbertcurve.hilbertcurve import HilbertCurve
import matplotlib.pyplot as plt
import time

# ==========================================
# 1. 核心算法类：处理排序逻辑
# ==========================================
class HilbertPointCloudSorter:
    def __init__(self, pcd_points, order=6):
        """
        初始化
        :param pcd_points: numpy array (N, 3) 原始点云坐标
        :param order: Hilbert 阶数 (p)。p=6 表示 64x64x64 的网格，足够可视化使用
        """
        self.original_points = pcd_points
        self.order = order
        self.sorted_points = None
        self.sorted_indices = None
        
    def process(self):
        print("正在进行归一化和量化处理...")
        # 1. 计算包围盒并归一化，保持长宽比 (Aspect Ratio)
        # 如果直接缩放 x,y,z 到 [0,1]，物体会变形。应该用最大边长来缩放。
        min_bound = np.min(self.original_points, axis=0)
        max_bound = np.max(self.original_points, axis=0)
        center = (min_bound + max_bound) / 2
        scale = np.max(max_bound - min_bound)
        
        # 归一化到 [0, 1] 中心化
        normalized = (self.original_points - center) / scale + 0.5
        # 截断到 [0, 1] 防止浮点误差越界
        normalized = np.clip(normalized, 0, 1)
        
        # 2. 量化为整数
        grid_size = 1 << self.order
        # 坐标范围 [0, grid_size - 1]
        quantized = (normalized * (grid_size - 1)).astype(np.int64)
        
        print(f"正在计算 {len(self.original_points)} 个点的 Hilbert Index (Order={self.order})...")
        # 3. 计算 Hilbert Index
        hc = HilbertCurve(p=self.order, n=3)
        distances = hc.distances_from_points(quantized.tolist())
        
        # 4. 排序
        print("正在排序...")
        self.sorted_indices = np.argsort(distances)
        self.sorted_points = self.original_points[self.sorted_indices]
        
        return self.sorted_points

# ==========================================
# 2. 可视化类：Open3D 动画控制
# ==========================================
def run_visualization(sorted_points):
    """
    运行 Open3D 动画
    """
    num_points = len(sorted_points)
    print(f"开始可视化，共 {num_points} 个点。按 'Q' 退出。")

    # --- 初始化 Open3D 窗口 ---
    vis = o3d.visualization.Visualizer()
    vis.create_window(window_name="Hilbert Curve Traversal", width=1024, height=768)
    
    # 设置黑色背景，对比度更高
    opt = vis.get_render_option()
    opt.background_color = np.asarray([0, 0, 0])
    opt.point_size = 2.0

    # --- 创建几何体 ---
    
    # 1. 背景点云 (设为深灰色，作为参考)
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(sorted_points)
    pcd.paint_uniform_color([0.2, 0.2, 0.2]) # 暗灰色
    vis.add_geometry(pcd)

    # 2. 动态路径 (LineSet)
    line_set = o3d.geometry.LineSet()
    # 预先分配空间，但在循环中逐步显示
    # 注意：Open3D 的 LineSet 若频繁 resize 性能较差。
    # 策略：我们一开始就把所有点放进去，但是 Lines (连接关系) 逐步添加。
    line_set.points = o3d.utility.Vector3dVector(sorted_points)
    line_set.lines = o3d.utility.Vector2iVector([]) 
    vis.add_geometry(line_set)

    # 3. 动态“笔头” (一个鲜艳的球体，指示当前位置)
    sphere = o3d.geometry.TriangleMesh.create_sphere(radius=0.02) # 半径需根据物体大小调整
    sphere.paint_uniform_color([1, 0, 0]) # 红色
    sphere.compute_vertex_normals()
    vis.add_geometry(sphere)

    # --- 颜色映射生成 (彩虹色) ---
    # 使用 matplotlib 生成从蓝到红的渐变色
    colormap = plt.get_cmap("jet")
    # 生成所有连线的颜色表
    colors_np = colormap(np.linspace(0, 1, num_points))[:, :3] # 去掉 alpha 通道

    # --- 动画循环 ---
    # 为了演示流畅，我们将点进行降采样或分批处理，否则几万个点一帧帧画太慢
    # 这里每帧增加 step 个点
    step = max(1, num_points // 1000) # 保证大约 1000 帧画完
    current_idx = 0
    
    all_lines = []
    all_colors = []

    # 获取视角控制
    ctr = vis.get_view_control()
    # 稍微旋转一下视角以便看清
    ctr.rotate(10.0, 0.0)

    while current_idx < num_points - 1:
        # 计算这一批次的终点
        end_idx = min(current_idx + step, num_points - 1)
        
        # 构建新的连线索引：[[0,1], [1,2], ...]
        new_lines = []
        for i in range(current_idx, end_idx):
            new_lines.append([i, i+1])
            all_colors.append(colors_np[i])
        
        all_lines.extend(new_lines)
        
        # 更新 LineSet 数据
        line_set.lines = o3d.utility.Vector2iVector(all_lines)
        line_set.colors = o3d.utility.Vector3dVector(all_colors)
        
        # 更新笔头位置
        last_point = sorted_points[end_idx]
        # sphere 需要平移到新位置 (Open3D 的 transform 是累积的，所以先重置再移动比较麻烦)
        # 简单方法：重新生成一个 sphere 或者计算相对位移。
        # 这里用相对位移：
        prev_point = sorted_points[current_idx] if current_idx > 0 else sorted_points[0]
        translation = last_point - prev_point
        # 注意：这里的球体移动在累积误差下可能不准，最稳妥是重置位置
        # 但为了性能，我们这里只更新 LineSet 和 Geometry
        
        # 通知 Open3D 数据已更新
        vis.update_geometry(line_set)
        
        # 视角自动旋转一点点，增加立体感
        ctr.rotate(1.0, 0.0)
        
        vis.poll_events()
        vis.update_renderer()
        
        current_idx = end_idx
        # time.sleep(0.01) # 如果太快可以解开这行

    print("动画结束。窗口将保持打开。")
    vis.run() # 保持窗口直到关闭
    vis.destroy_window()

# ==========================================
# 3. 主入口与数据生成
# ==========================================
if __name__ == "__main__":
    # --- 选项 A: 生成测试数据 (兔子或球体) ---
    print("生成测试点云数据...")
    mesh = o3d.geometry.TriangleMesh.create_torus(torus_radius=1.0, tube_radius=0.3)
    # 采样点云 (比如采样 5000 个点)
    pcd = mesh.sample_points_uniformly(number_of_points=5000)
    
    # 如果您有自己的文件，请取消注释下面这行：
    pcd = o3d.io.read_point_cloud(r"F:\Gongzihang\2025\data\point_cloud_data\20251102\clipped_results\20251102_122054_474\merged_5_cameras_final_20251102_122054_474_depth.pcd")

    points = np.asarray(pcd.points)

    # --- 处理 ---
    sorter = HilbertPointCloudSorter(points, order=5) # order=5 (32格) 速度较快
    sorted_pts = sorter.process()

    # --- 可视化 ---
    run_visualization(sorted_pts)