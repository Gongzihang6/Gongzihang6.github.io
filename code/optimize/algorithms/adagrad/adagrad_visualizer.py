"""
Adagrad算法可视化器
基于基础可视化框架实现的Adagrad算法
"""

import numpy as np
from typing import Dict, Callable, Optional, Tuple
import sys
import os

# 添加项目根目录到路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from utils.base_visualizer import BaseOptimizationVisualizer
from config import get_config

class AdagradVisualizer(BaseOptimizationVisualizer):
    """
    Adagrad算法可视化器
    
    实现Adagrad算法，包括可视化和动画功能
    Adagrad通过累积历史梯度的平方来自适应调整学习率
    """
    
    def __init__(self, f: Callable, df: Callable, 
                 x_range: Optional[Tuple[float, float]] = None,
                 figsize: Optional[Tuple[int, int]] = None):
        """
        初始化Adagrad可视化器
        
        参数:
            f: 目标函数
            df: 目标函数的导数
            x_range: x轴显示范围
            figsize: 图形大小
        """
        super().__init__('adagrad', f, df, x_range, figsize)
        
        # 获取Adagrad特定配置
        self.adagrad_config = self.config.get_algorithm_config('adagrad')
    
    def _get_algorithm_display_name(self) -> str:
        """获取算法显示名称（中文）"""
        return "Adagrad"
    
    def optimize_with_history(self, x0: float, learning_rate: Optional[float] = None,
                            epsilon: Optional[float] = None,
                            max_iterations: Optional[int] = None,
                            tolerance: Optional[float] = None,
                            **kwargs) -> Dict[str, np.ndarray]:
        """
        执行Adagrad优化并记录历史
        
        参数:
            x0: 初始点
            learning_rate: 学习率
            epsilon: 数值稳定性参数（默认1e-8）
            max_iterations: 最大迭代次数
            tolerance: 收敛容忍度
            
        返回:
            包含优化历史的字典
        """
        # 使用配置文件中的默认值
        if learning_rate is None:
            learning_rate = self.adagrad_config.get('learning_rate', 0.1)
        if epsilon is None:
            epsilon = self.adagrad_config.get('epsilon', 1e-8)
        if max_iterations is None:
            max_iterations = self.adagrad_config.get('max_iterations', 100)
        if tolerance is None:
            tolerance = self.adagrad_config.get('tolerance', 1e-6)
        
        # 初始化
        x = x0
        G = 0.0  # 累积梯度平方和
        
        # 记录历史
        x_values = [x]
        f_values = [self.f(x)]
        gradients = [self.df(x)]
        G_values = [G]
        adaptive_lr_values = [learning_rate]
        
        converged = False
        
        for i in range(max_iterations):
            # 计算梯度
            grad = self.df(x)
            
            # 累积梯度平方
            G += grad**2
            
            # 计算自适应学习率
            adaptive_lr = learning_rate / (np.sqrt(G) + epsilon)
            
            # 更新参数
            x_new = x - adaptive_lr * grad
            
            # 记录历史
            x_values.append(x_new)
            f_values.append(self.f(x_new))
            gradients.append(grad)
            G_values.append(G)
            adaptive_lr_values.append(adaptive_lr)
            
            # 检查收敛
            if abs(grad) < tolerance:
                converged = True
                print(f"在第 {i+1} 次迭代时收敛 (梯度: {abs(grad):.6f})")
                break
            
            x = x_new
        
        if not converged:
            print(f"在 {max_iterations} 次迭代后未收敛 (最终梯度: {abs(gradients[-1]):.6f})")
        
        return {
            'x_values': np.array(x_values),
            'f_values': np.array(f_values),
            'gradients': np.array(gradients),
            'G_values': np.array(G_values),
            'adaptive_lr_values': np.array(adaptive_lr_values),
            'iterations': len(x_values) - 1,
            'converged': converged
        }
    
    def _get_additional_info(self, frame: int, history: Dict[str, np.ndarray]) -> str:
        """获取Adagrad特定的额外信息"""
        if frame < len(history['G_values']):
            G = history['G_values'][frame]
            adaptive_lr = history['adaptive_lr_values'][frame] if frame < len(history['adaptive_lr_values']) else 0
            return f"累积梯度平方 = {G:.6f}, 自适应学习率 = {adaptive_lr:.6f}"
        return ""
    
    def _get_additional_statistics(self, history: Dict[str, np.ndarray]) -> str:
        """获取Adagrad特定的统计信息"""
        if len(history['G_values']) > 0:
            final_G = history['G_values'][-1]
            avg_adaptive_lr = np.mean(history['adaptive_lr_values'])
            min_adaptive_lr = np.min(history['adaptive_lr_values'])
            max_adaptive_lr = np.max(history['adaptive_lr_values'])
            
            return (f"  最终累积梯度平方: {final_G:.6f}\n"
                   f"  平均自适应学习率: {avg_adaptive_lr:.6f}\n"
                   f"  最小自适应学习率: {min_adaptive_lr:.6f}\n"
                   f"  最大自适应学习率: {max_adaptive_lr:.6f}")
        return ""