"""
Nesterov加速梯度法可视化器
基于基础可视化框架实现的Nesterov算法
"""

import numpy as np
from typing import Dict, Callable, Optional, Tuple
import sys
import os

# 添加项目根目录到路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from utils.base_visualizer import BaseOptimizationVisualizer
from config import get_config

class NesterovVisualizer(BaseOptimizationVisualizer):
    """
    Nesterov加速梯度法可视化器
    
    实现Nesterov加速梯度法，包括可视化和动画功能
    Nesterov方法通过在动量方向上预测位置来计算梯度，提供更好的收敛性
    """
    
    def __init__(self, f: Callable, df: Callable, 
                 x_range: Optional[Tuple[float, float]] = None,
                 figsize: Optional[Tuple[int, int]] = None):
        """
        初始化Nesterov可视化器
        
        参数:
            f: 目标函数
            df: 目标函数的导数
            x_range: x轴显示范围
            figsize: 图形大小
        """
        super().__init__('nesterov', f, df, x_range, figsize)
        
        # 获取Nesterov特定配置
        self.nesterov_config = self.config.get_algorithm_config('nesterov')
    
    def _get_algorithm_display_name(self) -> str:
        """获取算法显示名称（中文）"""
        return "Nesterov加速梯度法"
    
    def optimize_with_history(self, x0: float, learning_rate: Optional[float] = None,
                            momentum: Optional[float] = None,
                            max_iterations: Optional[int] = None,
                            tolerance: Optional[float] = None,
                            **kwargs) -> Dict[str, np.ndarray]:
        """
        执行Nesterov优化并记录历史
        
        参数:
            x0: 初始点
            learning_rate: 学习率
            momentum: 动量参数（默认0.9）
            max_iterations: 最大迭代次数
            tolerance: 收敛容忍度
            
        返回:
            包含优化历史的字典
        """
        # 使用配置文件中的默认值
        if learning_rate is None:
            learning_rate = self.nesterov_config.get('learning_rate', 0.01)
        if momentum is None:
            momentum = self.nesterov_config.get('momentum', 0.9)
        if max_iterations is None:
            max_iterations = self.nesterov_config.get('max_iterations', 100)
        if tolerance is None:
            tolerance = self.nesterov_config.get('tolerance', 1e-6)
        
        # 初始化
        x = x0
        v = 0.0  # 速度（动量）
        
        # 记录历史
        x_values = [x]
        f_values = [self.f(x)]
        gradients = [self.df(x)]
        velocities = [v]
        lookahead_points = [x]  # 前瞻点
        lookahead_gradients = [self.df(x)]
        
        converged = False
        
        for i in range(max_iterations):
            # 计算前瞻点（在动量方向上的预测位置）
            x_lookahead = x + momentum * v
            
            # 在前瞻点计算梯度
            grad_lookahead = self.df(x_lookahead)
            
            # 更新速度
            v = momentum * v - learning_rate * grad_lookahead
            
            # 更新参数
            x_new = x + v
            
            # 记录历史
            x_values.append(x_new)
            f_values.append(self.f(x_new))
            gradients.append(self.df(x))  # 当前点的梯度
            velocities.append(v)
            lookahead_points.append(x_lookahead)
            lookahead_gradients.append(grad_lookahead)
            
            # 检查收敛（使用前瞻点的梯度）
            if abs(grad_lookahead) < tolerance:
                converged = True
                print(f"在第 {i+1} 次迭代时收敛 (前瞻梯度: {abs(grad_lookahead):.6f})")
                break
            
            x = x_new
        
        if not converged:
            print(f"在 {max_iterations} 次迭代后未收敛 (最终前瞻梯度: {abs(lookahead_gradients[-1]):.6f})")
        
        return {
            'x_values': np.array(x_values),
            'f_values': np.array(f_values),
            'gradients': np.array(gradients),
            'velocities': np.array(velocities),
            'lookahead_points': np.array(lookahead_points),
            'lookahead_gradients': np.array(lookahead_gradients),
            'iterations': len(x_values) - 1,
            'converged': converged
        }
    
    def _get_additional_info(self, frame: int, history: Dict[str, np.ndarray]) -> str:
        """获取Nesterov特定的额外信息"""
        if frame < len(history['velocities']):
            v = history['velocities'][frame]
            lookahead_x = history['lookahead_points'][frame] if frame < len(history['lookahead_points']) else 0
            lookahead_grad = history['lookahead_gradients'][frame] if frame < len(history['lookahead_gradients']) else 0
            return f"速度 = {v:.6f}, 前瞻点 = {lookahead_x:.6f}, 前瞻梯度 = {lookahead_grad:.6f}"
        return ""
    
    def _get_additional_statistics(self, history: Dict[str, np.ndarray]) -> str:
        """获取Nesterov特定的统计信息"""
        if len(history['velocities']) > 0:
            avg_velocity = np.mean(np.abs(history['velocities']))
            max_velocity = np.max(np.abs(history['velocities']))
            
            avg_lookahead_grad = np.mean(np.abs(history['lookahead_gradients']))
            max_lookahead_grad = np.max(np.abs(history['lookahead_gradients']))
            
            return (f"  平均速度幅度: {avg_velocity:.6f}\n"
                   f"  最大速度幅度: {max_velocity:.6f}\n"
                   f"  平均前瞻梯度幅度: {avg_lookahead_grad:.6f}\n"
                   f"  最大前瞻梯度幅度: {max_lookahead_grad:.6f}")
        return ""