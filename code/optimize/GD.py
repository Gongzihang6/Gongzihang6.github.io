import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import FancyBboxPatch
import os

class GradientDescentVisualizer:
    """
    梯度下降可视化器类
    
    该类实现了梯度下降算法的可视化，包括：
    - 实时动画显示优化过程
    - 保存动画为GIF格式
    - 显示收敛信息和统计数据
    """
    
    def __init__(self, f, df, x_range=(-10, 10), figsize=(12, 8)):
        """
        初始化可视化器
        
        参数:
            f: 目标函数
            df: 目标函数的导数
            x_range: x轴显示范围，元组格式 (min, max)
            figsize: 图形大小，元组格式 (width, height)
        """
        self.f = f
        self.df = df
        self.x_range = x_range
        self.figsize = figsize
        
        # 初始化图形和子图
        self.fig, (self.ax1, self.ax2) = plt.subplots(1, 2, figsize=figsize)
        self.fig.suptitle('梯度下降算法可视化', fontsize=16, fontweight='bold')
        
        # 设置中文字体
        plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei']
        plt.rcParams['axes.unicode_minus'] = False
        
    def gradient_descent_with_history(self, x0, learning_rate, num_iterations, tolerance=1e-6):
        """
        执行梯度下降算法并记录完整历史
        
        参数:
            x0: 初始点
            learning_rate: 学习率
            num_iterations: 最大迭代次数
            tolerance: 收敛容忍度
            
        返回:
            dict: 包含优化历史的字典
        """
        x = x0
        history = {
            'x_values': [x],
            'f_values': [self.f(x)],
            'gradients': [self.df(x)],
            'learning_rates': [learning_rate]
        }
        
        print(f"开始梯度下降优化...")
        print(f"初始点: x0 = {x0:.4f}, f(x0) = {self.f(x0):.4f}")
        
        for i in range(num_iterations):
            gradient = self.df(x)
            x_new = x - learning_rate * gradient
            
            # 记录历史
            history['x_values'].append(x_new)
            history['f_values'].append(self.f(x_new))
            history['gradients'].append(self.df(x_new))
            history['learning_rates'].append(learning_rate)
            
            # 检查收敛
            if abs(x_new - x) < tolerance:
                print(f"在第 {i+1} 次迭代后收敛")
                break
                
            x = x_new
            
            # 每10次迭代打印一次进度
            if (i + 1) % 10 == 0:
                print(f"迭代 {i+1}: x = {x:.4f}, f(x) = {self.f(x):.4f}, 梯度 = {gradient:.4f}")
        
        # 转换为numpy数组以便处理
        for key in history:
            history[key] = np.array(history[key])
            
        print(f"优化完成！最终结果: x = {x:.4f}, f(x) = {self.f(x):.4f}")
        return history
    
    def setup_plots(self, history):
        """
        设置绘图区域和初始化图形元素
        
        参数:
            history: 优化历史数据
        """
        # 清空子图
        self.ax1.clear()
        self.ax2.clear()
        
        # 左侧子图：函数曲线和优化路径
        x_plot = np.linspace(self.x_range[0], self.x_range[1], 1000)
        y_plot = self.f(x_plot)
        
        self.ax1.plot(x_plot, y_plot, 'b-', linewidth=2, label='目标函数 f(x)')
        self.ax1.set_xlabel('x', fontsize=12)
        self.ax1.set_ylabel('f(x)', fontsize=12)
        self.ax1.set_title('梯度下降优化路径', fontsize=14, fontweight='bold')
        self.ax1.grid(True, alpha=0.3)
        self.ax1.legend()
        
        # 右侧子图：收敛曲线
        self.ax2.set_xlabel('迭代次数', fontsize=12)
        self.ax2.set_ylabel('函数值 f(x)', fontsize=12)
        self.ax2.set_title('收敛过程', fontsize=14, fontweight='bold')
        self.ax2.grid(True, alpha=0.3)
        
        # 初始化动画元素
        self.current_point, = self.ax1.plot([], [], 'ro', markersize=10, label='当前位置')
        self.path_line, = self.ax1.plot([], [], 'r--', alpha=0.7, linewidth=2, label='优化路径')
        self.convergence_line, = self.ax2.plot([], [], 'g-', linewidth=2, label='函数值')
        
        # 添加图例
        self.ax1.legend()
        self.ax2.legend()
        
        # 添加信息文本框
        self.info_text = self.ax1.text(0.02, 0.98, '', transform=self.ax1.transAxes, 
                                      fontsize=10, verticalalignment='top',
                                      bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))
    
    def animate_frame(self, frame, history):
        """
        动画帧更新函数
        
        参数:
            frame: 当前帧数
            history: 优化历史数据
        """
        if frame >= len(history['x_values']):
            return self.current_point, self.path_line, self.convergence_line, self.info_text
        
        # 更新当前点位置
        current_x = history['x_values'][frame]
        current_y = history['f_values'][frame]
        self.current_point.set_data([current_x], [current_y])
        
        # 更新路径
        path_x = history['x_values'][:frame+1]
        path_y = history['f_values'][:frame+1]
        self.path_line.set_data(path_x, path_y)
        
        # 更新收敛曲线
        iterations = np.arange(frame + 1)
        convergence_y = history['f_values'][:frame+1]
        self.convergence_line.set_data(iterations, convergence_y)
        
        # 动态调整右侧子图的y轴范围
        if frame > 0:
            y_min, y_max = np.min(convergence_y), np.max(convergence_y)
            y_range = y_max - y_min
            self.ax2.set_ylim(y_min - 0.1 * y_range, y_max + 0.1 * y_range)
            self.ax2.set_xlim(0, max(10, frame + 1))
        
        # 更新信息文本
        gradient = history['gradients'][frame]
        info_str = f'迭代: {frame}\n'
        info_str += f'x = {current_x:.4f}\n'
        info_str += f'f(x) = {current_y:.4f}\n'
        info_str += f'梯度 = {gradient:.4f}\n'
        info_str += f'学习率 = {history["learning_rates"][frame]:.4f}'
        self.info_text.set_text(info_str)
        
        return self.current_point, self.path_line, self.convergence_line, self.info_text
    
    def create_animation(self, x0, learning_rate=0.1, num_iterations=100, 
                        interval=100, save_gif=True, gif_filename='gradient_descent_animation.gif'):
        """
        创建并显示梯度下降动画
        
        参数:
            x0: 初始点
            learning_rate: 学习率
            num_iterations: 最大迭代次数
            interval: 动画帧间隔（毫秒）
            save_gif: 是否保存为GIF文件
            gif_filename: GIF文件名
        """
        # 执行梯度下降并获取历史数据
        history = self.gradient_descent_with_history(x0, learning_rate, num_iterations)
        
        # 设置绘图
        self.setup_plots(history)
        
        # 创建动画
        frames = len(history['x_values'])
        anim = animation.FuncAnimation(
            self.fig, 
            lambda frame: self.animate_frame(frame, history),
            frames=frames,
            interval=interval,
            blit=False,
            repeat=True
        )
        
        # 保存GIF动画
        if save_gif:
            print(f"正在保存动画为 {gif_filename}...")
            try:
                # 确保目录存在
                os.makedirs(os.path.dirname(os.path.abspath(gif_filename)), exist_ok=True)
                
                # 保存动画
                anim.save(gif_filename, writer='pillow', fps=10, dpi=100)
                print(f"动画已保存为: {os.path.abspath(gif_filename)}")
            except Exception as e:
                print(f"保存动画时出错: {e}")
                print("请确保已安装 Pillow 库: pip install Pillow")
        
        # 显示动画
        plt.tight_layout()
        plt.show()
        
        return anim, history

