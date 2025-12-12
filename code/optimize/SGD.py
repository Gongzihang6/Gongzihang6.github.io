import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# --- 函数定义和数据生成 (与方法一相同) ---
def loss_function(x, y):
    return (x - 1) ** 2 + (y - 2) ** 2

def gradient(x, y):
    return np.array([2 * (x - 1), 2 * (y - 2)])

x_range = np.linspace(-3, 5, 100)
y_range = np.linspace(-2, 6, 100)
X, Y = np.meshgrid(x_range, y_range)
Z = loss_function(X, Y)

# --- 预先计算所有迭代步骤 ---
eta = 0.1
num_iterations = 30
theta = np.array([0.0, 0.0])
path = [] # 用于存储每一步的 (x, y, loss)

for i in range(num_iterations):
    current_loss = loss_function(theta[0], theta[1])
    path.append((theta[0], theta[1], current_loss))
    gradient_value = gradient(theta[0], theta[1])
    theta = theta - eta * gradient_value
path.append((theta[0], theta[1], loss_function(theta[0], theta[1]))) # 添加最后一点

# --- 设置动画 ---
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.6)
ax.set_xlabel("Theta_0")
ax.set_ylabel("Theta_1")
ax.set_zlabel("Loss")

# 初始化一个空的line对象，我们将在动画中更新它的数据
line, = ax.plot([], [], [], color='red', marker='o', markersize=4, label='SGD Path')
ax.legend()

# 动画的更新函数
def update(frame):
    # 从预计算的路径中获取当前帧的数据
    x_data = [p[0] for p in path[:frame+1]]
    y_data = [p[1] for p in path[:frame+1]]
    z_data = [p[2] for p in path[:frame+1]]
    
    # 更新line对象的数据
    line.set_data(x_data, y_data)
    line.set_3d_properties(z_data)
    
    # 更新标题
    current_loss = path[frame][2]
    ax.set_title(f"SGD Iteration: {frame}/{num_iterations} | Loss: {current_loss:.4f}")
    
    return line,

# 创建并启动动画
# interval=100 表示每帧之间间隔100毫秒
# blit=False 在3D图中通常是必需的
ani = FuncAnimation(fig, update, frames=len(path), interval=1000, blit=False)

# 保存为GIF（可选，需要安装ImageMagick或Pillow）
ani.save('gif\sgd_animation.gif', writer='pillow', fps=10)

plt.show()