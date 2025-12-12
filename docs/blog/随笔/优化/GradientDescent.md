# 机器学习之最优化算法

## BGD（Batch Gradient Descent）

批量梯度下降法是一种常用的优化算法，用于求解函数的最小值或最大值。它通过迭代地更新参数的方式来逐步接近最优解。

假设我们要最小化一个可微函数 $f(x)$，其中 $x$ 是参数向量。梯度下降法的目标是找到使得 $f(x)$ 达到最小值的 $x$。这个过程可以通过以下公式进行描述：

$$
x_{n+1} = x_n - \alpha \cdot \nabla f(x_n)
$$

其中，$x_n$ 表示第 $n$ 次迭代的参数值，$\nabla f(x_n)$ 表示函数 $f$ 在 $x_n$ 处的梯度（即导数），$\alpha$ 称为学习率或步长，用于控制每次迭代的步幅。

具体而言，梯度下降法从 **任意初始点** 开始，根据当前位置的梯度方向（**即函数增长最快的方向**）以及学习率确定下一个位置，并不断迭代直到满足停止条件。<span style="color:#d59bf6;">当函数存在多个局部最小值时，梯度下降法可能会收敛到其中一个局部最优解。</span>

批量梯度下降的思想是要**绝对的精确**，每一次都看完所有训练数据（整个训练集N）计算出一个完全准确的“平均梯度”，然后以这个最正确的方向，更新一步；
$$
g_t = \nabla L(w_{t-1}) = \frac{1}{N} \sum_{i=1}^{N} \nabla L_i(w_{t-1}, x_i, y_i)
$$
统筹兼顾每一个样本的梯度，平均来选择最好的

优点：梯度方向最准，收敛路径最稳定，无“噪声”；

缺点：比较慢！训练集有 100 万张图，你就得算完 100 万张图的梯度才更新一次参数。而且内存爆炸，无法用于现代深度学习。

```python
import numpy as np
import matplotlib.pyplot as plt

def gradient_descent(f, df, x0, learning_rate, num_iterations):
    x = x0
    x_history = [x]
    
    for _ in range(num_iterations):
        gradient = df(x)
        x -= learning_rate * gradient
        x_history.append(x)
    
    return np.array(x_history)

# 定义函数f(x)
def f(x):
    return x**2 + 10*np.sin(x)

# 定义函数f(x)的导数df(x)
def df(x):
    return 2*x + 10*np.cos(x)

# 设置初始参数值和学习率
x0 = -5
learning_rate = 0.1
num_iterations = 100

# 运行梯度下降算法
x_history = gradient_descent(f, df, x0, learning_rate, num_iterations)

# 绘制函数曲线和梯度下降路径
x_range = np.linspace(-10, 10, 100)
plt.plot(x_range, f(x_range), label='f(x)')
plt.scatter(x_history, f(np.array(x_history)), c='red', label='Gradient Descent')
plt.legend()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Gradient Descent')
plt.show()
```

