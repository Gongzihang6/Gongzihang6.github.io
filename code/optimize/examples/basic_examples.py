"""
基础优化示例
展示各种优化算法的基本使用方法
"""

import sys
from pathlib import Path

# 添加项目根目录到路径
sys.path.append(str(Path(__file__).parent.parent))

from algorithms.gradient_descent import GradientDescentVisualizer
from algorithms.momentum import MomentumVisualizer
from config import get_config

def example_quadratic_function():
    """二次函数优化示例"""
    print("=" * 60)
    print("示例1: 二次函数优化 - 梯度下降")
    print("=" * 60)
    
    # 获取测试函数
    from utils.test_functions import TestFunctions
    f, df = TestFunctions.get_function_by_name('quadratic')
    
    # 创建梯度下降可视化器
    visualizer = GradientDescentVisualizer(f, df)
    
    # 执行优化并生成动画
    anim, history = visualizer.create_animation(
        x0=5.0,
        function_name='quadratic',
        learning_rate=0.1,
        max_iterations=50,
        save_gif=True,
        save_data=True
    )
    
    print(f"优化完成！最终结果: x = {history['x_values'][-1]:.6f}, f(x) = {history['f_values'][-1]:.6f}")
    print(f"迭代次数: {len(history['x_values'])}")
    print()


def example_cubic_function():
    """三次函数优化示例"""
    print("=" * 60)
    print("示例2: 三次函数优化 - 梯度下降")
    print("=" * 60)
    
    # 获取测试函数
    from utils.test_functions import TestFunctions
    f, df = TestFunctions.get_function_by_name('cubic')
    
    # 创建梯度下降可视化器
    visualizer = GradientDescentVisualizer(f, df)
    
    # 执行优化并生成动画
    anim, history = visualizer.create_animation(
        x0=3.0,
        function_name='cubic',
        learning_rate=0.01,
        max_iterations=100,
        save_gif=True,
        save_data=True
    )
    
    print(f"优化完成！最终结果: x = {history['x_values'][-1]:.6f}, f(x) = {history['f_values'][-1]:.6f}")
    print(f"迭代次数: {len(history['x_values'])}")
    print()


def example_rosenbrock_function():
    """Rosenbrock函数优化示例"""
    print("=" * 60)
    print("示例3: Rosenbrock函数优化 - 梯度下降")
    print("=" * 60)
    
    # 获取测试函数
    from utils.test_functions import TestFunctions
    f, df = TestFunctions.get_function_by_name('rosenbrock_1d')
    
    # 创建梯度下降可视化器
    visualizer = GradientDescentVisualizer(f, df)
    
    # 执行优化并生成动画
    anim, history = visualizer.create_animation(
        x0=2.0,
        function_name='rosenbrock_1d',
        learning_rate=0.001,
        max_iterations=200,
        save_gif=True,
        save_data=True
    )
    
    print(f"优化完成！最终结果: x = {history['x_values'][-1]:.6f}, f(x) = {history['f_values'][-1]:.6f}")
    print(f"迭代次数: {len(history['x_values'])}")
    print()


def example_multimodal_function():
    """多峰函数优化示例"""
    print("=" * 60)
    print("示例4: 多峰函数优化 - 梯度下降")
    print("=" * 60)
    
    # 获取测试函数
    from utils.test_functions import TestFunctions
    f, df = TestFunctions.get_function_by_name('multi_modal')
    
    # 创建梯度下降可视化器
    visualizer = GradientDescentVisualizer(f, df)
    
    # 执行优化并生成动画
    anim, history = visualizer.create_animation(
        x0=4.0,
        function_name='multi_modal',
        learning_rate=0.05,
        max_iterations=150,
        save_gif=True,
        save_data=True
    )
    
    print(f"优化完成！最终结果: x = {history['x_values'][-1]:.6f}, f(x) = {history['f_values'][-1]:.6f}")
    print(f"迭代次数: {len(history['x_values'])}")
    print()


