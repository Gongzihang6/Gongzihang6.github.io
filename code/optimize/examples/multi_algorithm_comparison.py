"""
多算法对比示例
展示不同优化算法在相同问题上的性能差异
"""

import sys
import os
import numpy as np
import matplotlib.pyplot as plt
from typing import Dict, List, Tuple

# 添加项目根目录到路径
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

# 导入所有算法
from algorithms.gradient_descent import GradientDescentVisualizer
from algorithms.momentum import MomentumVisualizer
from algorithms.rmsprop import RMSPropVisualizer
from algorithms.adam import AdamVisualizer
from algorithms.nesterov import NesterovVisualizer
from algorithms.adagrad import AdagradVisualizer
from algorithms.newton import NewtonVisualizer
from algorithms.bfgs import BFGSVisualizer
from utils.test_functions import TestFunctions
from config import get_config

def compare_all_algorithms_example():
    """
    对比所有优化算法在二次函数上的性能
    """
    print("=" * 60)
    print("多算法性能对比示例")
    print("=" * 60)
    
    # 获取配置
    config = get_config()
    
    # 定义测试函数
    test_func = TestFunctions()
    f, df = test_func.quadratic()
    
    # 为Newton方法定义二阶导数
    def d2f(x):
        return 2.0  # 二次函数的二阶导数是常数
    
    # 初始化所有算法
    algorithms = {
        '梯度下降': GradientDescentVisualizer(f, df),
        '动量法': MomentumVisualizer(f, df),
        'RMSProp': RMSPropVisualizer(f, df),
        'Adam': AdamVisualizer(f, df),
        'Nesterov': NesterovVisualizer(f, df),
        'Adagrad': AdagradVisualizer(f, df),
        '牛顿法': NewtonVisualizer(f, df, d2f=d2f),
        'BFGS': BFGSVisualizer(f, df)
    }
    
    # 运行所有算法
    x0 = -3.0
    results = {}
    
    print(f"初始点: x0 = {x0}")
    print(f"目标函数: f(x) = (x-2)² + 1")
    print(f"最优解: x* = 2.0, f* = 1.0")
    print("-" * 60)
    
    for name, visualizer in algorithms.items():
        print(f"运行 {name}...")
        try:
            if name == '牛顿法':
                # 牛顿法不需要学习率
                history = visualizer.optimize_with_history(x0)
            else:
                history = visualizer.optimize_with_history(x0)
            
            results[name] = {
                'history': history,
                'final_x': history['x_values'][-1],
                'final_f': history['f_values'][-1],
                'iterations': history['iterations'],
                'converged': history['converged']
            }
            
            print(f"  最终点: x = {results[name]['final_x']:.6f}")
            print(f"  最终值: f = {results[name]['final_f']:.6f}")
            print(f"  迭代次数: {results[name]['iterations']}")
            print(f"  是否收敛: {results[name]['converged']}")
            print()
            
        except Exception as e:
            print(f"  错误: {str(e)}")
            print()
    
    # 创建对比图
    create_comparison_plots(results, x0)
    
    return results

def compare_algorithms_on_multimodal():
    """
    对比算法在多峰函数上的性能
    """
    print("=" * 60)
    print("多峰函数上的算法对比")
    print("=" * 60)
    
    # 定义测试函数
    test_func = TestFunctions()
    f, df = test_func.multi_modal()
    
    # 选择几个主要算法进行对比
    algorithms = {
        '梯度下降': GradientDescentVisualizer(f, df, x_range=(-8, 6)),
        'Adam': AdamVisualizer(f, df, x_range=(-8, 6)),
        'RMSProp': RMSPropVisualizer(f, df, x_range=(-8, 6)),
        'Nesterov': NesterovVisualizer(f, df, x_range=(-8, 6))
    }
    
    # 测试不同起始点
    start_points = [-6.0, -2.0, 2.0, 4.0]
    
    print(f"目标函数: f(x) = x² + 10sin(x)")
    print(f"测试起始点: {start_points}")
    print("-" * 60)
    
    all_results = {}
    
    for x0 in start_points:
        print(f"\n起始点: x0 = {x0}")
        print("-" * 30)
        
        results = {}
        for name, visualizer in algorithms.items():
            try:
                history = visualizer.optimize_with_history(x0, max_iterations=200)
                results[name] = {
                    'final_x': history['x_values'][-1],
                    'final_f': history['f_values'][-1],
                    'iterations': history['iterations']
                }
                
                print(f"{name:12}: x = {results[name]['final_x']:8.4f}, "
                      f"f = {results[name]['final_f']:8.4f}, "
                      f"iter = {results[name]['iterations']:3d}")
                
            except Exception as e:
                print(f"{name:12}: 错误 - {str(e)}")
        
        all_results[x0] = results
    
    return all_results

