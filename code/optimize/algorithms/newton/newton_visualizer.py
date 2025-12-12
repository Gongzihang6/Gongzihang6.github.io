"""
牛顿法可视化器
基于基础可视化框架实现的牛顿法
"""

import numpy as np
from typing import Dict, Callable, Optional, Tuple
import sys
import os

# 添加项目根目录到路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from utils.base_visualizer import BaseOptimizationVisualizer
from config import get_config

class NewtonVisualizer(BaseOptimizationVisualizer):
    """
    牛顿法可视化器
    
    实现牛顿法，包括可视化和动画功能
    牛顿法使用二阶导数信息来寻找最优解，收敛速度快但需要计算Hessian矩阵
    """
    
    def __init__(self, f: Callable, df: Callable, 
                 x_range: Optional[Tuple[float, float]] = None,
                 figsize: Optional[Tuple[int, int]] = None,
                 d2f: Optional[Callable] = None):
        """
        初始化牛顿法可视化器
        
        参数:
            f: 目标函数
            df: 目标函数的一阶导数
            x_range: x轴显示范围
            figsize: 图形大小
            d2f: 目标函数的二阶导数（如果未提供，将使用数值微分）
        """
        super().__init__('newton', f, df, x_range, figsize)
        
        # 获取牛顿法特定配置
        self.newton_config = self.config.get_algorithm_config('newton')
        
        # 二阶导数函数
        self.d2f = d2f if d2f is not None else self._numerical_second_derivative
    
    def _numerical_second_derivative(self, x: float, h: float = 1e-5) -> float:
        """
        数值计算二阶导数
        使用中心差分公式: f''(x) ≈ [f'(x+h) - f'(x-h)] / (2h)
        """
        return (self.df(x + h) - self.df(x - h)) / (2 * h)
    
    def _get_algorithm_display_name(self) -> str:
        """获取算法显示名称（中文）"""
        return "牛顿法"
    
    def optimize_with_history(self, x0: float, 
                            max_iterations: Optional[int] = None,
                            tolerance: Optional[float] = None,
                            **kwargs) -> Dict[str, np.ndarray]:
        """
        执行牛顿法优化并记录历史
        
        参数:
            x0: 初始点
            max_iterations: 最大迭代次数
            tolerance: 收敛容忍度
            
        返回:
            包含优化历史的字典
        """
        # 使用配置文件中的默认值
        if max_iterations is None:
            max_iterations = self.newton_config.get('max_iterations', 50)
        if tolerance is None:
            tolerance = self.newton_config.get('tolerance', 1e-6)
        
        # 初始化
        x = x0
        
        # 记录历史
        x_values = [x]
        f_values = [self.f(x)]
        gradients = [self.df(x)]
        hessians = [self.d2f(x)]
        step_sizes = [0.0]
        
        converged = False
        
        for i in range(max_iterations):
            # 计算一阶和二阶导数
            grad = self.df(x)
            hess = self.d2f(x)
            
            # 检查Hessian是否为零或接近零
            if abs(hess) < 1e-12:
                print(f"在第 {i+1} 次迭代时Hessian接近零，无法继续")
                break
            
            # 牛顿步长
            step = -grad / hess
            
            # 更新参数
            x_new = x + step
            
            # 记录历史
            x_values.append(x_new)
            f_values.append(self.f(x_new))
            gradients.append(grad)
            hessians.append(hess)
            step_sizes.append(abs(step))
            
            # 检查收敛
            if abs(grad) < tolerance:
                converged = True
                print(f"在第 {i+1} 次迭代时收敛 (梯度: {abs(grad):.6f})")
                break
            
            # 检查步长是否过小
            if abs(step) < tolerance:
                converged = True
                print(f"在第 {i+1} 次迭代时收敛 (步长: {abs(step):.6f})")
                break
            
            x = x_new
        
        if not converged:
            print(f"在 {max_iterations} 次迭代后未收敛 (最终梯度: {abs(gradients[-1]):.6f})")
        
        return {
            'x_values': np.array(x_values),
            'f_values': np.array(f_values),
            'gradients': np.array(gradients),
            'hessians': np.array(hessians),
            'step_sizes': np.array(step_sizes),
            'iterations': len(x_values) - 1,
            'converged': converged
        }
    
    def _get_additional_info(self, frame: int, history: Dict[str, np.ndarray]) -> str:
        """获取牛顿法特定的额外信息"""
        if frame < len(history['hessians']):
            hess = history['hessians'][frame]
            step_size = history['step_sizes'][frame] if frame < len(history['step_sizes']) else 0
            return f"Hessian = {hess:.6f}, 步长 = {step_size:.6f}"
        return ""
    
    def _get_additional_statistics(self, history: Dict[str, np.ndarray]) -> str:
        """获取牛顿法特定的统计信息"""
        if len(history['hessians']) > 0:
            avg_hessian = np.mean(history['hessians'])
            min_hessian = np.min(history['hessians'])
            max_hessian = np.max(history['hessians'])
            
            avg_step_size = np.mean(history['step_sizes'])
            max_step_size = np.max(history['step_sizes'])
            
            return (f"  平均Hessian: {avg_hessian:.6f}\n"
                   f"  最小Hessian: {min_hessian:.6f}\n"
                   f"  最大Hessian: {max_hessian:.6f}\n"
                   f"  平均步长: {avg_step_size:.6f}\n"
                   f"  最大步长: {max_step_size:.6f}")
        return ""