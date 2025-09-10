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