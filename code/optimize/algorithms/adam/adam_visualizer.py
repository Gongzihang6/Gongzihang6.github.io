"""
Adam算法可视化器
基于基础可视化框架实现的Adam算法
"""

import numpy as np
from typing import Dict, Callable, Optional, Tuple
import sys
import os

# 添加项目根目录到路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from utils.base_visualizer import BaseOptimizationVisualizer
from config import get_config

class AdamVisualizer(BaseOptimizationVisualizer):
    """
    Adam算法可视化器
    
    实现Adam算法，包括可视化和动画功能
    Adam结合了动量法和RMSProp的优点，使用一阶和二阶矩估计
    """
    
    def __init__(self, f: Callable, df: Callable, 
                 x_range: Optional[Tuple[float, float]] = None,
                 figsize: Optional[Tuple[int, int]] = None):
        """
        初始化Adam可视化器
        
        参数:
            f: 目标函数
            df: 目标函数的导数
            x_range: x轴显示范围
            figsize: 图形大小
        """
        super().__init__('adam', f, df, x_range, figsize)
        
        # 获取Adam特定配置
        self.adam_config = self.config.get_algorithm_config('adam')
    
    def _get_algorithm_display_name(self) -> str:
        """获取算法显示名称（中文）"""
        return "Adam"
    
    def optimize_with_history(self, x0: float, learning_rate: Optional[float] = None,
                            beta1: Optional[float] = None,
                            beta2: Optional[float] = None,
                            epsilon: Optional[float] = None,
                            max_iterations: Optional[int] = None,
                            tolerance: Optional[float] = None,
                            **kwargs) -> Dict[str, np.ndarray]:
        """
        执行Adam优化并记录历史
        
        参数:
            x0: 初始点
            learning_rate: 学习率
            beta1: 一阶矩估计的指数衰减率（默认0.9）
            beta2: 二阶矩估计的指数衰减率（默认0.999）
            epsilon: 数值稳定性参数（默认1e-8）
            max_iterations: 最大迭代次数
            tolerance: 收敛容忍度
            
        返回:
            包含优化历史的字典
        """
        # 使用配置文件中的默认值
        if learning_rate is None:
            learning_rate = self.adam_config.get('learning_rate', 0.001)
        if beta1 is None:
            beta1 = self.adam_config.get('beta1', 0.9)
        if beta2 is None:
            beta2 = self.adam_config.get('beta2', 0.999)
        if epsilon is None:
            epsilon = self.adam_config.get('epsilon', 1e-8)
        if max_iterations is None:
            max_iterations = self.adam_config.get('max_iterations', 100)
        if tolerance is None:
            tolerance = self.adam_config.get('tolerance', 1e-6)
        
        # 初始化
        x = x0
        m = 0.0  # 一阶矩估计
        v = 0.0  # 二阶矩估计
        
        # 记录历史
        x_values = [x]
        f_values = [self.f(x)]
        gradients = [self.df(x)]
        m_values = [m]
        v_values = [v]
        m_hat_values = [0.0]
        v_hat_values = [0.0]
        
        converged = False
        
        for t in range(1, max_iterations + 1):
            # 计算梯度
            grad = self.df(x)
            
            # 更新一阶和二阶矩估计
            m = beta1 * m + (1 - beta1) * grad
            v = beta2 * v + (1 - beta2) * grad**2
            
            # 偏差修正
            m_hat = m / (1 - beta1**t)
            v_hat = v / (1 - beta2**t)
            
            # 更新参数
            x_new = x - learning_rate * m_hat / (np.sqrt(v_hat) + epsilon)
            
            # 记录历史
            x_values.append(x_new)
            f_values.append(self.f(x_new))
            gradients.append(grad)
            m_values.append(m)
            v_values.append(v)
            m_hat_values.append(m_hat)
            v_hat_values.append(v_hat)
            
            # 检查收敛
            if abs(grad) < tolerance:
                converged = True
                print(f"在第 {t} 次迭代时收敛 (梯度: {abs(grad):.6f})")
                break
            
            x = x_new
        
        if not converged:
            print(f"在 {max_iterations} 次迭代后未收敛 (最终梯度: {abs(gradients[-1]):.6f})")
        
        return {
            'x_values': np.array(x_values),
            'f_values': np.array(f_values),
            'gradients': np.array(gradients),
            'm_values': np.array(m_values),
            'v_values': np.array(v_values),
            'm_hat_values': np.array(m_hat_values),
            'v_hat_values': np.array(v_hat_values),
            'iterations': len(x_values) - 1,
            'converged': converged
        }
    
    def _get_additional_info(self, frame: int, history: Dict[str, np.ndarray]) -> str:
        """获取Adam特定的额外信息"""
        if frame < len(history['m_values']):
            m = history['m_values'][frame]
            v = history['v_values'][frame]
            m_hat = history['m_hat_values'][frame] if frame < len(history['m_hat_values']) else 0
            v_hat = history['v_hat_values'][frame] if frame < len(history['v_hat_values']) else 0
            return f"m = {m:.6f}, v = {v:.6f}, m̂ = {m_hat:.6f}, v̂ = {v_hat:.6f}"
        return ""
    
    def _get_additional_statistics(self, history: Dict[str, np.ndarray]) -> str:
        """获取Adam特定的统计信息"""
        if len(history['m_values']) > 0:
            avg_m = np.mean(history['m_values'])
            avg_v = np.mean(history['v_values'])
            avg_m_hat = np.mean(history['m_hat_values'])
            avg_v_hat = np.mean(history['v_hat_values'])
            
            return (f"  平均一阶矩估计: {avg_m:.6f}\n"
                   f"  平均二阶矩估计: {avg_v:.6f}\n"
                   f"  平均偏差修正一阶矩: {avg_m_hat:.6f}\n"
                   f"  平均偏差修正二阶矩: {avg_v_hat:.6f}")
        return ""