![gradient_descent_optimization with LR=0.1](https://cdn.jsdelivr.net/gh/Gongzihang6/Pictures@main/Medias/2025%5C10%5Cgradient_descent_optimization.gif)

![lr_0.01_optimization](https://cdn.jsdelivr.net/gh/Gongzihang6/Pictures@main/Medias/2025%5C10%5Clr_0.01_optimization.gif)

![lr_0.3_optimization](https://cdn.jsdelivr.net/gh/Gongzihang6/Pictures@main/Medias/2025%5C10%5Clr_0.3_optimization.gif)

如上三幅图所示，学习率设为0.1时，正常收敛且速度较快；学习率设为0.01时，也能收敛，但明显收敛速度放缓；学习率设为0.3时，明显过大，在最小值附近来回震荡，无法收敛到极小值；所以学习率既不能过大，也不能过小；

## SGD（Stochastic Gradient Descent）

随机梯度下降法常用于训练机器学习模型。它的主要思想是通过迭代更新模型参数来最小化损失函数。

传统的梯度下降法是使用所有的样本，计算所有样本点的梯度，根据梯度的平均值，决定参数更新的方向（整个数据集上“最正确”的下降方向），相比于传统的梯度下降法，SGD 在每一次迭代中**仅使用一个样本数据**进行参数更新，因此计算速度更快。但缺点是梯度方向不一定最正确，方向可能不稳定，虽然大方向可能依然正确，但是会像醉汉一样，左移右晃的前行；

SGD 的公式如下：

$$
g_t = \nabla L_i(w_{t-1}, x_i, y_i) （i 是随机选的）
$$

其中，$\theta$ 表示模型参数，$\eta$ 表示学习率，$\nabla L_i$ 表示损失函数关于参数 $\omega$ 的梯度（t-1表示迭代轮数），$(x^{(i)}, y^{(i)})$ 表示第 $i$ 个训练样本。

SGD 的工作过程如下：

1. 初始化模型参数 $\theta$；
2. 随机选择一个样本 $(x^{(i)}, y^{(i)})$；
3. 计算损失函数关于参数 $\omega$ 的梯度：$\nabla L_i$；
4. 更新参数 $\omega_t$：$\omega_t= \omega_{t-1}- \eta \cdot \nabla L_i$；
5. 重复步骤 2-4，直到达到停止条件（例如达到指定的迭代次数或损失函数下降到一定程度）。

下面是一个关于 SGD 的工作原理的一个例子。

```python
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
ani.save('code\optimize\sgd_animation.gif', writer='pillow', fps=10)

plt.show()
```

![sgd_animation](https://cdn.jsdelivr.net/gh/Gongzihang6/Pictures@main/Medias/2025%5C10%5Csgd_animation.gif)

## MBGD（Mini-Batch SGD）

小批量梯度下降法是介于随机梯度下降法（SGD）和批量梯度下降法（BGD）之间的一种折中方法。

它将训练样本划分为多个批次（mini-batches），每个批次包含若干个样本。与 SGD 每次只使用一个样本进行参数更新相比，MBGD 每次使用一个批次的样本进行参数更新。

MBGD 的主要区别和优势如下：

1.  **计算效率：** 与 BGD 相比，MBGD 采用小批量样本进行参数更新，可以减少计算时间。尤其在大规模数据集上，MBGD 通常比 BGD 更快。而与 SGD 相比，MBGD 每次更新的样本数量更多，可以充分利用矩阵运算的并行性，加速参数更新过程。
2.  **稳定性：** MBGD 相对于 SGD 具有更好的稳定性。由于 MBGD 每次使用多个样本进行参数更新，因此其参数更新方向相对于单个样本更加准确，避免了 SGD 中参数更新的高度不稳定问题。这使得 MBGD 在训练过程中更容易收敛到更好的局部最优解。
3.  **鲁棒性：** MBGD 相对于 SGD 对噪声数据具有更好的鲁棒性。由于 MBGD 每次使用多个样本进行参数更新，它对于单个样本中的噪声信息会有所平均化，从而减少了单个样本对模型的影响。
4.  **泛化能力：** MBGD 相对于 SGD 和 BGD 在一定程度上具有更好的泛化能力。与 SGD 相比，MBGD 使用了更多的样本进行参数更新，可以更充分地表征数据集的特征；与 BGD 相比，MBGD 采用了部分样本进行参数更新，避免了过度拟合的问题。

需要注意的是，MBGD 的选择要根据具体问题的需求来确定。较小的批次大小可能会导致更快的收敛速度，但也可能陷入局部最优解。较大的批次大小可能导致计算变慢，但可能会获得更稳定的解。

因此，在实践中，我们通常需要根据数据集的规模、模型的复杂度和计算资源的限制等因素来选择适当的批次大小。

综上所述，MBGD 是在 SGD 和 BGD 之间取得折中的一种优化算法，它在计算效率、稳定性、鲁棒性和泛化能力等方面都具有一定的优势。





























































































































































































