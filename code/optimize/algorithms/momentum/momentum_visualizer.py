"""
动量法优化算法可视化器
实现动量法优化算法的核心逻辑和可视化功能
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Circle
import os
import json
from typing import List, Tuple, Dict, Any, Optional, Callable
import logging
import warnings
import sys
from pathlib import Path

# 添加项目根目录到路径
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from utils.base_visualizer import BaseOptimizationVisualizer
from utils.test_functions import TestFunctions
from config import get_config


class MomentumVisualizer(BaseOptimizationVisualizer):
    """
    动量法优化算法可视化器
    
    动量法通过累积历史梯度信息来加速收敛，特别适用于：
    - 具有噪声梯度的优化问题
    - 存在局部最小值的复杂函数
    - 需要快速收敛的场景
    """
    
    def __init__(self, f: Callable, df: Callable, config_manager=None):
        """
        初始化动量法可视化器
        
        参数:
            f: 目标函数
            df: 目标函数的导数
            config_manager: 配置管理器实例
        """
        super().__init__("momentum", f, df)
        self.algorithm_name = "momentum"
        self.logger = logging.getLogger(__name__)
        
        # 初始化配置管理器
        if config_manager is None:
            from config import get_config
            self.config_manager = get_config()
        else:
            self.config_manager = config_manager
        
    def _get_algorithm_display_name(self) -> str:
        """
        获取算法显示名称
        
        返回:
            str: 算法的显示名称
        """
        return "动量法 (Momentum)"
    
    def optimize_with_history(self, x0: float, **kwargs) -> Dict[str, np.ndarray]:
        """
        使用动量法进行优化并记录历史
        
        参数:
            x0: 初始点
            **kwargs: 算法参数
                learning_rate: 学习率
                momentum: 动量系数 (0-1之间)
                max_iterations: 最大迭代次数
                tolerance: 收敛容差
            
        返回:
            包含优化历史的字典
        """
        # 从kwargs获取参数
        learning_rate = kwargs.get('learning_rate')
        momentum = kwargs.get('momentum')
        max_iterations = kwargs.get('max_iterations')
        tolerance = kwargs.get('tolerance')
        
        # 获取默认参数
        config = self.config_manager.get_algorithm_config(self.algorithm_name)
        learning_rate = learning_rate or config.get('learning_rate', 0.01)
        momentum = momentum or config.get('momentum', 0.9)
        max_iterations = max_iterations or config.get('max_iterations', 100)
        tolerance = tolerance or config.get('tolerance', 1e-6)
        
        # 初始化
        x = x0
        velocity = 0.0  # 动量项
        x_history = [x]
        y_history = [self.f(x)]
        gradient_history = []
        velocity_history = [velocity]
        
        self.logger.info(f"开始动量法优化: x0={x0}, lr={learning_rate}, momentum={momentum}")
        
        for i in range(max_iterations):
            # 计算梯度
            gradient = self.df(x)
            gradient_history.append(gradient)
            
            # 更新动量项
            velocity = momentum * velocity - learning_rate * gradient
            velocity_history.append(velocity)
            
            # 更新参数
            x = x + velocity
            y = self.f(x)
            
            x_history.append(x)
            y_history.append(y)
            
            # 检查收敛
            if abs(gradient) < tolerance:
                self.logger.info(f"在第{i+1}次迭代收敛，梯度={gradient:.6f}")
                break
                
        # 返回符合基类接口的格式
        return {
            'x_values': np.array(x_history),
            'f_values': np.array(y_history),
            'gradients': np.array(gradient_history),
            'learning_rates': np.full(len(gradient_history), learning_rate),
            'momentum_values': np.array(velocity_history[1:]),  # 排除初始值
            'iterations': len(x_history) - 1,
            'converged': abs(gradient_history[-1]) < tolerance if gradient_history else False
        }
    
    def optimize_with_adaptive_momentum(self,
                                      func: Callable[[float], float],
                                      grad_func: Callable[[float], float],
                                      x0: float,
                                      learning_rate: float = None,
                                      initial_momentum: float = None,
                                      max_iterations: int = None,
                                      tolerance: float = None) -> Tuple[List[float], List[float], Dict[str, Any]]:
        """
        使用自适应动量的动量法优化
        
        参数:
            func: 目标函数
            grad_func: 梯度函数
            x0: 初始点
            learning_rate: 学习率
            initial_momentum: 初始动量系数
            max_iterations: 最大迭代次数
            tolerance: 收敛容差
            
        返回:
            x_history: x值历史
            y_history: 函数值历史
            info: 优化信息
        """
        # 获取默认参数
        config = self.config_manager.get_algorithm_config(self.algorithm_name)
        learning_rate = learning_rate or config.get('learning_rate', 0.01)
        initial_momentum = initial_momentum or config.get('momentum', 0.9)
        max_iterations = max_iterations or config.get('max_iterations', 100)
        tolerance = tolerance or config.get('tolerance', 1e-6)
        
        # 初始化
        x = x0
        velocity = 0.0
        momentum = initial_momentum
        x_history = [x]
        y_history = [func(x)]
        gradient_history = []
        momentum_history = [momentum]
        
        self.logger.info(f"开始自适应动量法优化: x0={x0}, lr={learning_rate}")
        
        for i in range(max_iterations):
            # 计算梯度
            gradient = grad_func(x)
            gradient_history.append(gradient)
            
            # 自适应调整动量系数
            if i > 0:
                # 如果梯度方向改变，减小动量
                if gradient_history[-1] * gradient_history[-2] < 0:
                    momentum = max(0.1, momentum * 0.8)
                else:
                    # 如果梯度方向一致，增加动量
                    momentum = min(0.99, momentum * 1.05)
            
            momentum_history.append(momentum)
            
            # 更新动量项
            velocity = momentum * velocity - learning_rate * gradient
            
            # 更新参数
            x = x + velocity
            y = func(x)
            
            x_history.append(x)
            y_history.append(y)
            
            # 检查收敛
            if abs(gradient) < tolerance:
                self.logger.info(f"在第{i+1}次迭代收敛，梯度={gradient:.6f}")
                break
                
        # 优化信息
        info = {
            'iterations': len(x_history) - 1,
            'final_x': x_history[-1],
            'final_y': y_history[-1],
            'final_gradient': gradient_history[-1] if gradient_history else 0,
            'converged': abs(gradient_history[-1]) < tolerance if gradient_history else False,
            'learning_rate': learning_rate,
            'initial_momentum': initial_momentum,
            'final_momentum': momentum,
            'gradient_history': gradient_history,
            'momentum_history': momentum_history
        }
        
        return x_history, y_history, info
    
    def compare_momentum_values(self,
                              func_name: str = 'quadratic',
                              x0: float = -5.0,
                              momentum_values: List[float] = None,
                              learning_rate: float = None,
                              max_iterations: int = None) -> Dict[str, Any]:
        """
        比较不同动量系数的优化效果
        
        参数:
            func_name: 测试函数名称
            x0: 初始点
            momentum_values: 动量系数列表
            learning_rate: 学习率
            max_iterations: 最大迭代次数
            
        返回:
            比较结果字典
        """
        if momentum_values is None:
            momentum_values = [0.0, 0.5, 0.9, 0.95, 0.99]
            
        # 获取测试函数
        func, grad_func = TestFunctions.get_function_by_name(func_name)
        
        results = {}
        
        for momentum in momentum_values:
            x_hist, y_hist, info = self.optimize_with_history(
                func, grad_func, x0, 
                learning_rate=learning_rate,
                momentum=momentum,
                max_iterations=max_iterations
            )
            
            results[f'momentum_{momentum}'] = {
                'x_history': x_hist,
                'y_history': y_hist,
                'info': info,
                'momentum': momentum
            }
            
        return results
    
    def visualize_optimization(self,
                             func_name: str = 'quadratic',
                             x0: float = -5.0,
                             learning_rate: float = None,
                             momentum: float = None,
                             x_range: List[float] = None,
                             save_gif: bool = True,
                             save_data: bool = True) -> Dict[str, Any]:
        """
        可视化动量法优化过程
        
        参数:
            func_name: 测试函数名称
            x0: 初始点
            learning_rate: 学习率
            momentum: 动量系数
            x_range: x轴范围
            save_gif: 是否保存GIF
            save_data: 是否保存数据
            
        返回:
            可视化结果
        """
        # 获取测试函数
        func, grad_func = TestFunctions.get_function_by_name(func_name)
        
        # 临时设置函数（如果需要的话）
        original_f, original_df = self.f, self.df
        self.f, self.df = func, grad_func
        
        # 可视化
        anim, history = self.create_animation(
            x0=x0,
            function_name=func_name,
            save_gif=save_gif,
            save_data=save_data,
            learning_rate=learning_rate,
            momentum=momentum
        )
        
        # 构建返回结果
        result = {
            'animation': anim,
            'history': history,
            'info': {
                'final_x': history['x_values'][-1],
                'final_y': history['f_values'][-1],
                'iterations': len(history['x_values']) - 1,
                'converged': abs(history['gradients'][-1]) < self.config_manager.get('algorithms.momentum.tolerance', 1e-6)
            }
        }
        
        # 恢复原始函数
        self.f, self.df = original_f, original_df
            
        return result
    
    def compare_with_gradient_descent(self,
                                    func_name: str = 'quadratic',
                                    x0: float = -5.0,
                                    learning_rate: float = None,
                                    momentum: float = None) -> Dict[str, Any]:
        """
        与标准梯度下降比较
        
        参数:
            func_name: 测试函数名称
            x0: 初始点
            learning_rate: 学习率
            momentum: 动量系数
            
        返回:
            比较结果
        """
        # 获取测试函数
        func, grad_func = TestFunctions.get_function_by_name(func_name)
        
        # 动量法优化
        x_hist_momentum, y_hist_momentum, info_momentum = self.optimize_with_history(
            func, grad_func, x0, learning_rate, momentum
        )
        
        # 标准梯度下降（动量=0）
        x_hist_gd, y_hist_gd, info_gd = self.optimize_with_history(
            func, grad_func, x0, learning_rate, momentum=0.0
        )
        
        # 创建比较图
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
        
        # 绘制函数曲线
        x_range = self.config_manager.get_algorithm_config(self.algorithm_name).get('x_range', [-10, 10])
        x_plot = np.linspace(x_range[0], x_range[1], 1000)
        y_plot = [func(x) for x in x_plot]
        
        # 左图：优化路径
        ax1.plot(x_plot, y_plot, 'b-', alpha=0.7, label='函数曲线')
        ax1.plot(x_hist_gd, y_hist_gd, 'ro-', alpha=0.7, label='标准梯度下降', markersize=4)
        ax1.plot(x_hist_momentum, y_hist_momentum, 'go-', alpha=0.7, label=f'动量法 (β={momentum})', markersize=4)
        ax1.set_xlabel('x')
        ax1.set_ylabel('f(x)')
        ax1.set_title('优化路径比较')
        ax1.legend()
        ax1.grid(True, alpha=0.3)
        
        # 右图：收敛曲线
        ax2.plot(range(len(y_hist_gd)), y_hist_gd, 'r-', label='标准梯度下降')
        ax2.plot(range(len(y_hist_momentum)), y_hist_momentum, 'g-', label=f'动量法 (β={momentum})')
        ax2.set_xlabel('迭代次数')
        ax2.set_ylabel('函数值')
        ax2.set_title('收敛曲线比较')
        ax2.legend()
        ax2.grid(True, alpha=0.3)
        ax2.set_yscale('log')
        
        plt.tight_layout()
        
        # 保存图片
        output_path = self.config_manager.get_output_path(self.algorithm_name)
        filename = f"momentum_vs_gd_{func_name}.png"
        filepath = output_path / filename
        plt.savefig(filepath, dpi=300, bbox_inches='tight')
        plt.close()
        
        return {
            'momentum_result': {
                'x_history': x_hist_momentum,
                'y_history': y_hist_momentum,
                'info': info_momentum
            },
            'gradient_descent_result': {
                'x_history': x_hist_gd,
                'y_history': y_hist_gd,
                'info': info_gd
            },
            'comparison_plot': str(filepath)
        }