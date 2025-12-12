"""
高级优化算法示例
演示复杂场景和高级功能的使用
"""

import sys
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

# 添加项目根目录到路径
sys.path.append(str(Path(__file__).parent.parent))

from algorithms.gradient_descent import GradientDescentVisualizer
from utils.test_functions import TestFunctions
from config import get_config

def custom_function_example():
    """示例1: 自定义函数优化"""
    print("=" * 60)
    print("示例1: 自定义函数优化")
    print("=" * 60)
    
    # 创建自定义函数: f(x) = sin(x) + 0.1*x^2
    def custom_f(x):
        return np.sin(x) + 0.1 * x**2
    
    def custom_df(x):
        return np.cos(x) + 0.2 * x
    
    print("自定义函数: f(x) = sin(x) + 0.1*x^2")
    
    # 创建可视化器
    visualizer = GradientDescentVisualizer(
        custom_f, custom_df,
        x_range=[-10, 10],
        figsize=(15, 6)
    )
    
    # 运行优化
    anim, history = visualizer.create_animation(
        x0=8.0,
        function_name="custom_sin_quadratic",
        learning_rate=0.1,
        max_iterations=200,
        save_gif=True,
        save_data=True
    )
    
    print(f"优化完成！最终结果: x = {history['x_values'][-1]:.6f}, f(x) = {history['f_values'][-1]:.6f}")
    print(f"迭代次数: {len(history['x_values'])}")

def noisy_gradient_example():
    """示例2: 带噪声梯度的优化"""
    print("\n" + "=" * 60)
    print("示例2: 带噪声梯度的优化")
    print("=" * 60)
    
    # 创建带噪声的梯度函数
    f, df_clean = TestFunctions.quadratic(a=1.0, b=-4.0, c=5.0)
    
    def noisy_df(x, noise_level=0.1):
        """带噪声的梯度"""
        clean_grad = df_clean(x)
        noise = np.random.normal(0, noise_level * abs(clean_grad))
        return clean_grad + noise
    
    print("使用带噪声的梯度进行优化")
    
    # 创建可视化器
    visualizer = GradientDescentVisualizer(
        f, noisy_df,
        x_range=[-1, 6],
        figsize=(15, 6)
    )
    
    # 设置随机种子以获得可重复的结果
    np.random.seed(42)
    
    # 运行优化
    anim, history = visualizer.create_animation(
        x0=5.0,
        function_name="noisy_gradient",
        learning_rate=0.05,  # 使用较小的学习率以应对噪声
        max_iterations=200,
        save_gif=True,
        save_data=True
    )
    
    print(f"优化完成！最终结果: x = {history['x_values'][-1]:.6f}, f(x) = {history['f_values'][-1]:.6f}")
    print(f"迭代次数: {len(history['x_values'])}")

def batch_optimization_example():
    """示例3: 批量优化不同起始点"""
    print("\n" + "=" * 60)
    print("示例3: 批量优化不同起始点")
    print("=" * 60)
    
    # 创建复杂的多峰函数
    f, df = TestFunctions.multi_modal()
    
    # 创建可视化器
    visualizer = GradientDescentVisualizer(
        f, df,
        x_range=[-5, 5],
        figsize=(20, 10)
    )
    
    # 多个起始点
    starting_points = np.linspace(-4.5, 4.5, 10)
    
    print(f"批量优化 {len(starting_points)} 个起始点")
    
    all_results = []
    
    for i, x0 in enumerate(starting_points):
        print(f"优化起始点 {i+1}/{len(starting_points)}: x0 = {x0:.2f}")
        
        # 运行优化（不保存GIF以节省时间）
        history = visualizer.optimize_with_history(
            x0=x0,
            learning_rate=0.05,
            max_iterations=100
        )
        
        result = {
            'x0': x0,
            'final_x': history['x_values'][-1],
            'final_value': history['f_values'][-1],
            'iterations': len(history['x_values']),
            'converged': bool(history.get('converged', False))
        }
        
        all_results.append(result)
    
    # 分析结果
    print("\n批量优化结果分析:")
    print("-" * 70)
    print(f"{'起始点':8s} {'最终点':10s} {'最终值':12s} {'迭代次数':8s} {'收敛':6s}")
    print("-" * 70)
    
    for result in all_results:
        converged_str = "是" if result['converged'] else "否"
        print(f"{result['x0']:8.2f} {result['final_x']:10.4f} "
              f"{result['final_value']:12.6f} {result['iterations']:8d} {converged_str:6s}")
    
    # 找到最佳结果
    best_result = min(all_results, key=lambda x: x['final_value'])
    print(f"\n最佳结果: 起始点 {best_result['x0']:.2f} -> "
          f"最终点 {best_result['final_x']:.4f}, "
          f"函数值 {best_result['final_value']:.6f}")
    
    # 为最佳结果创建动画
    print("为最佳结果创建动画...")
    anim, history = visualizer.create_animation(
        x0=best_result['x0'],
        function_name="batch_optimization_best",
        learning_rate=0.05,
        max_iterations=100,
        save_gif=True,
        save_data=True
    )

