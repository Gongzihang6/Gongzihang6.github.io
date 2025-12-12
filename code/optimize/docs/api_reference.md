# API 参考文档

## 目录
1. [配置管理 (config)](#配置管理-config)
2. [算法模块 (algorithms)](#算法模块-algorithms)
3. [工具模块 (utils)](#工具模块-utils)
4. [示例模块 (examples)](#示例模块-examples)

## 配置管理 (config)

### ConfigManager

配置管理器类，负责加载和管理项目配置。

```python
from config import ConfigManager

config_manager = ConfigManager()
```

#### 方法

##### `__init__(config_path: str = None)`

初始化配置管理器。

**参数**:
- `config_path` (str, 可选): 配置文件路径，默认为 `config/config.yaml`

##### `load_config() -> dict`

加载配置文件。

**返回**:
- `dict`: 配置字典

**异常**:
- `FileNotFoundError`: 配置文件不存在
- `yaml.YAMLError`: YAML格式错误

##### `get(key: str, default=None)`

获取配置项。

**参数**:
- `key` (str): 配置键，支持点分隔的嵌套键（如 `algorithms.gradient_descent.learning_rate`）
- `default`: 默认值

**返回**:
- 配置值或默认值

##### `set(key: str, value)`

设置配置项。

**参数**:
- `key` (str): 配置键
- `value`: 配置值

##### `get_algorithm_config(algorithm_name: str) -> dict`

获取特定算法的配置。

**参数**:
- `algorithm_name` (str): 算法名称

**返回**:
- `dict`: 算法配置字典

##### `get_output_path(algorithm_name: str) -> str`

获取算法输出路径。

**参数**:
- `algorithm_name` (str): 算法名称

**返回**:
- `str`: 输出路径

##### `generate_filename(algorithm_name: str, function_name: str, file_type: str) -> str`

生成标准化文件名。

**参数**:
- `algorithm_name` (str): 算法名称
- `function_name` (str): 函数名称
- `file_type` (str): 文件类型（gif, json, png等）

**返回**:
- `str`: 生成的文件名

### 便捷函数

#### `get_config() -> dict`

获取全局配置实例。

#### `update_config(key: str, value)`

更新全局配置。

## 算法模块 (algorithms)

### GradientDescentVisualizer

梯度下降算法可视化器。

```python
from algorithms.gradient_descent import GradientDescentVisualizer

visualizer = GradientDescentVisualizer(f, df, x_range=[-5, 5])
```

#### 初始化

##### `__init__(f, df, x_range=[-5, 5], figsize=None, colors=None)`

**参数**:
- `f` (callable): 目标函数
- `df` (callable): 目标函数的导数
- `x_range` (list): x轴显示范围 [min, max]
- `figsize` (tuple, 可选): 图形大小
- `colors` (dict, 可选): 颜色配置

#### 优化方法

##### `optimize_with_history(x0, learning_rate=None, max_iterations=None, tolerance=None) -> dict`

标准梯度下降优化。

**参数**:
- `x0` (float): 初始点
- `learning_rate` (float, 可选): 学习率
- `max_iterations` (int, 可选): 最大迭代次数
- `tolerance` (float, 可选): 收敛容忍度

**返回**:
- `dict`: 包含优化历史的字典
  - `x`: x值历史
  - `f`: 函数值历史
  - `df`: 梯度历史
  - `converged`: 是否收敛
  - `iterations`: 迭代次数

##### `optimize_with_adaptive_learning_rate(x0, initial_learning_rate=None, decay_factor=None, max_iterations=None, tolerance=None) -> dict`

自适应学习率梯度下降。

**参数**:
- `x0` (float): 初始点
- `initial_learning_rate` (float, 可选): 初始学习率
- `decay_factor` (float, 可选): 衰减因子
- `max_iterations` (int, 可选): 最大迭代次数
- `tolerance` (float, 可选): 收敛容忍度

**返回**:
- `dict`: 优化历史字典（同上）

##### `optimize_with_momentum(x0, learning_rate=None, momentum=None, max_iterations=None, tolerance=None) -> dict`

动量梯度下降。

**参数**:
- `x0` (float): 初始点
- `learning_rate` (float, 可选): 学习率
- `momentum` (float, 可选): 动量系数
- `max_iterations` (int, 可选): 最大迭代次数
- `tolerance` (float, 可选): 收敛容忍度

**返回**:
- `dict`: 优化历史字典

#### 可视化方法

##### `create_animation(x0, function_name, method='standard', save_gif=True, save_data=True, **kwargs) -> tuple`

创建优化过程动画。

**参数**:
- `x0` (float): 初始点
- `function_name` (str): 函数名称（用于文件命名）
- `method` (str): 优化方法（'standard', 'adaptive', 'momentum'）
- `save_gif` (bool): 是否保存GIF
- `save_data` (bool): 是否保存数据
- `**kwargs`: 传递给优化方法的额外参数

**返回**:
- `tuple`: (动画对象, 优化历史)

##### `compare_learning_rates(x0, function_name, learning_rates=None, save_gif=True, save_data=True) -> dict`

比较不同学习率的效果。

**参数**:
- `x0` (float): 初始点
- `function_name` (str): 函数名称
- `learning_rates` (list, 可选): 学习率列表
- `save_gif` (bool): 是否保存GIF
- `save_data` (bool): 是否保存数据

**返回**:
- `dict`: 比较结果字典

##### `compare_optimization_variants(x0, function_name, save_gif=True, save_data=True) -> dict`

比较不同优化算法变体。

**参数**:
- `x0` (float): 初始点
- `function_name` (str): 函数名称
- `save_gif` (bool): 是否保存GIF
- `save_data` (bool): 是否保存数据

**返回**:
- `dict`: 比较结果字典

## 工具模块 (utils)

### BaseOptimizationVisualizer

抽象基类，定义优化可视化器的通用接口。

```python
from utils.base_visualizer import BaseOptimizationVisualizer

class MyVisualizer(BaseOptimizationVisualizer):
    # 实现抽象方法
    pass
```

#### 抽象方法

##### `optimize_with_history(x0, **kwargs) -> dict`

执行优化并返回历史记录。

##### `_animate_frame(frame, history, ax1, ax2, line_func, point_func, point_current, text_info) -> tuple`

动画帧更新函数。

#### 通用方法

##### `create_animation(x0, function_name, save_gif=True, save_data=True, **kwargs) -> tuple`

创建优化动画。

##### `save_optimization_data(history, filename) -> str`

保存优化数据到JSON文件。

##### `print_optimization_stats(history)`

打印优化统计信息。

### TestFunctions

测试函数库，提供各种优化测试函数。

```python
from utils.test_functions import TestFunctions

f, df = TestFunctions.quadratic(a=1.0, b=-4.0, c=5.0)
```

#### 简单函数

##### `quadratic(a=1.0, b=-4.0, c=5.0) -> tuple`

二次函数：f(x) = ax² + bx + c

**参数**:
- `a`, `b`, `c` (float): 二次函数系数

**返回**:
- `tuple`: (函数, 导数函数)

##### `cubic(a=1.0, b=-6.0, c=9.0, d=-4.0) -> tuple`

三次函数：f(x) = ax³ + bx² + cx + d

##### `quartic(a=1.0, b=-8.0, c=18.0, d=-16.0, e=5.0) -> tuple`

四次函数：f(x) = ax⁴ + bx³ + cx² + dx + e

#### 经典测试函数

##### `rosenbrock_1d(a=1.0, b=100.0) -> tuple`

一维Rosenbrock函数。

##### `beale_1d() -> tuple`

一维Beale函数。

##### `multimodal() -> tuple`

多峰函数。

##### `rastrigin_1d(A=10.0) -> tuple`

一维Rastrigin函数。

##### `ackley_1d(a=20.0, b=0.2, c=2*np.pi) -> tuple`

一维Ackley函数。

##### `schwefel_1d() -> tuple`

一维Schwefel函数。

##### `griewank_1d() -> tuple`

一维Griewank函数。

#### 工具方法

##### `get_function_info(func_name: str) -> dict`

获取函数信息。

**参数**:
- `func_name` (str): 函数名称

**返回**:
- `dict`: 函数信息字典

##### `from_expression(expression: str, x_symbol='x') -> tuple`

从字符串表达式创建函数。

**参数**:
- `expression` (str): 数学表达式
- `x_symbol` (str): 变量符号

**返回**:
- `tuple`: (函数, 导数函数)

### FileManager

文件管理器，处理文件和目录操作。

```python
from utils.file_manager import FileManager

file_manager = FileManager()
```

#### 目录管理

##### `ensure_directory_exists(directory_path: str)`

确保目录存在。

##### `create_directory_structure(base_path: str, structure: dict)`

创建目录结构。

##### `get_directory_size(directory_path: str) -> int`

获取目录大小。

#### 文件操作

##### `generate_filename(algorithm_name: str, function_name: str, file_type: str, timestamp: bool = True) -> str`

生成标准化文件名。

##### `save_json(data: dict, filepath: str)`

保存JSON数据。

##### `load_json(filepath: str) -> dict`

加载JSON数据。

##### `list_files(directory: str, pattern: str = '*', recursive: bool = False) -> list`

列出文件。

##### `clean_old_files(directory: str, max_age_days: int = 30)`

清理旧文件。

##### `backup_file(filepath: str) -> str`

备份文件。

##### `get_file_info(filepath: str) -> dict`

获取文件信息。

##### `compress_directory(directory_path: str, output_path: str)`

压缩目录。

#### 日志管理

##### `setup_logging(log_level: str = 'INFO')`

设置日志系统。

## 示例模块 (examples)

### 基础示例

#### `run_basic_examples()`

运行基础优化示例。

包含的示例：
- 二次函数优化
- 三次函数优化
- Rosenbrock函数优化
- 多峰函数优化
- 自适应学习率示例
- 动量方法示例

### 比较示例

#### `run_comparison_examples()`

运行比较分析示例。

包含的比较：
- 不同学习率比较
- 不同起始点比较
- 算法变体比较
- 函数难度比较
- 收敛容忍度比较

### 高级示例

#### `run_advanced_examples()`

运行高级功能示例。

包含的功能：
- 自定义函数优化
- 噪声梯度优化
- 批量优化
- 收敛性分析
- 性能分析

## 异常处理

### 常见异常

#### `ConfigurationError`

配置相关错误。

#### `OptimizationError`

优化过程错误。

#### `VisualizationError`

可视化相关错误。

### 异常处理示例

```python
try:
    visualizer = GradientDescentVisualizer(f, df)
    anim, history = visualizer.create_animation(x0=5.0, function_name="test")
except ConfigurationError as e:
    print(f"配置错误: {e}")
except OptimizationError as e:
    print(f"优化错误: {e}")
except VisualizationError as e:
    print(f"可视化错误: {e}")
except Exception as e:
    print(f"未知错误: {e}")
```

## 类型提示

项目使用类型提示来提高代码可读性和IDE支持。

### 常用类型

```python
from typing import Callable, Dict, List, Tuple, Optional, Union

# 函数类型
FunctionType = Callable[[float], float]
DerivativeType = Callable[[float], float]

# 历史记录类型
HistoryType = Dict[str, List[float]]

# 配置类型
ConfigType = Dict[str, Union[str, int, float, bool, Dict]]
```

## 扩展指南

### 添加新算法

1. 在 `algorithms/` 下创建新目录
2. 继承 `BaseOptimizationVisualizer`
3. 实现必要的抽象方法
4. 在 `algorithms/__init__.py` 中注册

### 添加新测试函数

1. 在 `TestFunctions` 类中添加静态方法
2. 返回 `(function, derivative)` 元组
3. 添加函数信息到 `get_function_info` 方法

### 自定义可视化

1. 继承相应的可视化器类
2. 重写 `_animate_frame` 方法
3. 自定义颜色和样式配置

## 性能优化

### 内存优化

- 使用生成器处理大数据集
- 及时清理不需要的变量
- 合理设置最大迭代次数

### 计算优化

- 缓存重复计算结果
- 使用向量化操作
- 并行处理多个实验

### 可视化优化

- 降低动画帧率
- 减少图形分辨率
- 禁用不必要的GIF保存