def example_adaptive_learning_rate():
    """自适应学习率梯度下降示例"""
    print("=" * 60)
    print("示例5: 自适应学习率梯度下降")
    print("=" * 60)
    
    # 获取测试函数
    from utils.test_functions import TestFunctions
    f, df = TestFunctions.get_function_by_name('rosenbrock_1d')
    
    # 创建梯度下降可视化器
    visualizer = GradientDescentVisualizer(f, df)
    
    # 执行自适应学习率优化
    anim, history = visualizer.create_animation(
        x0=2.0,
        function_name='rosenbrock_1d',
        learning_rate=0.001,  # 降低学习率避免溢出
        max_iterations=200,
        save_gif=True,
        save_data=True
    )
    
    print(f"优化完成！最终结果: x = {history['x_values'][-1]:.6f}, f(x) = {history['f_values'][-1]:.6f}")
    print(f"迭代次数: {len(history['x_values'])}")
    print()


def example_momentum_gradient_descent():
    """动量梯度下降示例"""
    print("=" * 60)
    print("示例6: 动量梯度下降")
    print("=" * 60)
    
    # 获取测试函数
    from utils.test_functions import TestFunctions
    f, df = TestFunctions.get_function_by_name('rosenbrock_1d')
    
    # 创建梯度下降可视化器
    visualizer = GradientDescentVisualizer(f, df)
    
    # 执行动量优化
    anim, history = visualizer.create_animation(
        x0=2.0,
        function_name='rosenbrock_1d',
        learning_rate=0.001,  # 降低学习率避免溢出
        max_iterations=200,
        save_gif=True,
        save_data=True
    )
    
    print(f"优化完成！最终结果: x = {history['x_values'][-1]:.6f}, f(x) = {history['f_values'][-1]:.6f}")
    print(f"迭代次数: {len(history['x_values'])}")
    print()


def example_momentum_optimization():
    """动量法优化示例"""
    print("=" * 60)
    print("示例7: 动量优化算法")
    print("=" * 60)
    
    # 获取测试函数
    from utils.test_functions import TestFunctions
    f, df = TestFunctions.get_function_by_name('quadratic')
    
    # 创建动量法可视化器
    visualizer = MomentumVisualizer(f, df)
    
    # 设置参数
    x0 = -5.0
    learning_rate = 0.01
    momentum = 0.9
    
    # 执行优化
    result = visualizer.visualize_optimization(
        func_name='quadratic',
        x0=x0,
        learning_rate=learning_rate,
        momentum=momentum,
        save_gif=True,
        save_data=True
    )
    
    # 输出结果
    print(f"优化完成！最终结果: x = {result['info']['final_x']:.6f}, f(x) = {result['info']['final_y']:.6f}")
    print(f"迭代次数: {result['info']['iterations']}")
    print()

def run_basic_examples():
    """运行所有基础示例"""
    print("=== 基础优化示例 ===")
    
    # 示例1: 二次函数优化
    print("\n1. 二次函数优化")
    example_quadratic_function()
    
    # 示例2: 三次函数优化
    print("\n2. 三次函数优化")
    example_cubic_function()
    
    # 示例3: Rosenbrock函数优化
    print("\n3. Rosenbrock函数优化")
    example_rosenbrock_function()
    
    # 示例4: 多峰函数优化
    print("\n4. 多峰函数优化")
    example_multimodal_function()
    
    # 示例5: 自适应学习率
    print("\n5. 自适应学习率梯度下降")
    example_adaptive_learning_rate()
    
    # 示例6: 动量梯度下降
    print("\n6. 动量梯度下降")
    example_momentum_gradient_descent()
    
    # 示例7: 动量法优化
    print("\n7. 动量法优化")
    example_momentum_optimization()
    
    print("\n=== 所有基础示例完成 ===")

if __name__ == "__main__":
    run_basic_examples()