def convergence_analysis_example():
    """示例4: 收敛性分析"""
    print("\n" + "=" * 60)
    print("示例4: 收敛性分析")
    print("=" * 60)
    
    # 创建二次函数
    f, df = TestFunctions.quadratic(a=1.0, b=-4.0, c=5.0)
    
    # 创建可视化器
    visualizer = GradientDescentVisualizer(
        f, df,
        x_range=[-1, 6],
        figsize=(15, 6)
    )
    
    # 运行优化并获取详细历史
    history = visualizer.optimize_with_history(
        x0=5.0,
        learning_rate=0.1,
        max_iterations=100
    )
    
    # 计算收敛指标
    x_values = np.array(history['x_values'])
    f_values = np.array(history['f_values'])
    gradient_values = np.array(history['gradients'])
    
    # 计算相对误差
    optimal_x = 2.0  # 已知最优解
    optimal_f = 1.0  # 已知最优函数值
    
    x_errors = np.abs(x_values - optimal_x)
    f_errors = np.abs(f_values - optimal_f)
    
    # 创建收敛分析图
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    
    # 函数值收敛
    axes[0, 0].semilogy(f_errors)
    axes[0, 0].set_title('函数值收敛 (对数尺度)')
    axes[0, 0].set_xlabel('迭代次数')
    axes[0, 0].set_ylabel('|f(x) - f*|')
    axes[0, 0].grid(True)
    
    # 参数收敛
    axes[0, 1].semilogy(x_errors)
    axes[0, 1].set_title('参数收敛 (对数尺度)')
    axes[0, 1].set_xlabel('迭代次数')
    axes[0, 1].set_ylabel('|x - x*|')
    axes[0, 1].grid(True)
    
    # 梯度范数
    axes[1, 0].semilogy(np.abs(gradient_values))
    axes[1, 0].set_title('梯度范数 (对数尺度)')
    axes[1, 0].set_xlabel('迭代次数')
    axes[1, 0].set_ylabel('|∇f(x)|')
    axes[1, 0].grid(True)
    
    # 步长
    step_sizes = np.abs(np.diff(x_values))
    axes[1, 1].semilogy(step_sizes)
    axes[1, 1].set_title('步长 (对数尺度)')
    axes[1, 1].set_xlabel('迭代次数')
    axes[1, 1].set_ylabel('|x_{k+1} - x_k|')
    axes[1, 1].grid(True)
    
    plt.tight_layout()
    
    # 保存收敛分析图
    config = get_config()
    output_dir = config.get_output_path('gradient_descent')
    
    convergence_plot_path = output_dir / 'convergence_analysis.png'
    plt.savefig(convergence_plot_path, dpi=300, bbox_inches='tight')
    plt.show()
    
    print(f"收敛分析图已保存到: {convergence_plot_path}")
    
    # 计算收敛率
    if len(f_errors) > 10:
        # 线性收敛率估计
        log_errors = np.log(f_errors[5:])  # 跳过前几次迭代
        iterations = np.arange(len(log_errors))
        
        # 线性拟合
        coeffs = np.polyfit(iterations, log_errors, 1)
        convergence_rate = -coeffs[0]
        
        print(f"\n收敛性分析结果:")
        print(f"估计的线性收敛率: {convergence_rate:.4f}")
        print(f"最终函数值误差: {f_errors[-1]:.2e}")
        print(f"最终参数误差: {x_errors[-1]:.2e}")
        print(f"最终梯度范数: {abs(gradient_values[-1]):.2e}")

