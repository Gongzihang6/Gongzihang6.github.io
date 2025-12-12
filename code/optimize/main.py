"""
优化算法可视化项目主入口
提供统一的命令行接口来运行各种优化算法
"""

import argparse
import sys
from pathlib import Path

# 添加项目根目录到路径
sys.path.append(str(Path(__file__).parent))

from algorithms import get_algorithm, get_available_algorithms
from utils.test_functions import TestFunctions
from config import get_config
from utils.base_visualizer import BaseOptimizationVisualizer
from utils.comparison import compare_algorithms

def main():
    """主函数"""
    parser = argparse.ArgumentParser(
        description='优化算法可视化工具',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例用法:
  python main.py gradient_descent quadratic --x0 5.0 --learning_rate 0.1
  python main.py gradient_descent rosenbrock_1d --x0 -1.5 --max_iterations 200
  python main.py --list-algorithms
  python main.py --list-functions
        """
    )
    
    # 基本参数
    parser.add_argument('algorithm', nargs='?', 
                       help='优化算法名称 (使用 --list-algorithms 查看可用算法)')
    parser.add_argument('function', nargs='?', 
                       help='测试函数名称 (使用 --list-functions 查看可用函数)')
    
    # 列表选项
    parser.add_argument('--list-algorithms', action='store_true',
                       help='列出所有可用的优化算法')
    parser.add_argument('--list-functions', action='store_true',
                       help='列出所有可用的测试函数')
    
    # 优化参数
    parser.add_argument('--x0', type=float, default=5.0,
                       help='初始点 (默认: 5.0)')
    parser.add_argument('--learning_rate', type=float,
                       help='学习率 (使用算法默认值)')
    parser.add_argument('--max_iterations', type=int,
                       help='最大迭代次数 (使用算法默认值)')
    parser.add_argument('--tolerance', type=float,
                       help='收敛容忍度 (使用算法默认值)')
    
    # 算法特定参数
    parser.add_argument('--momentum', type=float,
                       help='动量系数 (适用于动量法, 默认: 0.9)')
    parser.add_argument('--adaptive', action='store_true',
                       help='使用自适应学习率 (适用于梯度下降)')
    parser.add_argument('--decay_factor', type=float,
                       help='学习率衰减因子 (适用于自适应学习率, 默认: 0.9)')
    
    # 可视化参数
    parser.add_argument('--x_range', nargs=2, type=float, metavar=('MIN', 'MAX'),
                       help='x轴显示范围 (例如: --x_range -10 10)')
    parser.add_argument('--figsize', nargs=2, type=int, metavar=('WIDTH', 'HEIGHT'),
                       help='图形大小 (例如: --figsize 15 6)')
    
    # 输出参数
    parser.add_argument('--no-gif', action='store_true',
                       help='不保存GIF动画')
    parser.add_argument('--no-data', action='store_true',
                       help='不保存优化数据')
    
    # 函数参数
    parser.add_argument('--function_params', type=str,
                       help='函数参数 (JSON格式, 例如: \'{"a": 1.0, "b": 0.0}\')')
    
    # 比较模式
    parser.add_argument('--compare-learning-rates', nargs='+', type=float,
                       help='比较不同学习率 (例如: --compare-learning-rates 0.01 0.1 0.5)')
    parser.add_argument('--compare-variants', action='store_true',
                       help='比较算法变体 (仅适用于支持的算法)')
    
    args = parser.parse_args()
    
    # 处理列表选项
    if args.list_algorithms:
        print("可用的优化算法:")
        for algo in get_available_algorithms():
            print(f"  - {algo}")
        return
    
    if args.list_functions:
        print("可用的测试函数:")
        function_info = TestFunctions.get_function_info()
        for name, info in function_info.items():
            print(f"  - {name}: {info['name']} ({info['difficulty']})")
            print(f"    {info['description']}")
            print(f"    推荐范围: {info['recommended_range']}")
            print()
        return
    
    # 检查必需参数
    if not args.algorithm or not args.function:
        parser.error("请指定算法和函数名称，或使用 --list-algorithms 和 --list-functions 查看可用选项")
    
    try:
        # 获取算法类
        AlgorithmClass = get_algorithm(args.algorithm)
        
        # 实例化算法
        algorithm = AlgorithmClass()
        
        # 创建可视化器
        visualizer = BaseOptimizationVisualizer(algorithm)
        
        # 获取测试函数
        func_parts = TestFunctions.get_function(args.function)
        f, df = func_parts[0], func_parts[1]
        d2f = func_parts[2] if len(func_parts) > 2 else None

        # 准备优化参数
        optimize_kwargs = {}
        if args.learning_rate is not None:
            optimize_kwargs['learning_rate'] = args.learning_rate
        if args.max_iterations is not None:
            optimize_kwargs['max_iterations'] = args.max_iterations
        if args.tolerance is not None:
            optimize_kwargs['tolerance'] = args.tolerance
        if args.momentum is not None:
            optimize_kwargs['momentum'] = args.momentum
        
        print(f"开始运行 {args.algorithm} 算法")
        print(f"测试函数: {args.function}")
        print(f"初始点: x0 = {args.x0}")
        print(f"参数: {optimize_kwargs}")
        print("=" * 50)

        if args.compare_learning_rates:
            algorithms_to_compare = []
            for lr in args.compare_learning_rates:
                # 假设基础算法类支持 learning_rate 参数
                algo_instance = AlgorithmClass(learning_rate=lr)
                algorithms_to_compare.append(algo_instance)
            
            compare_algorithms(
                algorithms=algorithms_to_compare,
                x0=args.x0,
                function_name=f"{args.function}_lr_comparison",
                f=f, df=df, d2f=d2f
            )
        elif args.compare_variants:
            # 示例：比较梯度下降的三个变体
            from algorithms.gradient_descent.gradient_descent import GradientDescent
            from algorithms.gradient_descent.adaptive_gradient_descent import AdaptiveGradientDescent
            from algorithms.gradient_descent.momentum_gradient_descent import MomentumGradientDescent
            
            algorithms_to_compare = [
                GradientDescent(),
                AdaptiveGradientDescent(),
                MomentumGradientDescent()
            ]
            compare_algorithms(
                algorithms=algorithms_to_compare,
                x0=args.x0,
                function_name=f"{args.function}_variant_comparison",
                f=f, df=df, d2f=d2f
            )
        else:
            # 运行优化和可视化
            anim, history = visualizer.run(
                x0=args.x0,
                f=f,
                df=df,
                d2f=d2f,
                function_name=args.function,
                save_gif=not args.no_gif,
                save_data=not args.no_data,
                **optimize_kwargs
            )
        
    except Exception as e:
        print(f"错误: {e}")
        sys.exit(1)

def run_examples():
    """运行示例"""
    print("运行优化算法示例...")
    print("=" * 50)

    # 获取算法和函数
    gd_class = get_algorithm('gradient_descent')
    f1, df1, d2f1 = TestFunctions.get_function('quadratic', a=1.0, b=2.0, c=0.0)

    # 实例化算法和可视化器
    gd_algorithm = gd_class()
    visualizer = BaseOptimizationVisualizer(gd_algorithm, x_range=(-1, 5))

    # 运行优化
    visualizer.run(
        x0=5.0,
        f=f1,
        df=df1,
        d2f=d2f1,
        function_name="quadratic_example",
        learning_rate=0.1,
        save_gif=True,
        save_data=True,
        show_plot=False  # 在非交互式模式下运行时，避免阻塞
    )

    print("\n所有示例运行完成！")
    print("请查看 output/ 目录中的结果文件。")

if __name__ == "__main__":
    # 如果没有命令行参数，运行示例
    if len(sys.argv) == 1:
        run_examples()
    else:
        main()
