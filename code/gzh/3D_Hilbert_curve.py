import open3d as o3d
import numpy as np
import matplotlib.pyplot as plt
import time
import sys

# ==========================================
# 1. 基础类与算法 (保持不变)
# ==========================================
class Turtle3D:
    def __init__(self):
        self.x, self.y, self.z = 0.0, 0.0, 0.0
        self.path = [(0.0, 0.0, 0.0)]

    def move(self, dx, dy, dz):
        self.x += dx
        self.y += dy
        self.z += dz
        self.path.append((self.x, self.y, self.z))

    def get_path(self):
        return np.array(self.path)

def hilbert_3d(turtle, order, u1, u2, u3):
    if order == 0: return
    hilbert_3d(turtle, order-1, u3, u1, u2)
    turtle.move(*u1)
    hilbert_3d(turtle, order-1, u2, u3, u1)
    turtle.move(*u2)
    hilbert_3d(turtle, order-1, u2, u3, u1)
    turtle.move(*tuple(-x for x in u1))
    hilbert_3d(turtle, order-1, tuple(-x for x in u1), tuple(-x for x in u2), u3)
    turtle.move(*u3)
    hilbert_3d(turtle, order-1, tuple(-x for x in u1), tuple(-x for x in u2), u3)
    turtle.move(*u1)
    hilbert_3d(turtle, order-1, tuple(-x for x in u2), u3, tuple(-x for x in u1))
    turtle.move(*tuple(-x for x in u2))
    hilbert_3d(turtle, order-1, tuple(-x for x in u2), u3, tuple(-x for x in u1))
    turtle.move(*tuple(-x for x in u1))
    hilbert_3d(turtle, order-1, u3, tuple(-x for x in u1), tuple(-x for x in u2))

# ==========================================
# 2. 箭头生成 (保持小尺寸逻辑)
# ==========================================
def generate_arrow_segments(points, arrow_len):
    arrow_points = []
    arrow_indices = []
    wing_span = arrow_len * 0.4 
    
    for i in range(len(points) - 1):
        start = points[i]
        end = points[i+1]
        direction = end - start
        seg_length = np.linalg.norm(direction)
        if seg_length == 0: continue
        direction = direction / seg_length
        
        # 箭头尖端位于线段 50% 处
        tip = start + direction * (seg_length * 0.5)
        
        aux_vec = np.array([0, 0, 1])
        if np.abs(np.dot(direction, aux_vec)) > 0.9: 
            aux_vec = np.array([0, 1, 0])
            
        right = np.cross(direction, aux_vec)
        right = right / np.linalg.norm(right)
        up = np.cross(direction, right)
        
        back = -direction * arrow_len
        
        p1 = tip + back + right * wing_span
        p2 = tip + back - right * wing_span
        p3 = tip + back + up * wing_span
        p4 = tip + back - up * wing_span
        
        base_idx = len(arrow_points)
        arrow_points.extend([tip, p1, p2, p3, p4])
        arrow_indices.append([base_idx, base_idx+1])
        arrow_indices.append([base_idx, base_idx+2])
        arrow_indices.append([base_idx, base_idx+3])
        arrow_indices.append([base_idx, base_idx+4])
        
    return np.array(arrow_points), np.array(arrow_indices)

def align_vector_to_vector(v_from, v_to):
    v_from = v_from / np.linalg.norm(v_from)
    v_to = v_to / np.linalg.norm(v_to)
    axis = np.cross(v_from, v_to)
    cos_angle = np.dot(v_from, v_to)
    if cos_angle > 0.999: return np.eye(3)
    if cos_angle < -0.999: return -np.eye(3)
    axis = axis / np.linalg.norm(axis)
    angle = np.arccos(cos_angle)
    return o3d.geometry.get_rotation_matrix_from_axis_angle(axis * angle)