def performance_profiling_example():
    """示例5: 性能分析"""
    print("\n" + "=" * 60)
    print("示例5: 性能分析")
    print("=" * 60)
    
    import time
    
    # 测试不同复杂度的函数
    test_cases = [
        ("简单二次函数", TestFunctions.quadratic(), [-1, 6], 5.0, 0.1),
        ("三次函数", TestFunctions.cubic(), [-3, 3], 2.5, 0.01),
        ("Rosenbrock函数", TestFunctions.rosenbrock_1d(), [-2, 3], -1.5, 0.001),
        ("多峰函数", TestFunctions.multi_modal(), [-5, 5], 4.0, 0.05)
    ]
    
    performance_results = []
    
    for name, (f, df), x_range, x0, lr in test_cases:
        print(f"\n测试 {name}...")
        
        # 创建可视化器
        visualizer = GradientDescentVisualizer(
            f, df,
            x_range=x_range,
            figsize=(15, 6)
        )
        
        # 测量优化时间
        start_time = time.time()
        
        history = visualizer.optimize_with_history(
            x0=x0,
            learning_rate=lr,
            max_iterations=500
        )
        
        optimization_time = time.time() - start_time
        
        # 测量动画创建时间
        start_time = time.time()
        
        anim = visualizer.create_animation_from_history(
            history,
            function_name=f"performance_{name.replace(' ', '_')}",
            save_gif=False,  # 不保存GIF以节省时间
            save_data=True
        )
        
        animation_time = time.time() - start_time
        
        result = {
            'name': name,
            'iterations': len(history['x_values']),
            'optimization_time': optimization_time,
            'animation_time': animation_time,
            'total_time': optimization_time + animation_time,
            'time_per_iteration': optimization_time / len(history['x_values'])
        }
        
        performance_results.append(result)
        
        print(f"  迭代次数: {result['iterations']}")
        print(f"  优化时间: {result['optimization_time']:.4f}秒")
        print(f"  动画时间: {result['animation_time']:.4f}秒")
        print(f"  每次迭代时间: {result['time_per_iteration']:.6f}秒")
    
    # 打印性能总结
    print("\n" + "=" * 70)
    print("性能分析总结:")
    print("=" * 70)
    print(f"{'函数名':15s} {'迭代次数':8s} {'优化时间':10s} {'动画时间':10s} {'总时间':8s}")
    print("-" * 70)
    
    for result in performance_results:
        print(f"{result['name']:15s} {result['iterations']:8d} "
              f"{result['optimization_time']:10.4f} {result['animation_time']:10.4f} "
              f"{result['total_time']:8.4f}")

def run_advanced_examples():
    """运行所有高级示例"""
    print("开始运行高级优化算法示例...")
    print("这些示例将演示复杂场景和高级功能")
    print("结果将保存在 output/gradient_descent/ 目录中")
    
    try:
        # 运行各个高级示例
        custom_function_example()
        noisy_gradient_example()
        batch_optimization_example()
        convergence_analysis_example()
        performance_profiling_example()
        
        print("\n" + "=" * 60)
        print("所有高级示例运行完成！")
        print("=" * 60)
        print("请查看以下目录中的结果:")
        print("- GIF动画: output/gradient_descent/")
        print("- 优化数据: output/gradient_descent/")
        print("- 分析图表: output/gradient_descent/")
        print("- 日志文件: logs/")
        
    except Exception as e:
        print(f"运行高级示例时出错: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    run_advanced_examples()