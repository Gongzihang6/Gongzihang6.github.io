"""
测试所有已实现的优化算法
"""

from algorithms import get_available_algorithms, get_algorithm
from utils.base_visualizer import BaseOptimizationVisualizer
from utils.test_functions import TestFunctions

def test_all():
    """
    测试所有算法
    """
    available_algorithms = get_available_algorithms()
    print(f"可用的算法: {available_algorithms}")

    f, df, d2f = TestFunctions.get_function('quadratic')

    for algo_name in available_algorithms:
        print(f"\n--- 测试算法: {algo_name} ---")
        try:
            AlgoClass = get_algorithm(algo_name)
            algorithm = AlgoClass()
            
            visualizer = BaseOptimizationVisualizer(algorithm)
            
            visualizer.run(
                x0=5.0,
                f=f,
                df=df,
                d2f=d2f,
                function_name=f"test_{algo_name}",
                save_gif=True,
                save_data=True,
                show_plot=False
            )
            print(f"--- {algo_name} 测试成功 ---")
        except Exception as e:
            print(f"--- {algo_name} 测试失败: {e} ---")

if __name__ == "__main__":
    test_all()