def create_comparison_plots(results: Dict, x0: float):
    """
    创建算法对比图表
    """
    # 设置中文字体
    plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'DejaVu Sans']
    plt.rcParams['axes.unicode_minus'] = False
    
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12))
    
    # 1. 收敛曲线对比
    ax1.set_title('收敛曲线对比', fontsize=14, fontweight='bold')
    for name, result in results.items():
        if 'history' in result:
            iterations = range(len(result['history']['f_values']))
            ax1.plot(iterations, result['history']['f_values'], 
                    label=name, linewidth=2, marker='o', markersize=3)
    
    ax1.set_xlabel('迭代次数')
    ax1.set_ylabel('函数值')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    ax1.set_yscale('log')
    
    # 2. 最终结果对比
    names = list(results.keys())
    final_values = [results[name]['final_f'] for name in names]
    iterations = [results[name]['iterations'] for name in names]
    
    bars = ax2.bar(names, final_values, color='skyblue', alpha=0.7)
    ax2.set_title('最终函数值对比', fontsize=14, fontweight='bold')
    ax2.set_ylabel('最终函数值')
    ax2.tick_params(axis='x', rotation=45)
    
    # 在柱状图上添加数值标签
    for bar, value in zip(bars, final_values):
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height,
                f'{value:.4f}', ha='center', va='bottom')
    
    # 3. 迭代次数对比
    bars = ax3.bar(names, iterations, color='lightcoral', alpha=0.7)
    ax3.set_title('迭代次数对比', fontsize=14, fontweight='bold')
    ax3.set_ylabel('迭代次数')
    ax3.tick_params(axis='x', rotation=45)
    
    # 在柱状图上添加数值标签
    for bar, value in zip(bars, iterations):
        height = bar.get_height()
        ax3.text(bar.get_x() + bar.get_width()/2., height,
                f'{value}', ha='center', va='bottom')
    
    # 4. 优化路径对比（选择几个主要算法）
    ax4.set_title('优化路径对比', fontsize=14, fontweight='bold')
    
    # 绘制函数曲线
    x_range = np.linspace(-4, 6, 1000)
    test_func = TestFunctions()
    f_plot, _ = test_func.quadratic()
    y_range = [f_plot(x) for x in x_range]
    ax4.plot(x_range, y_range, 'b-', alpha=0.3, linewidth=1, label='f(x)')
    
    # 选择几个代表性算法绘制路径
    selected_algorithms = ['梯度下降', 'Adam', 'RMSProp', '牛顿法']
    colors = ['red', 'green', 'orange', 'purple']
    
    for i, name in enumerate(selected_algorithms):
        if name in results and 'history' in results[name]:
            history = results[name]['history']
            ax4.plot(history['x_values'], history['f_values'], 
                    color=colors[i], marker='o', markersize=4, 
                    linewidth=2, label=name, alpha=0.8)
    
    ax4.set_xlabel('x')
    ax4.set_ylabel('f(x)')
    ax4.legend()
    ax4.grid(True, alpha=0.3)
    
    plt.tight_layout()
    
    # 保存图片
    config = get_config()
    output_path = config.get_output_path('comparison')
    filename = config.generate_filename('multi_algorithm_comparison', 'comparison', 'png')
    filepath = os.path.join(output_path, filename)
    
    os.makedirs(output_path, exist_ok=True)
    plt.savefig(filepath, dpi=300, bbox_inches='tight', format='png')
    print(f"对比图已保存到: {filepath}")
    
    plt.show()

def performance_summary_table(results: Dict):
    """
    创建性能总结表格
    """
    print("\n" + "=" * 80)
    print("算法性能总结表")
    print("=" * 80)
    print(f"{'算法名称':<15} {'最终x值':<12} {'最终f值':<12} {'迭代次数':<8} {'收敛状态':<8}")
    print("-" * 80)
    
    for name, result in results.items():
        converged_str = "是" if result['converged'] else "否"
        print(f"{name:<15} {result['final_x']:<12.6f} {result['final_f']:<12.6f} "
              f"{result['iterations']:<8} {converged_str:<8}")
    
    print("-" * 80)

def main():
    """
    主函数：运行所有对比示例
    """
    try:
        # 1. 二次函数上的算法对比
        results1 = compare_all_algorithms_example()
        performance_summary_table(results1)
        
        print("\n" + "=" * 60)
        print("按Enter键继续多峰函数测试...")
        input()
        
        # 2. 多峰函数上的算法对比
        results2 = compare_algorithms_on_multimodal()
        
        print("\n算法对比完成！")
        
    except Exception as e:
        print(f"运行过程中出现错误: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()