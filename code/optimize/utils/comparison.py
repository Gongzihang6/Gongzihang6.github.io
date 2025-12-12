"""
提供比较不同优化算法性能的工具
"""

from typing import List, Dict, Any, Callable
from .base_visualizer import BaseOptimizationVisualizer
from algorithms.base_algorithm import OptimizationAlgorithm

from typing import List, Dict, Any, Callable, Optional

def compare_algorithms(algorithms: List[OptimizationAlgorithm], 
                       x0: float, 
                       function_name: str,
                       f: Callable, df: Callable, d2f: Optional[Callable] = None,
                       **kwargs):
    """
    比较多个优化算法的性能

    参数:
        algorithms: 要比较的算法实例列表
        f: 目标函数
        df: 目标函数的导数
        d2f: 目标函数的二阶导数
        x0: 初始点
        function_name: 函数名称
        **kwargs: 传递给所有算法的通用参数
    """
    print("开始算法比较...")
    results = []

    for algorithm in algorithms:
        print(f"\n--- 正在运行: {algorithm.get_name()} ---")
        visualizer = BaseOptimizationVisualizer(algorithm)
        
        _, history = visualizer.run(
            x0=x0,
            f=f,
            df=df,
            d2f=d2f,
            function_name=f"{function_name}_{algorithm.get_name()}",
            show_plot=False,
            **kwargs
        )
        
        results.append({
            'algorithm': algorithm.get_name(),
            'final_x': history['x_values'][-1],
            'final_f_x': history['f_values'][-1],
            'iterations': history['iterations'],
            'converged': history['converged']
        })

    # 在这里可以添加生成比较图表或报告的逻辑
    print("\n--- 比较结果 ---")
    for res in sorted(results, key=lambda r: r['final_f_x']):
        print(f"算法: {res['algorithm']:<25} | "
              f"最终 f(x): {res['final_f_x']:.6f} | "
              f"迭代次数: {res['iterations']:<4} | "
              f"收敛: {res['converged']}")
    
    return results
