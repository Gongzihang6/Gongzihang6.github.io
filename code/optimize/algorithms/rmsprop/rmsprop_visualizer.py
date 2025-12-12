"""
RMSProp算法可视化器
基于基础可视化框架实现的RMSProp算法
"""

import numpy as np
from typing import Dict, Callable, Optional, Tuple
import sys
import os

# 添加项目根目录到路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from utils.base_visualizer import BaseOptimizationVisualizer
from config import get_config

class RMSPropVisualizer(BaseOptimizationVisualizer):
    """
    RMSProp算法可视化器
    
    实现RMSProp算法，包括可视化和动画功能
    RMSProp通过维护梯度平方的指数移动平均来自适应调整学习率
    """
    
    def __init__(self, f: Callable, df: Callable, 
                 x_range: Optional[Tuple[float, float]] = None,
                 figsize: Optional[Tuple[int, int]] = None):
        """
        初始化RMSProp可视化器
        
        参数:
            f: 目标函数
            df: 目标函数的导数
            x_range: x轴显示范围
            figsize: 图形大小
        """
        super().__init__('rmsprop', f, df, x_range, figsize)
        
        # 获取RMSProp特定配置
        self.rmsprop_config = self.config.get_algorithm_config('rmsprop')
    
    def _get_algorithm_display_name(self) -> str:
        """获取算法显示名称（中文）"""
        return "RMSProp"
    
    def optimize_with_history(self, x0: float, learning_rate: Optional[float] = None,
                            decay_rate: Optional[float] = None,
                            epsilon: Optional[float] = None,
                            max_iterations: Optional[int] = None,
                            tolerance: Optional[float] = None,
                            **kwargs) -> Dict[str, np.ndarray]:
        """
        执行RMSProp优化并记录历史
        
        参数:
            x0: 初始点
            learning_rate: 学习率
            decay_rate: 衰减率（默认0.9）
            epsilon: 数值稳定性参数（默认1e-8）
            max_iterations: 最大迭代次数
            tolerance: 收敛容忍度
            
        返回:
            包含优化历史的字典
        """
        # 使用配置文件中的默认值
        if learning_rate is None:
            learning_rate = self.rmsprop_config.get('learning_rate', 0.01)
        if decay_rate is None:
            decay_rate = self.rmsprop_config.get('decay_rate', 0.9)
        if epsilon is None:
            epsilon = self.rmsprop_config.get('epsilon', 1e-8)
        if max_iterations is None:
            max_iterations = self.rmsprop_config.get('max_iterations', 1000)
        if tolerance is None:
            tolerance = self.rmsprop_config.get('tolerance', 1e-6)
        
        # 初始化
        x = x0
        v = 0.0  # 梯度平方的指数移动平均
        
        # 记录历史
        x_values = [x]
        f_values = [self.f(x)]
        gradients = [self.df(x)]
        learning_rates = [learning_rate]
        v_values = [v]
        
        converged = False
        
        for i in range(max_iterations):
            # 计算梯度
            grad = self.df(x)
            
            # 更新梯度平方的指数移动平均
            v = decay_rate * v + (1 - decay_rate) * grad**2
            
            # 计算自适应学习率
            adaptive_lr = learning_rate / (np.sqrt(v) + epsilon)
            
            # 更新参数
            x_new = x - adaptive_lr * grad
            
            # 记录历史
            x_values.append(x_new)
            f_values.append(self.f(x_new))
            gradients.append(grad)
            learning_rates.append(adaptive_lr)
            v_values.append(v)
            
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
            'learning_rates': np.array(learning_rates),
            'v_values': np.array(v_values),
            'iterations': len(x_values) - 1,
            'converged': converged
        }
    
    def _get_additional_info(self, frame: int, history: Dict[str, np.ndarray]) -> str:
        """获取RMSProp特定的额外信息"""
        if frame < len(history['v_values']):
            v = history['v_values'][frame]
            lr = history['learning_rates'][frame] if frame < len(history['learning_rates']) else 0
            return f"v = {v:.6f}, 自适应学习率 = {lr:.6f}"
        return ""
    
    def _get_additional_statistics(self, history: Dict[str, np.ndarray]) -> str:
        """获取RMSProp特定的统计信息"""
        if len(history['v_values']) > 0:
            avg_v = np.mean(history['v_values'])
            max_v = np.max(history['v_values'])
            min_v = np.min(history['v_values'])
            
            avg_adaptive_lr = np.mean(history['learning_rates'])
            max_adaptive_lr = np.max(history['learning_rates'])
            min_adaptive_lr = np.min(history['learning_rates'])
            
            return (f"  平均v值: {avg_v:.6f}\n"
                   f"  最大v值: {max_v:.6f}\n"
                   f"  最小v值: {min_v:.6f}\n"
                   f"  平均自适应学习率: {avg_adaptive_lr:.6f}\n"
                   f"  最大自适应学习率: {max_adaptive_lr:.6f}\n"
                   f"  最小自适应学习率: {min_adaptive_lr:.6f}")
        return ""