# ==========================================
# 3. 主程序
# ==========================================
def main():
    # --- 参数配置 ---
    ORDER = 4
    SIZE = 10.0
    ANIMATION_SPEED = 1  
    FRAME_DELAY = 0.01
    # ----------------

    step = SIZE / (2**ORDER - 1)
    
    print(f"正在生成 {ORDER} 阶 Hilbert 曲线...")
    t = Turtle3D()
    hilbert_3d(t, ORDER, (step, 0, 0), (0, step, 0), (0, 0, step))
    points = t.get_path()
    total_points = len(points)

    # 【修改点 1】：使用 HSV (彩虹色) 配色，比 Viridis 亮得多
    # hsv: 红->黄->绿->青->蓝->洋红->红。全程高饱和度。
    cmap = plt.get_cmap("hsv") 
    all_colors = np.array([cmap(i/(total_points-1))[:3] for i in range(total_points)])

    # 箭头保持小尺寸 (25%)
    arrow_size_dynamic = step * 0.25
    arrow_pts_all, arrow_idx_all = generate_arrow_segments(points, arrow_len=arrow_size_dynamic)
    
    # 【修改点 2】：箭头改用亮白色，或者稍微暗一点的黄色，让彩色曲线当主角
    # 亮白色: [1, 1, 1]，如果觉得还是抢戏，可以改为灰色 [0.5, 0.5, 0.5]
    # 这里用亮白色，对比度高，但不会像黄色那样容易和曲线混淆
    arrow_color_fixed = np.array([0.8, 0.8, 0.8]) 

    # --- Open3D 初始化 ---
    vis = o3d.visualization.Visualizer()
    vis.create_window(f"Hilbert Curve Order {ORDER}", width=1024, height=768)
    opt = vis.get_render_option()
    opt.background_color = np.array([0, 0, 0])
    
    # 【修改点 3】：大幅增加线宽
    # 注意：部分 Windows/Nvidia 驱动可能会忽略此参数强制显示为 1px。
    # 如果是这种情况，通常无法通过 line_width 解决，只能换 colormap 增加对比度。
    opt.line_width = 5.0 
    # 开启点的大小，如果你想看到顶点
    opt.point_size = 5.0 

    # A. 主路径
    main_line = o3d.geometry.LineSet()
    main_line.points = o3d.utility.Vector3dVector(points[:2])
    main_line.lines = o3d.utility.Vector2iVector([[0, 1]])
    main_line.colors = o3d.utility.Vector3dVector(all_colors[:1])
    vis.add_geometry(main_line)

    # B. 箭头
    arrow_line = o3d.geometry.LineSet()
    arrow_line.points = o3d.utility.Vector3dVector(arrow_pts_all[:5])
    arrow_line.lines = o3d.utility.Vector2iVector(arrow_idx_all[:4])
    vis.add_geometry(arrow_line)

    # C. 海龟头部 (圆锥体)
    cone_len = step * 0.6 
    mesh_base = o3d.geometry.TriangleMesh.create_cone(radius=cone_len*0.3, height=cone_len)
    # 头部用纯红色，非常醒目
    mesh_base.paint_uniform_color([1.0, 0.0, 0.0]) 
    mesh_base.compute_vertex_normals()
    
    turtle_head = o3d.geometry.TriangleMesh(mesh_base)
    turtle_head.translate([0, 0, -cone_len/2])
    turtle_head.rotate(o3d.geometry.get_rotation_matrix_from_axis_angle([np.pi, 0, 0]), center=[0,0,0])
    turtle_head.translate(points[0])
    vis.add_geometry(turtle_head)

    # D. 包围盒
    bbox = o3d.geometry.AxisAlignedBoundingBox(min_bound=points.min(axis=0), max_bound=points.max(axis=0))
    bbox.color = (0.3, 0.3, 0.3)
    vis.add_geometry(bbox)

    # --- 相机 ---
    ctr = vis.get_view_control()
    ctr.set_lookat((points.min(axis=0) + points.max(axis=0)) / 2)
    ctr.set_front([-1.0, -1.0, -1.0])
    ctr.set_up([0, 0, 1])
    ctr.set_zoom(0.8)
    
    base_vector = np.array([0, 0, 1]) 

    # --- 动画循环 ---
    curr_idx = 0
    while vis.poll_events():
        if curr_idx < total_points - 1:
            next_idx = min(curr_idx + ANIMATION_SPEED, total_points - 1)
            
            if next_idx > curr_idx:
                # 1. 更新主线
                indices = np.stack((np.arange(0, next_idx), np.arange(1, next_idx+1)), axis=-1)
                main_line.points = o3d.utility.Vector3dVector(points[:next_idx+1])
                main_line.lines = o3d.utility.Vector2iVector(indices)
                main_line.colors = o3d.utility.Vector3dVector(all_colors[:indices.shape[0]])
                vis.update_geometry(main_line)

                # 2. 更新箭头
                if next_idx > 0:
                    num_arrow_pts = next_idx * 5
                    num_arrow_lines = next_idx * 4
                    
                    arrow_line.points = o3d.utility.Vector3dVector(arrow_pts_all[:num_arrow_pts])
                    arrow_line.lines = o3d.utility.Vector2iVector(arrow_idx_all[:num_arrow_lines])
                    colors_arr = np.tile(arrow_color_fixed, (num_arrow_lines, 1))
                    arrow_line.colors = o3d.utility.Vector3dVector(colors_arr)
                    vis.update_geometry(arrow_line)

                # 3. 更新头部
                current_pos = points[next_idx]
                prev_pos = points[next_idx-1]
                move_vec = current_pos - prev_pos
                
                if np.linalg.norm(move_vec) > 1e-6:
                    R = align_vector_to_vector(base_vector, move_vec)
                    turtle_head.vertices = o3d.utility.Vector3dVector(mesh_base.vertices)
                    turtle_head.triangles = mesh_base.triangles
                    turtle_head.translate([0, 0, -cone_len/2])
                    turtle_head.rotate(o3d.geometry.get_rotation_matrix_from_axis_angle([np.pi, 0, 0]), center=[0,0,0])
                    turtle_head.rotate(R, center=[0,0,0])
                    turtle_head.translate(current_pos)
                    vis.update_geometry(turtle_head)

                curr_idx = next_idx
                time.sleep(FRAME_DELAY)

        vis.update_renderer()

    vis.destroy_window()

if __name__ == "__main__":
    main()