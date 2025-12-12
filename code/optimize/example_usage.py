"""
梯度下降可视化使用示例
演示不同函数和参数设置下的优化效果
"""

import numpy as np
from GD import GradientDescentVisualizer

def example_1_quadratic():
    """
    示例1: 简单二次函数优化
    """
    print("\n" + "="*60)
    print("示例1: 简单二次函数 f(x) = (x-2)² + 1")
    print("="*60)
    
    # 定义简单二次函数
    def f(x):
        return (x - 2)**2 + 1
    
    def df(x):
        return 2 * (x - 2)
    
    # 创建可视化器
    visualizer = GradientDescentVisualizer(f, df, x_range=(-2, 6), figsize=(15, 6))
    
    # 运行优化
    anim, history = visualizer.create_animation(
        x0=-1.0,
        learning_rate=0.3,
        num_iterations=20,
        interval=300,
        save_gif=True,
        gif_filename='quadratic_optimization.gif'
    )

def example_2_complex_function():
    """
    示例2: 复杂多峰函数优化
    """
    print("\n" + "="*60)
    print("示例2: 复杂函数 f(x) = x⁴ - 4x³ + 4x² + 2")
    print("="*60)
    
    # 定义复杂函数
    def f(x):
        return x**4 - 4*x**3 + 4*x**2 + 2
    
    def df(x):
        return 4*x**3 - 12*x**2 + 8*x
    
    # 创建可视化器
    visualizer = GradientDescentVisualizer(f, df, x_range=(-1, 4), figsize=(15, 6))
    
    # 运行优化
    anim, history = visualizer.create_animation(
        x0=3.5,
        learning_rate=0.05,
        num_iterations=100,
        interval=150,
        save_gif=True,
        gif_filename='complex_function_optimization.gif'
    )

def example_3_different_learning_rates():
    """
    示例3: 比较不同学习率的效果
    """
    print("\n" + "="*60)
    print("示例3: 比较不同学习率 - f(x) = x² + 10sin(x)")
    print("="*60)
    
    # 使用原始函数
    def f(x):
        return x**2 + 10*np.sin(x)
    
    def df(x):
        return 2*x + 10*np.cos(x)
    
    learning_rates = [0.01, 0.1, 0.3]
    
    for i, lr in enumerate(learning_rates):
        print(f"\n运行学习率 = {lr} 的优化...")
        
        visualizer = GradientDescentVisualizer(f, df, x_range=(-8, 6), figsize=(15, 6))
        
        anim, history = visualizer.create_animation(
            x0=-5.0,
            learning_rate=lr,
            num_iterations=50,
            interval=200,
            save_gif=True,
            gif_filename=f'lr_{lr}_optimization.gif'
        )

def example_4_rosenbrock_function():
    """
    示例4: Rosenbrock函数的一维简化版本
    """
    print("\n" + "="*60)
    print("示例4: Rosenbrock类型函数 f(x) = 100(x²-1)² + (x-1)²")
    print("="*60)
    
    # 定义Rosenbrock类型函数
    def f(x):
        return 100 * (x**2 - 1)**2 + (x - 1)**2
    
    def df(x):
        return 400 * x * (x**2 - 1) + 2 * (x - 1)
    
    # 创建可视化器
    visualizer = GradientDescentVisualizer(f, df, x_range=(-2, 3), figsize=(15, 6))
    
    # 运行优化
    anim, history = visualizer.create_animation(
        x0=-1.5,
        learning_rate=0.001,  # 需要很小的学习率
        num_iterations=200,
        interval=100,
        save_gif=True,
        gif_filename='rosenbrock_optimization.gif'
    )

def compare_starting_points():
    """
    示例5: 比较不同起始点的优化结果
    """
    print("\n" + "="*60)
    print("示例5: 比较不同起始点 - f(x) = x² + 10sin(x)")
    print("="*60)
    
    # 使用原始函数
    def f(x):
        return x**2 + 10*np.sin(x)
    
    def df(x):
        return 2*x + 10*np.cos(x)
    
    starting_points = [-7, -3, 0, 3]
    
    for i, x0 in enumerate(starting_points):
        print(f"\n从起始点 x0 = {x0} 开始优化...")
        
        visualizer = GradientDescentVisualizer(f, df, x_range=(-8, 6), figsize=(15, 6))
        
        anim, history = visualizer.create_animation(
            x0=x0,
            learning_rate=0.1,
            num_iterations=50,
            interval=200,
            save_gif=True,
            gif_filename=f'start_point_{x0}_optimization.gif'
        )

def main():
    """
    主函数：运行所有示例
    """
    print("梯度下降可视化示例集合")
    print("本程序将演示不同函数和参数设置下的梯度下降优化过程")
    
    # 询问用户要运行哪个示例
    print("\n请选择要运行的示例:")
    print("1. 简单二次函数优化")
    print("2. 复杂多峰函数优化") 
    print("3. 不同学习率比较")
    print("4. Rosenbrock类型函数优化")
    print("5. 不同起始点比较")
    print("6. 运行所有示例")
    
    try:
        choice = input("\n请输入选择 (1-6): ").strip()
        
        if choice == '1':
            example_1_quadratic()
        elif choice == '2':
            example_2_complex_function()
        elif choice == '3':
            example_3_different_learning_rates()
        elif choice == '4':
            example_4_rosenbrock_function()
        elif choice == '5':
            compare_starting_points()
        elif choice == '6':
            print("运行所有示例...")
            example_1_quadratic()
            example_2_complex_function()
            example_3_different_learning_rates()
            example_4_rosenbrock_function()
            compare_starting_points()
        else:
            print("无效选择，运行默认示例...")
            example_1_quadratic()
            
    except KeyboardInterrupt:
        print("\n程序被用户中断")
    except Exception as e:
        print(f"运行时出错: {e}")
        print("运行默认示例...")
        example_1_quadratic()

if __name__ == "__main__":
    main()