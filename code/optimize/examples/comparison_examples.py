"""
比较优化算法示例
演示不同参数设置和算法变体的比较
"""

import sys
from pathlib import Path

# 添加项目根目录到路径
sys.path.append(str(Path(__file__).parent.parent))

from algorithms.gradient_descent import GradientDescentVisualizer
from utils.test_functions import TestFunctions
from config import get_config

def compare_learning_rates_example():
    """示例1: 比较不同学习率的效果"""
    print("=" * 60)
    print("示例1: 比较不同学习率的效果")
    print("=" * 60)
    
    # 创建二次函数
    f, df = TestFunctions.quadratic(a=1.0, b=-4.0, c=5.0)
    
    # 创建可视化器
    visualizer = GradientDescentVisualizer(
        f, df,
        x_range=[-1, 6],
        figsize=(20, 8)
    )
    
    # 比较不同学习率
    learning_rates = [0.01, 0.05, 0.1, 0.2, 0.5]
    
    print(f"比较学习率: {learning_rates}")
    
    results = visualizer.compare_learning_rates(
        x0=5.0,
        function_name="quadratic_lr_comparison",
        learning_rates=learning_rates
    )
    
    # 打印比较结果
    print("\n学习率比较结果:")
    print("-" * 50)
    for result in results:
        lr = result['parameters']['learning_rate']
        print(f"学习率 {lr:4.2f}: 迭代{result['iterations']:3d}次, "
              f"最终值 f(x)={result['final_f_x']:8.6f}, "
              f"改善 {result['improvement']:8.6f}")

def compare_starting_points_example():
    """示例2: 比较不同起始点的效果"""
    print("\n" + "=" * 60)
    print("示例2: 比较不同起始点的效果")
    print("=" * 60)
    
    # 创建多峰函数
    f, df = TestFunctions.multi_modal()
    
    # 创建可视化器
    visualizer = GradientDescentVisualizer(
        f, df,
        x_range=[-5, 5],
        figsize=(20, 8)
    )
    
    # 不同起始点
    starting_points = [-4.0, -2.0, 0.0, 2.0, 4.0]
    
    print(f"比较起始点: {starting_points}")
    
    # 为每个起始点运行优化
    results = {}
    for x0 in starting_points:
        print(f"运行起始点 x0 = {x0}")
        
        anim, history = visualizer.create_animation(
            x0=x0,
            function_name=f"multi_modal_start_{x0:+.1f}",
            learning_rate=0.05,
            max_iterations=200,
            save_gif=True,
            save_data=True
        )
        
        results[x0] = {
            'final_x': history['x_values'][-1],
            'final_value': history['f_values'][-1],
            'iterations': len(history['x_values']),
            'converged': history.get('converged', False)
        }
    
    # 打印比较结果
    print("\n起始点比较结果:")
    print("-" * 60)
    for x0, result in results.items():
        print(f"起始点 {x0:+5.1f}: 收敛到 x={result['final_x']:+7.4f}, "
              f"f(x)={result['final_value']:8.6f}, "
              f"迭代{result['iterations']:3d}次")

def compare_optimization_variants_example():
    """示例3: 比较优化算法变体"""
    print("\n" + "=" * 60)
    print("示例3: 比较优化算法变体")
    print("=" * 60)
    
    # 创建Rosenbrock函数（使用较小的参数避免数值溢出）
    f, df = TestFunctions.rosenbrock_1d(a=1.0, b=10.0)
    
    # 创建可视化器
    visualizer = GradientDescentVisualizer(
        f, df,
        x_range=[-2, 3],
        figsize=(20, 10)
    )
    
    print("比较标准梯度下降、自适应学习率和动量方法")
    
    # 比较算法变体
    results = visualizer.compare_optimization_variants(
        x0=-1.5,
        function_name="rosenbrock_variants_comparison"
    )
    
    # 打印比较结果
    print("\n算法变体比较结果:")
    print("-" * 70)
    for variant, result in results.items():
        print(f"{variant:20s}: 迭代{result['iterations']:3d}次, "
              f"最终值 f(x)={result['final_value']:10.8f}, "
              f"收敛时间 {result['convergence_time']:6.4f}秒")

