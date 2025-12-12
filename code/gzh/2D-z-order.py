import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# ================= 配置区域 =================
ORDER = 2             # 阶数：控制稠密程度 (建议 1-6)
POINTS_PER_FRAME = 1   # 绘制速度控制1：每一帧增加多少个点 (数值越大越快)
INTERVAL = 160          # 绘制速度控制2：帧与帧之间的间隔 (毫秒，数值越小越快)
# ===========================================

def morton_decode(t, order):
    """
    将线性索引 t 解码为 (x, y) 坐标 (莫顿码位交叉)
    """
    x = 0
    y = 0
    for i in range(order):
        x |= ((t >> (2 * i)) & 1) << i
        y |= ((t >> (2 * i + 1)) & 1) << i
    return x, y

def generate_data(order):
    """预先计算所有坐标点"""
    num_points = 4 ** order
    x_coords = []
    y_coords = []
    for t in range(num_points):
        x, y = morton_decode(t, order)
        x_coords.append(x)
        y_coords.append(y)
    return x_coords, y_coords, num_points

def animate_z_order():
    # 1. 准备数据
    print(f"正在生成 {ORDER} 阶数据，共 {4**ORDER} 个点...")
    x_data, y_data, total_points = generate_data(ORDER)

    # 2. 设置画布
    fig, ax = plt.subplots(figsize=(8, 8))
    
    # 设置坐标轴范围 (稍微留一点边距)
    limit = 2 ** ORDER
    ax.set_xlim(-1, limit)
    ax.set_ylim(-1, limit)
    ax.set_aspect('equal') # 保持正方形比例
    ax.grid(True, linestyle='--', alpha=0.3)
    
    # 初始化线条对象 (先画一个空的)
    line, = ax.plot([], [], color='blue', lw=1.5, marker='.', markersize=3)
    
    # 标题对象，用于动态显示进度
    title = ax.set_title(f"Z-Order Curve (Order={ORDER})")

    # 3. 动画更新函数
    def update(frame):
        # 计算当前应该画到第几个点
        # frame 从 0 开始，每次 update 代表过了一帧
        current_index = frame * POINTS_PER_FRAME
        
        # 防止溢出
        if current_index > total_points:
            current_index = total_points

        # 更新线条数据
        line.set_data(x_data[:current_index], y_data[:current_index])
        
        # 更新标题显示进度
        progress = (current_index / total_points) * 100
        title.set_text(f"Z-Order Curve (Order={ORDER}) - Progress: {progress:.1f}%")
        
        return line, title

    # 4. 创建动画
    # frames 计算：总点数 / 每帧点数
    total_frames = (total_points // POINTS_PER_FRAME) + 2
    
    ani = animation.FuncAnimation(
        fig, 
        update, 
        frames=total_frames, 
        interval=INTERVAL, 
        blit=False,       # blit=True 性能更好，但有时会导致标题不更新，这里设为 False 保证兼容性
        repeat=False      # 播放完不重复
    )

    print("开始绘制窗口...")
    plt.show()

if __name__ == "__main__":
    animate_z_order()