# 定义目标函数和其导数
def f(x):
    """
    目标函数: f(x) = x² + 10*sin(x)
    这是一个具有多个局部最小值的非凸函数
    """
    return x**2 + 10*np.sin(x)

def df(x):
    """
    目标函数的导数: f'(x) = 2x + 10*cos(x)
    """
    return 2*x + 10*np.cos(x)

def main():
    """
    主函数：演示梯度下降可视化
    """
    print("=" * 50)
    print("梯度下降算法可视化演示")
    print("=" * 50)
    
    # 创建可视化器
    visualizer = GradientDescentVisualizer(f, df, x_range=(-8, 6), figsize=(15, 6))
    
    # 设置参数
    x0 = -5.0          # 初始点
    learning_rate = 0.1 # 学习率
    num_iterations = 50 # 迭代次数
    
    print(f"参数设置:")
    print(f"  初始点: {x0}")
    print(f"  学习率: {learning_rate}")
    print(f"  最大迭代次数: {num_iterations}")
    print("-" * 50)
    
    # 创建并显示动画
    animation_obj, history = visualizer.create_animation(
        x0=x0,
        learning_rate=learning_rate,
        num_iterations=num_iterations,
        interval=200,  # 每帧200毫秒
        save_gif=True,
        gif_filename='gradient_descent_optimization.gif'
    )
    
    # 打印最终统计信息
    print("-" * 50)
    print("优化统计信息:")
    print(f"  总迭代次数: {len(history['x_values']) - 1}")
    print(f"  最终位置: x = {history['x_values'][-1]:.6f}")
    print(f"  最终函数值: f(x) = {history['f_values'][-1]:.6f}")
    print(f"  最终梯度: {history['gradients'][-1]:.6f}")
    print(f"  函数值改善: {history['f_values'][0] - history['f_values'][-1]:.6f}")
    print("=" * 50)

if __name__ == "__main__":
    main()