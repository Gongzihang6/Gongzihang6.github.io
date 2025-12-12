# 用户指南

## 目录
1. [快速入门](#快速入门)
2. [基础概念](#基础概念)
3. [配置管理](#配置管理)
4. [算法详解](#算法详解)
5. [测试函数库](#测试函数库)
6. [可视化功能](#可视化功能)
7. [高级用法](#高级用法)
8. [最佳实践](#最佳实践)

## 快速入门

### 第一个例子

```python
from algorithms.gradient_descent import GradientDescentVisualizer
from utils.test_functions import TestFunctions

# 1. 创建测试函数
f, df = TestFunctions.quadratic(a=1.0, b=-4.0, c=5.0)

# 2. 创建可视化器
visualizer = GradientDescentVisualizer(f, df, x_range=[-1, 6])

# 3. 运行优化
anim, history = visualizer.create_animation(
    x0=5.0,
    function_name="my_first_optimization",
    learning_rate=0.1,
    save_gif=True
)

print(f"最终结果: x = {history['x'][-1]:.6f}")
```

### 命令行使用

```bash
# 基本用法
python main.py gradient_descent quadratic --x0 5.0 --learning_rate 0.1

# 查看帮助
python main.py --help

# 列出可用算法和函数
python main.py --list-algorithms
python main.py --list-functions
```

## 基础概念

### 优化算法

优化算法是寻找函数最小值（或最大值）的数学方法。本项目专注于一维函数的优化可视化。

### 梯度下降

梯度下降是最基础的优化算法：
- **原理**: 沿着函数梯度的反方向移动
- **公式**: `x_{k+1} = x_k - α * ∇f(x_k)`
- **参数**: 
  - `α`: 学习率，控制步长大小
  - `∇f(x)`: 函数在点x处的梯度

### 收敛性

- **收敛**: 算法找到最优解
- **发散**: 算法无法找到解，可能震荡或发散
- **局部最优**: 算法收敛到局部最小值而非全局最小值

## 配置管理

### 配置文件结构

```yaml
# config/config.yaml
project:
  name: "优化算法可视化"
  version: "1.0.0"

paths:
  output: "./output"
  algorithms: "./algorithms"
  temp: "./temp"
  logs: "./logs"

visualization:
  figure:
    figsize: [15, 6]
    dpi: 100
  animation:
    interval: 100
    repeat: true
  fonts:
    chinese: "SimHei"
    english: "Arial"

algorithms:
  gradient_descent:
    learning_rate: 0.1
    max_iterations: 100
    tolerance: 1e-6
```

### 使用配置

```python
from config import get_config, update_config

# 获取配置
config = get_config()
learning_rate = config['algorithms']['gradient_descent']['learning_rate']

# 更新配置
update_config('algorithms.gradient_descent.learning_rate', 0.05)
```

## 算法详解

### 梯度下降算法

#### 标准梯度下降

```python
# 基本用法
history = visualizer.optimize_with_history(
    x0=5.0,
    learning_rate=0.1,
    max_iterations=100,
    tolerance=1e-6
)
```

**参数说明**:
- `x0`: 初始点
- `learning_rate`: 学习率，建议范围 [0.001, 0.5]
- `max_iterations`: 最大迭代次数
- `tolerance`: 收敛容忍度

#### 自适应学习率梯度下降

```python
# 自适应学习率
history = visualizer.optimize_with_adaptive_learning_rate(
    x0=5.0,
    initial_learning_rate=0.5,
    decay_factor=0.9,
    max_iterations=100
)
```

**特点**:
- 学习率随迭代次数递减
- 有助于避免震荡
- 适合复杂函数优化

#### 动量梯度下降

```python
# 动量方法
history = visualizer.optimize_with_momentum(
    x0=5.0,
    learning_rate=0.01,
    momentum=0.9,
    max_iterations=200
)
```

**特点**:
- 利用历史梯度信息
- 加速收敛
- 有助于跳出局部最优

## 测试函数库

### 简单函数

#### 二次函数
```python
f, df = TestFunctions.quadratic(a=1.0, b=-4.0, c=5.0)
# f(x) = ax² + bx + c
```

#### 三次函数
```python
f, df = TestFunctions.cubic(a=1.0, b=-6.0, c=9.0, d=-4.0)
# f(x) = ax³ + bx² + cx + d
```

### 经典优化测试函数

#### Rosenbrock函数
```python
f, df = TestFunctions.rosenbrock_1d(a=1.0, b=100.0)
# 著名的"香蕉函数"，测试算法性能
```

#### Beale函数
```python
f, df = TestFunctions.beale_1d()
# 多峰函数，有多个局部最优解
```

### 复杂函数

#### 多峰函数
```python
f, df = TestFunctions.multimodal()
# 具有多个局部最优解的复杂函数
```

#### Rastrigin函数
```python
f, df = TestFunctions.rastrigin_1d(A=10.0)
# 高度多峰的测试函数
```

### 自定义函数

```python
# 方法1: 直接定义
def my_function(x):
    return x**4 - 4*x**3 + 6*x**2 - 4*x + 1

def my_derivative(x):
    return 4*x**3 - 12*x**2 + 12*x - 4

# 方法2: 使用字符串表达式
f, df = TestFunctions.from_expression("x**2 + sin(x)")
```

## 可视化功能

### 基本可视化

```python
# 创建动画
anim, history = visualizer.create_animation(
    x0=5.0,
    function_name="basic_example",
    save_gif=True,
    save_data=True
)
```

### 比较可视化

#### 比较不同学习率

```python
results = visualizer.compare_learning_rates(
    x0=5.0,
    function_name="lr_comparison",
    learning_rates=[0.01, 0.1, 0.5]
)
```

#### 比较算法变体

```python
results = visualizer.compare_optimization_variants(
    x0=-1.5,
    function_name="algorithm_comparison"
)
```

### 自定义可视化

```python
# 自定义图形参数
visualizer = GradientDescentVisualizer(
    f, df,
    x_range=[-5, 5],
    figsize=(20, 8),
    colors={
        'function': 'blue',
        'point': 'red',
        'path': 'green'
    }
)
```

## 高级用法

### 批量实验

```python
# 批量测试不同起始点
starting_points = [-4, -2, 0, 2, 4]
results = []

for x0 in starting_points:
    history = visualizer.optimize_with_history(
        x0=x0,
        learning_rate=0.1
    )
    results.append({
        'x0': x0,
        'final_x': history['x'][-1],
        'final_value': history['f'][-1],
        'iterations': len(history['x'])
    })
```

### 性能分析

```python
import time

# 测量优化时间
start_time = time.time()
history = visualizer.optimize_with_history(x0=5.0)
optimization_time = time.time() - start_time

print(f"优化时间: {optimization_time:.4f}秒")
print(f"每次迭代时间: {optimization_time/len(history['x']):.6f}秒")
```

### 收敛性分析

```python
import numpy as np
import matplotlib.pyplot as plt

# 分析收敛性
x_values = np.array(history['x'])
f_values = np.array(history['f'])

# 计算收敛误差
optimal_x = 2.0  # 已知最优解
errors = np.abs(x_values - optimal_x)

# 绘制收敛曲线
plt.semilogy(errors)
plt.xlabel('迭代次数')
plt.ylabel('误差 (对数尺度)')
plt.title('收敛性分析')
plt.grid(True)
plt.show()
```

### 参数敏感性分析

```python
# 测试不同学习率的敏感性
learning_rates = [0.001, 0.01, 0.1, 0.5, 1.0]
sensitivity_results = {}

for lr in learning_rates:
    try:
        history = visualizer.optimize_with_history(
            x0=5.0,
            learning_rate=lr,
            max_iterations=200
        )
        sensitivity_results[lr] = {
            'converged': history.get('converged', False),
            'iterations': len(history['x']),
            'final_value': history['f'][-1]
        }
    except:
        sensitivity_results[lr] = {'converged': False}

# 分析结果
for lr, result in sensitivity_results.items():
    print(f"学习率 {lr}: 收敛={result['converged']}")
```

## 最佳实践

### 学习率选择

1. **从中等值开始**: 通常从0.1开始尝试
2. **观察收敛行为**: 
   - 震荡 → 减小学习率
   - 收敛太慢 → 增大学习率
3. **使用自适应方法**: 对于复杂函数，考虑自适应学习率

### 函数选择

1. **简单函数**: 用于验证算法正确性
2. **经典测试函数**: 用于性能评估
3. **实际问题**: 根据具体应用选择

### 可视化设置

1. **合适的显示范围**: 确保能看到完整的优化过程
2. **适当的迭代次数**: 平衡动画长度和收敛效果
3. **清晰的标注**: 使用有意义的文件名和标题

### 性能优化

1. **批量实验时禁用GIF**: 节省时间和存储空间
2. **合理设置图形大小**: 平衡质量和性能
3. **使用适当的容忍度**: 避免不必要的迭代

### 结果分析

1. **保存优化数据**: 便于后续分析
2. **记录实验参数**: 确保结果可重现
3. **比较不同设置**: 找到最佳参数组合

### 错误处理

1. **检查函数定义**: 确保函数和导数正确
2. **验证参数范围**: 避免无效的参数设置
3. **监控收敛性**: 及时发现发散问题

## 常见问题解答

### Q: 为什么优化不收敛？
A: 可能的原因：
- 学习率过大导致震荡
- 函数没有全局最优解
- 初始点选择不当
- 导数计算错误

### Q: 如何选择合适的学习率？
A: 建议步骤：
1. 从0.1开始尝试
2. 观察收敛行为
3. 根据需要调整
4. 考虑使用自适应方法

### Q: 动画播放太快/太慢怎么办？
A: 调整动画间隔：
```python
# 在配置文件中修改
visualization:
  animation:
    interval: 200  # 毫秒，增大值使动画变慢
```

### Q: 如何处理多峰函数？
A: 建议方法：
- 尝试多个不同的起始点
- 使用动量方法
- 降低学习率
- 增加迭代次数

### Q: 内存使用过多怎么办？
A: 优化建议：
- 减少最大迭代次数
- 降低图形分辨率
- 禁用GIF保存
- 及时清理临时文件