def compare_functions_example():
    """示例4: 比较不同函数的优化难度"""
    print("\n" + "=" * 60)
    print("示例4: 比较不同函数的优化难度")
    print("=" * 60)
    
    # 定义测试函数
    test_functions = {
        'quadratic': (TestFunctions.quadratic(a=1.0, b=-4.0, c=5.0), [-1, 6], 5.0, 0.1),
        'cubic': (TestFunctions.cubic(), [-3, 3], 2.5, 0.01),
        'quartic': (TestFunctions.quartic(), [-3, 3], 2.0, 0.01),
        'rosenbrock': (TestFunctions.rosenbrock_1d(), [-2, 3], -1.5, 0.001),
        'beale': (TestFunctions.beale_1d(), [-5, 5], 4.0, 0.01)
    }
    
    results = {}
    
    for func_name, (func_tuple, x_range, x0, lr) in test_functions.items():
        print(f"\n测试函数: {func_name}")
        
        f, df = func_tuple
        
        # 创建可视化器
        visualizer = GradientDescentVisualizer(
            f, df,
            x_range=x_range,
            figsize=(15, 6)
        )
        
        # 运行优化
        anim, history = visualizer.create_animation(
            x0=x0,
            function_name=f"{func_name}_difficulty_test",
            learning_rate=lr,
            max_iterations=500,
            save_gif=True,
            save_data=True
        )
        
        results[func_name] = {
            'final_x': history['x_values'][-1],
            'final_value': history['f_values'][-1],
            'iterations': len(history['x_values']),
            'converged': history.get('converged', False),
            'learning_rate': lr
        }
    
    # 打印比较结果
    print("\n" + "=" * 70)
    print("函数优化难度比较结果:")
    print("=" * 70)
    print(f"{'函数名':12s} {'学习率':8s} {'迭代次数':8s} {'最终值':12s} {'收敛':6s}")
    print("-" * 70)
    
    for func_name, result in results.items():
        converged_str = "是" if result['converged'] else "否"
        print(f"{func_name:12s} {result['learning_rate']:8.3f} "
              f"{result['iterations']:8d} {result['final_value']:12.6f} {converged_str:6s}")

def tolerance_sensitivity_example():
    """示例5: 收敛容忍度敏感性分析"""
    print("\n" + "=" * 60)
    print("示例5: 收敛容忍度敏感性分析")
    print("=" * 60)
    
    # 创建二次函数
    f, df = TestFunctions.quadratic(a=1.0, b=-4.0, c=5.0)
    
    # 创建可视化器
    visualizer = GradientDescentVisualizer(
        f, df,
        x_range=[-1, 6],
        figsize=(15, 6)
    )
    
    # 不同的容忍度
    tolerances = [1e-2, 1e-3, 1e-4, 1e-5, 1e-6]
    
    print(f"测试容忍度: {tolerances}")
    
    results = {}
    
    for tol in tolerances:
        print(f"运行容忍度 {tol:.0e}")
        
        anim, history = visualizer.create_animation(
            x0=5.0,
            function_name=f"tolerance_{tol:.0e}",
            learning_rate=0.1,
            tolerance=tol,
            max_iterations=1000,
            save_gif=True,
            save_data=True
        )
        
        results[tol] = {
            'final_x': history['x_values'][-1],
            'final_value': history['f_values'][-1],
            'iterations': len(history['x_values']),
            'converged': history.get('converged', False)
        }
    
    # 打印比较结果
    print("\n容忍度敏感性分析结果:")
    print("-" * 60)
    print(f"{'容忍度':10s} {'迭代次数':8s} {'最终x值':12s} {'最终函数值':12s}")
    print("-" * 60)
    
    for tol, result in results.items():
        print(f"{tol:10.0e} {result['iterations']:8d} "
              f"{result['final_x']:12.8f} {result['final_value']:12.8f}")

def run_comparison_examples():
    """运行所有比较示例"""
    print("开始运行比较优化算法示例...")
    print("这些示例将演示不同参数和算法变体的比较")
    print("结果将保存在 output/gradient_descent/ 目录中")
    
    try:
        # 运行各个比较示例
        compare_learning_rates_example()
        compare_starting_points_example()
        compare_optimization_variants_example()
        compare_functions_example()
        tolerance_sensitivity_example()
        
        print("\n" + "=" * 60)
        print("所有比较示例运行完成！")
        print("=" * 60)
        print("请查看以下目录中的结果:")
        print("- GIF动画: output/gradient_descent/")
        print("- 优化数据: output/gradient_descent/")
        print("- 比较图表: output/gradient_descent/")
        print("- 日志文件: logs/")
        
    except Exception as e:
        print(f"运行比较示例时出错: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    run_comparison_examples()