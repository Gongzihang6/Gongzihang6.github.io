import open3d as o3d
import numpy as np
import time
import matplotlib.pyplot as plt  # 仅用于生成好看的颜色映射

# ================= 参数设置 =================
ORDER = 3                # 阶数 (建议 2-4，太高会导致点数爆炸)
                         # Order 2 = 64 点
                         # Order 3 = 512 点
                         # Order 4 = 4096 点
                         # Order 5 = 32768 点

DRAW_SPEED = 1          # 绘制速度：每帧增加多少个点
FRAME_DELAY = 0.1       # 帧间隔 (秒)
POINT_SIZE = 5.0         # 点的大小（如果显示点的话）
LINE_WIDTH = 2.0         # 线宽 (Open3D的线宽支持取决于OpenGL驱动，通常固定)
# ===========================================

def morton_decode_3d(t, order):
    """
    3D 莫顿码解码：将线性索引 t 解码为 (x, y, z)
    原理：位交叉 (Bit Interleaving)
    t 的二进制: ... z1 y1 x1 z0 y0 x0
    """
    x = 0
    y = 0
    z = 0
    
    for i in range(order):
        # 提取 x: 第 3*i 位 -> 移到第 i 位
        x |= ((t >> (3 * i)) & 1) << i
        # 提取 y: 第 3*i+1 位 -> 移到第 i 位
        y |= ((t >> (3 * i + 1)) & 1) << i
        # 提取 z: 第 3*i+2 位 -> 移到第 i 位
        z |= ((t >> (3 * i + 2)) & 1) << i
        
    return x, y, z

def generate_3d_z_curve_data(order):
    """预计算所有点和连线"""
    num_points = 8 ** order  # 3D空间是8叉树结构
    print(f"正在生成数据... 阶数: {order}, 总点数: {num_points}")
    
    points = []
    for t in range(num_points):
        points.append(morton_decode_3d(t, order))
    
    points = np.array(points, dtype=np.float64)
    
    # 生成连线索引: [0,1], [1,2], [2,3]...
    lines = [[i, i + 1] for i in range(num_points - 1)]
    lines = np.array(lines, dtype=np.int32)
    
    # 生成渐变颜色 (使用 matplotlib 的 colormap 生成 RGB)
    # 让曲线颜色随索引变化，方便观察路径
    cmap = plt.get_cmap("jet")
    colors = cmap(np.linspace(0, 1, len(lines)))[:, :3] # 取前3通道(RGB)
    
    return points, lines, colors

def main():
    # 1. 生成数据
    full_points, full_lines, full_colors = generate_3d_z_curve_data(ORDER)
    total_points = len(full_points)

    # 2. 初始化 Open3D 可视化窗口
    vis = o3d.visualization.Visualizer()
    vis.create_window(window_name=f"3D Z-Order Curve (Order={ORDER})", width=1024, height=768)
    
    # 设置黑色背景，看起来更酷炫
    opt = vis.get_render_option()
    opt.background_color = np.asarray([0.1, 0.1, 0.1])
    opt.point_size = POINT_SIZE
    opt.line_width = LINE_WIDTH

    # 3. 创建初始几何体 (LineSet)
    line_set = o3d.geometry.LineSet()
    
    # 同时也创建一个 PointCloud 用来显示点（可选，增强视觉效果）
    pcd = o3d.geometry.PointCloud()
    
    # 添加坐标轴辅助线
    axis = o3d.geometry.TriangleMesh.create_coordinate_frame(size=2**ORDER * 0.2, origin=[0, 0, 0])
    vis.add_geometry(axis)
    vis.add_geometry(line_set)
    vis.add_geometry(pcd)

    # 4. 动画循环
    current_idx = 0
    
    # 这是一个简单技巧：为了让相机能看到所有点，先把所有点加进去计算一次包围盒，然后再清空
    line_set.points = o3d.utility.Vector3dVector(full_points)
    vis.update_geometry(line_set)
    vis.reset_view_point(True)
    line_set.points = o3d.utility.Vector3dVector([]) # 清空准备开始动画
    
    print("开始绘制动画...")
    
    while True:
        if current_idx < total_points:
            # 增加索引
            current_idx += DRAW_SPEED
            if current_idx > total_points:
                current_idx = total_points
            
            # 切片数据
            # 注意：LineSet 需要 Points 和 Lines。
            # Points 我们可以把当前所有的点都放进去
            # Lines 只能放当前连通的数量
            
            valid_lines_count = max(0, current_idx - 1)
            
            # 更新几何体数据
            # 1. 更新点
            slice_points = full_points[:current_idx]
            line_set.points = o3d.utility.Vector3dVector(slice_points)
            pcd.points = o3d.utility.Vector3dVector(slice_points)
            
            # 2. 更新线 (连接关系)
            if valid_lines_count > 0:
                line_set.lines = o3d.utility.Vector2iVector(full_lines[:valid_lines_count])
                line_set.colors = o3d.utility.Vector3dVector(full_colors[:valid_lines_count])
                
                # 给点也上色 (使用最后一条线的颜色作为点的颜色，近似)
                # 这里的逻辑稍微简化，直接用全量的颜色映射
                # 实际上点比线多1个，这里为了演示简单不做严格对齐
                pcd_colors = np.zeros((current_idx, 3))
                # 简单填充颜色，实际效果也很好
                if current_idx > 1:
                    pcd_colors[:-1] = full_colors[:valid_lines_count]
                    pcd_colors[-1] = full_colors[valid_lines_count-1]
                pcd.colors = o3d.utility.Vector3dVector(pcd_colors)

            # 通知 Open3D 数据已变更
            vis.update_geometry(line_set)
            vis.update_geometry(pcd)
            
            # 只有在前几帧调整视角，避免视角乱跳，之后让用户自己控制
            if current_idx < DRAW_SPEED * 2:
                vis.poll_events()
                vis.update_renderer()
            
        # 保持窗口响应 (即使画完了也要响应旋转缩放)
        vis.poll_events()
        vis.update_renderer()
        
        # 控制帧率 (仅在绘制过程中)
        if current_idx < total_points:
            time.sleep(FRAME_DELAY)

    # 注意：在 Open3D 非阻塞模式下，通常需要手动关闭窗口来结束进程
    vis.destroy_window()

if __name__ == "__main__":
    main()