# 开发指南

## 目录
1. [开发环境设置](#开发环境设置)
2. [项目架构](#项目架构)
3. [编码规范](#编码规范)
4. [测试指南](#测试指南)
5. [扩展开发](#扩展开发)
6. [性能优化](#性能优化)
7. [调试技巧](#调试技巧)
8. [贡献指南](#贡献指南)

## 开发环境设置

### 环境要求

- Python 3.8+
- Git
- 推荐使用虚拟环境

### 依赖安装

```bash
# 使用 mamba (推荐)
mamba install numpy matplotlib scipy sympy pyyaml

# 或使用 pip
pip install numpy matplotlib scipy sympy pyyaml
```

### 开发工具

推荐的开发工具：
- **IDE**: PyCharm, VSCode, 或 Trae AI
- **代码格式化**: black, autopep8
- **类型检查**: mypy
- **文档生成**: sphinx

### 项目克隆和设置

```bash
# 克隆项目
git clone <repository-url>
cd optimize

# 创建虚拟环境
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或
venv\Scripts\activate  # Windows

# 安装依赖
pip install -r requirements.txt

# 验证安装
python main.py --list-algorithms
```

## 项目架构

### 目录结构

```
optimize/
├── algorithms/          # 算法实现
│   ├── __init__.py     # 算法注册中心
│   └── gradient_descent/
│       ├── __init__.py
│       └── gradient_descent_visualizer.py
├── config/             # 配置管理
│   ├── __init__.py
│   ├── config.yaml     # 主配置文件
│   └── config_manager.py
├── utils/              # 工具模块
│   ├── __init__.py
│   ├── base_visualizer.py
│   ├── test_functions.py
│   └── file_manager.py
├── examples/           # 示例代码
│   ├── __init__.py
│   ├── basic_examples.py
│   ├── comparison_examples.py
│   └── advanced_examples.py
├── tests/              # 测试代码
├── docs/               # 文档
├── output/             # 输出文件
├── main.py             # 主入口
└── README.md
```

### 架构设计原则

1. **模块化**: 每个算法独立成模块
2. **可扩展**: 易于添加新算法和功能
3. **配置驱动**: 通过配置文件管理参数
4. **统一接口**: 所有算法遵循相同接口
5. **分离关注点**: 算法、可视化、配置分离

### 核心组件

#### 1. 算法注册系统

```python
# algorithms/__init__.py
ALGORITHM_REGISTRY = {
    'gradient_descent': GradientDescentVisualizer,
    # 新算法在此注册
}

def get_algorithm(name: str):
    """获取算法类"""
    if name not in ALGORITHM_REGISTRY:
        raise ValueError(f"未知算法: {name}")
    return ALGORITHM_REGISTRY[name]
```

#### 2. 配置管理系统

```python
# config/config_manager.py
class ConfigManager:
    """统一配置管理"""
    def __init__(self, config_path: str = None):
        self.config_path = config_path or "config/config.yaml"
        self.config = self.load_config()
    
    def get(self, key: str, default=None):
        """支持点分隔的嵌套键访问"""
        pass
```

#### 3. 基础可视化器

```python
# utils/base_visualizer.py
class BaseOptimizationVisualizer(ABC):
    """所有优化可视化器的基类"""
    
    @abstractmethod
    def optimize_with_history(self, x0, **kwargs) -> dict:
        """执行优化并返回历史记录"""
        pass
    
    @abstractmethod
    def _animate_frame(self, frame, history, ax1, ax2, line_func, 
                      point_func, point_current, text_info) -> tuple:
        """动画帧更新函数"""
        pass
```

## 编码规范

### Python 编码风格

遵循 PEP 8 标准，主要规则：

1. **缩进**: 使用4个空格
2. **行长度**: 最大79字符
3. **命名规范**:
   - 类名: `PascalCase`
   - 函数/变量: `snake_case`
   - 常量: `UPPER_CASE`
   - 私有成员: `_leading_underscore`

### 注释规范

#### 文档字符串

```python
def optimize_with_history(self, x0: float, learning_rate: float = 0.1, 
                         max_iterations: int = 100, tolerance: float = 1e-6) -> dict:
    """
    使用梯度下降法进行优化并记录历史。
    
    Args:
        x0 (float): 初始点
        learning_rate (float, optional): 学习率. Defaults to 0.1.
        max_iterations (int, optional): 最大迭代次数. Defaults to 100.
        tolerance (float, optional): 收敛容忍度. Defaults to 1e-6.
    
    Returns:
        dict: 包含优化历史的字典，包含以下键：
            - x (List[float]): x值历史
            - f (List[float]): 函数值历史
            - df (List[float]): 梯度历史
            - converged (bool): 是否收敛
            - iterations (int): 实际迭代次数
    
    Raises:
        ValueError: 当学习率为负数时
        RuntimeError: 当优化发散时
    
    Example:
        >>> visualizer = GradientDescentVisualizer(f, df)
        >>> history = visualizer.optimize_with_history(x0=5.0, learning_rate=0.1)
        >>> print(f"最终结果: {history['x'][-1]}")
    """
```

#### 行内注释

```python
# 计算梯度
gradient = self.df(current_x)

# 检查收敛条件
if abs(gradient) < tolerance:
    converged = True
    break

# 更新参数
current_x = current_x - learning_rate * gradient  # 梯度下降更新规则
```

### 类型提示

```python
from typing import Callable, Dict, List, Tuple, Optional, Union

class GradientDescentVisualizer:
    def __init__(self, 
                 f: Callable[[float], float],
                 df: Callable[[float], float],
                 x_range: List[float] = [-5, 5],
                 figsize: Optional[Tuple[int, int]] = None,
                 colors: Optional[Dict[str, str]] = None) -> None:
        """初始化梯度下降可视化器"""
        pass
```

### 错误处理

```python
def optimize_with_history(self, x0: float, **kwargs) -> dict:
    """优化函数"""
    try:
        # 参数验证
        if learning_rate <= 0:
            raise ValueError("学习率必须为正数")
        
        # 执行优化
        history = self._run_optimization(x0, **kwargs)
        
        return history
        
    except ValueError as e:
        self.logger.error(f"参数错误: {e}")
        raise
    except Exception as e:
        self.logger.error(f"优化过程中发生错误: {e}")
        raise RuntimeError(f"优化失败: {e}")
```

## 测试指南

### 测试结构

```
tests/
├── __init__.py
├── test_algorithms/
│   ├── __init__.py
│   └── test_gradient_descent.py
├── test_utils/
│   ├── __init__.py
│   ├── test_test_functions.py
│   └── test_file_manager.py
├── test_config/
│   ├── __init__.py
│   └── test_config_manager.py
└── test_integration/
    ├── __init__.py
    └── test_end_to_end.py
```

### 单元测试示例

```python
# tests/test_algorithms/test_gradient_descent.py
import unittest
import numpy as np
from algorithms.gradient_descent import GradientDescentVisualizer
from utils.test_functions import TestFunctions

class TestGradientDescentVisualizer(unittest.TestCase):
    """梯度下降可视化器测试"""
    
    def setUp(self):
        """测试前准备"""
        self.f, self.df = TestFunctions.quadratic(a=1.0, b=-4.0, c=5.0)
        self.visualizer = GradientDescentVisualizer(self.f, self.df)
    
    def test_optimize_with_history_convergence(self):
        """测试优化收敛性"""
        history = self.visualizer.optimize_with_history(
            x0=5.0, 
            learning_rate=0.1,
            tolerance=1e-6
        )
        
        # 验证收敛
        self.assertTrue(history['converged'])
        
        # 验证最终结果接近理论最优解 (x=2)
        final_x = history['x'][-1]
        self.assertAlmostEqual(final_x, 2.0, places=3)
    
    def test_optimize_with_invalid_learning_rate(self):
        """测试无效学习率"""
        with self.assertRaises(ValueError):
            self.visualizer.optimize_with_history(
                x0=5.0, 
                learning_rate=-0.1
            )
    
    def test_optimize_with_large_learning_rate(self):
        """测试过大学习率导致发散"""
        history = self.visualizer.optimize_with_history(
            x0=5.0, 
            learning_rate=2.0,  # 过大的学习率
            max_iterations=50
        )
        
        # 应该不收敛
        self.assertFalse(history['converged'])
    
    def tearDown(self):
        """测试后清理"""
        pass

if __name__ == '__main__':
    unittest.main()
```

### 集成测试

```python
# tests/test_integration/test_end_to_end.py
import unittest
import os
import tempfile
from main import main

class TestEndToEnd(unittest.TestCase):
    """端到端测试"""
    
    def setUp(self):
        """创建临时目录"""
        self.temp_dir = tempfile.mkdtemp()
    
    def test_main_basic_optimization(self):
        """测试主程序基本优化功能"""
        # 模拟命令行参数
        args = [
            'gradient_descent', 'quadratic',
            '--x0', '5.0',
            '--learning_rate', '0.1',
            '--no-gif',  # 不生成GIF以加快测试
            '--output_dir', self.temp_dir
        ]
        
        # 执行主程序
        result = main(args)
        
        # 验证结果
        self.assertEqual(result, 0)  # 成功退出
        
        # 验证输出文件存在
        output_files = os.listdir(self.temp_dir)
        self.assertTrue(any(f.endswith('.json') for f in output_files))
```

### 运行测试

```bash
# 运行所有测试
python -m pytest tests/

# 运行特定测试文件
python -m pytest tests/test_algorithms/test_gradient_descent.py

# 运行特定测试方法
python -m pytest tests/test_algorithms/test_gradient_descent.py::TestGradientDescentVisualizer::test_optimize_with_history_convergence

# 生成覆盖率报告
python -m pytest --cov=algorithms --cov=utils --cov=config tests/
```

## 扩展开发

### 添加新优化算法

#### 1. 创建算法目录

```bash
mkdir algorithms/new_algorithm
touch algorithms/new_algorithm/__init__.py
touch algorithms/new_algorithm/new_algorithm_visualizer.py
```

#### 2. 实现算法类

```python
# algorithms/new_algorithm/new_algorithm_visualizer.py
from utils.base_visualizer import BaseOptimizationVisualizer
import numpy as np

class NewAlgorithmVisualizer(BaseOptimizationVisualizer):
    """新算法可视化器"""
    
    def __init__(self, f, df, **kwargs):
        super().__init__(f, df, **kwargs)
        self.algorithm_name = "new_algorithm"
    
    def optimize_with_history(self, x0: float, **kwargs) -> dict:
        """实现新算法的优化逻辑"""
        # 获取配置参数
        config = self.config_manager.get_algorithm_config(self.algorithm_name)
        
        # 算法参数
        param1 = kwargs.get('param1', config.get('param1', 0.1))
        param2 = kwargs.get('param2', config.get('param2', 0.9))
        max_iterations = kwargs.get('max_iterations', config.get('max_iterations', 100))
        tolerance = kwargs.get('tolerance', config.get('tolerance', 1e-6))
        
        # 初始化
        current_x = x0
        history = {
            'x': [current_x],
            'f': [self.f(current_x)],
            'df': [self.df(current_x)],
            'converged': False,
            'iterations': 0
        }
        
        # 算法主循环
        for i in range(max_iterations):
            # 实现新算法的更新规则
            gradient = self.df(current_x)
            
            # 检查收敛
            if abs(gradient) < tolerance:
                history['converged'] = True
                break
            
            # 新算法的更新规则（示例）
            current_x = current_x - param1 * gradient + param2 * some_term
            
            # 记录历史
            history['x'].append(current_x)
            history['f'].append(self.f(current_x))
            history['df'].append(gradient)
        
        history['iterations'] = len(history['x'])
        return history
    
    def _animate_frame(self, frame, history, ax1, ax2, line_func, 
                      point_func, point_current, text_info):
        """动画帧更新（可以自定义可视化效果）"""
        # 调用父类的默认实现
        return super()._animate_frame(frame, history, ax1, ax2, line_func, 
                                    point_func, point_current, text_info)
```

#### 3. 注册算法

```python
# algorithms/new_algorithm/__init__.py
from .new_algorithm_visualizer import NewAlgorithmVisualizer

__all__ = ['NewAlgorithmVisualizer']
```

```python
# algorithms/__init__.py
from .new_algorithm import NewAlgorithmVisualizer

ALGORITHM_REGISTRY = {
    'gradient_descent': GradientDescentVisualizer,
    'new_algorithm': NewAlgorithmVisualizer,  # 添加新算法
}
```

#### 4. 添加配置

```yaml
# config/config.yaml
algorithms:
  new_algorithm:
    param1: 0.1
    param2: 0.9
    max_iterations: 100
    tolerance: 1e-6
```

#### 5. 创建测试

```python
# tests/test_algorithms/test_new_algorithm.py
import unittest
from algorithms.new_algorithm import NewAlgorithmVisualizer
from utils.test_functions import TestFunctions

class TestNewAlgorithmVisualizer(unittest.TestCase):
    def setUp(self):
        self.f, self.df = TestFunctions.quadratic()
        self.visualizer = NewAlgorithmVisualizer(self.f, self.df)
    
    def test_basic_optimization(self):
        history = self.visualizer.optimize_with_history(x0=5.0)
        self.assertIsInstance(history, dict)
        self.assertIn('x', history)
        self.assertIn('f', history)
```

### 添加新测试函数

```python
# utils/test_functions.py
class TestFunctions:
    @staticmethod
    def new_function(param1=1.0, param2=2.0):
        """
        新测试函数: f(x) = param1 * x^2 + param2 * sin(x)
        
        Args:
            param1 (float): 二次项系数
            param2 (float): 正弦项系数
        
        Returns:
            tuple: (函数, 导数函数)
        """
        def f(x):
            return param1 * x**2 + param2 * np.sin(x)
        
        def df(x):
            return 2 * param1 * x + param2 * np.cos(x)
        
        return f, df
    
    @staticmethod
    def get_function_info(func_name: str) -> dict:
        """获取函数信息"""
        info_dict = {
            # ... 现有函数信息 ...
            'new_function': {
                'name': '新测试函数',
                'description': '二次函数与正弦函数的组合',
                'parameters': ['param1', 'param2'],
                'difficulty': 'medium',
                'global_minimum': '依赖参数'
            }
        }
        return info_dict.get(func_name, {})
```

## 性能优化

### 计算优化

#### 1. 向量化操作

```python
# 避免循环
# 慢速版本
history_f = []
for x in history_x:
    history_f.append(self.f(x))

# 快速版本
history_f = [self.f(x) for x in history_x]  # 或使用numpy向量化
```

#### 2. 缓存机制

```python
from functools import lru_cache

class OptimizedVisualizer:
    @lru_cache(maxsize=1000)
    def _cached_function_eval(self, x: float) -> float:
        """缓存函数评估结果"""
        return self.f(x)
```

#### 3. 早停机制

```python
def optimize_with_early_stopping(self, x0, patience=10, **kwargs):
    """带早停的优化"""
    best_value = float('inf')
    patience_counter = 0
    
    for i in range(max_iterations):
        current_value = self.f(current_x)
        
        if current_value < best_value:
            best_value = current_value
            patience_counter = 0
        else:
            patience_counter += 1
            
        if patience_counter >= patience:
            break  # 早停
```

### 内存优化

#### 1. 生成器使用

```python
def optimization_generator(self, x0, **kwargs):
    """使用生成器节省内存"""
    current_x = x0
    
    for i in range(max_iterations):
        yield {
            'iteration': i,
            'x': current_x,
            'f': self.f(current_x),
            'df': self.df(current_x)
        }
        
        # 更新逻辑
        current_x = self._update_step(current_x)
```

#### 2. 内存监控

```python
import psutil
import os

def monitor_memory_usage():
    """监控内存使用"""
    process = psutil.Process(os.getpid())
    memory_info = process.memory_info()
    print(f"内存使用: {memory_info.rss / 1024 / 1024:.2f} MB")
```

### 可视化优化

#### 1. 减少绘图频率

```python
def create_optimized_animation(self, x0, **kwargs):
    """优化的动画创建"""
    # 只保存关键帧
    key_frames = self._select_key_frames(history)
    
    # 降低帧率
    interval = kwargs.get('interval', 200)  # 增加间隔
```

#### 2. 异步保存

```python
import threading

def save_gif_async(self, animation, filename):
    """异步保存GIF"""
    def save_worker():
        animation.save(filename, writer='pillow')
    
    thread = threading.Thread(target=save_worker)
    thread.start()
    return thread
```

## 调试技巧

### 日志调试

```python
import logging

# 设置日志
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

class GradientDescentVisualizer:
    def __init__(self, *args, **kwargs):
        self.logger = logging.getLogger(self.__class__.__name__)
    
    def optimize_with_history(self, x0, **kwargs):
        self.logger.debug(f"开始优化，初始点: {x0}")
        
        for i in range(max_iterations):
            self.logger.debug(f"迭代 {i}: x={current_x:.6f}, f={self.f(current_x):.6f}")
            
            # 优化逻辑
            
        self.logger.info(f"优化完成，最终结果: {current_x:.6f}")
```

### 可视化调试

```python
def debug_optimization_path(self, history):
    """可视化调试优化路径"""
    import matplotlib.pyplot as plt
    
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    # 参数变化
    axes[0, 0].plot(history['x'])
    axes[0, 0].set_title('参数变化')
    axes[0, 0].set_xlabel('迭代次数')
    axes[0, 0].set_ylabel('x值')
    
    # 函数值变化
    axes[0, 1].plot(history['f'])
    axes[0, 1].set_title('函数值变化')
    axes[0, 1].set_xlabel('迭代次数')
    axes[0, 1].set_ylabel('f(x)')
    
    # 梯度变化
    axes[1, 0].plot(history['df'])
    axes[1, 0].set_title('梯度变化')
    axes[1, 0].set_xlabel('迭代次数')
    axes[1, 0].set_ylabel('df/dx')
    
    # 步长变化
    steps = [abs(history['x'][i+1] - history['x'][i]) 
             for i in range(len(history['x'])-1)]
    axes[1, 1].plot(steps)
    axes[1, 1].set_title('步长变化')
    axes[1, 1].set_xlabel('迭代次数')
    axes[1, 1].set_ylabel('步长')
    
    plt.tight_layout()
    plt.show()
```

### 性能分析

```python
import cProfile
import pstats

def profile_optimization(self, x0, **kwargs):
    """性能分析"""
    profiler = cProfile.Profile()
    profiler.enable()
    
    # 执行优化
    history = self.optimize_with_history(x0, **kwargs)
    
    profiler.disable()
    
    # 分析结果
    stats = pstats.Stats(profiler)
    stats.sort_stats('cumulative')
    stats.print_stats(10)  # 显示前10个最耗时的函数
    
    return history
```

## 贡献指南

### 代码贡献流程

1. **Fork 项目**
2. **创建特性分支**
   ```bash
   git checkout -b feature/new-algorithm
   ```

3. **开发和测试**
   ```bash
   # 编写代码
   # 添加测试
   python -m pytest tests/
   ```

4. **提交代码**
   ```bash
   git add .
   git commit -m "添加新的优化算法: XXX"
   ```

5. **推送分支**
   ```bash
   git push origin feature/new-algorithm
   ```

6. **创建 Pull Request**

### 提交信息规范

使用以下格式：

```
类型(范围): 简短描述

详细描述（可选）

相关问题: #123
```

类型包括：
- `feat`: 新功能
- `fix`: 错误修复
- `docs`: 文档更新
- `style`: 代码格式化
- `refactor`: 代码重构
- `test`: 测试相关
- `chore`: 构建过程或辅助工具的变动

### 代码审查清单

- [ ] 代码遵循项目编码规范
- [ ] 添加了适当的测试
- [ ] 测试通过
- [ ] 添加了必要的文档
- [ ] 更新了相关配置文件
- [ ] 性能影响可接受
- [ ] 向后兼容性

### 文档贡献

1. **API文档**: 更新 `docs/api_reference.md`
2. **用户指南**: 更新 `docs/user_guide.md`
3. **示例代码**: 添加到 `examples/` 目录
4. **README**: 更新主要功能说明

### 问题报告

报告问题时请包含：

1. **环境信息**
   - Python版本
   - 操作系统
   - 依赖版本

2. **重现步骤**
   - 详细的操作步骤
   - 输入参数
   - 期望结果 vs 实际结果

3. **错误信息**
   - 完整的错误堆栈
   - 相关日志

4. **最小重现示例**
   ```python
   # 能重现问题的最小代码示例
   ```

### 功能请求

提出功能请求时请说明：

1. **使用场景**: 为什么需要这个功能
2. **预期行为**: 功能应该如何工作
3. **替代方案**: 是否有其他解决方法
4. **实现建议**: 如果有想法，请分享

通过遵循这些开发指南，我们可以确保项目的代码质量、可维护性和扩展性。欢迎所有形式的贡献！