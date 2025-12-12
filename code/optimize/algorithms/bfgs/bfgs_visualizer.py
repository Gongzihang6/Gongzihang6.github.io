"""
BFGS拟牛顿法可视化器
基于基础可视化框架实现的BFGS算法
"""

import numpy as np
from typing import Dict, Callable, Optional, Tuple
import sys
import os

# 添加项目根目录到路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from utils.base_visualizer import BaseOptimizationVisualizer
from config import get_config

class BFGSVisualizer(BaseOptimizationVisualizer):
    """
    BFGS拟牛顿法可视化器
    
    实现BFGS算法，包括可视化和动画功能
    BFGS通过逐步构建Hessian矩阵的近似来避免直接计算二阶导数
    """
    
    def __init__(self, f: Callable, df: Callable, 
                 x_range: Optional[Tuple[float, float]] = None,
                 figsize: Optional[Tuple[int, int]] = None):
        """
        初始化BFGS可视化器
        
        参数:
            f: 目标函数
            df: 目标函数的导数
            x_range: x轴显示范围
            figsize: 图形大小
        """
        super().__init__('bfgs', f, df, x_range, figsize)
        
        # 获取BFGS特定配置
        self.bfgs_config = self.config.get_algorithm_config('bfgs')
    
    def _get_algorithm_display_name(self) -> str:
        """获取算法显示名称（中文）"""
        return "BFGS拟牛顿法"
    
    def _line_search(self, x: float, direction: float, grad: float, 
                    c1: float = 1e-4, max_iter: int = 20) -> float:
        """
        简单的回溯线搜索
        
        参数:
            x: 当前点
            direction: 搜索方向
            grad: 当前梯度
            c1: Armijo条件参数
            max_iter: 最大迭代次数
            
        返回:
            步长
        """
        alpha = 1.0
        f_x = self.f(x)
        
        for _ in range(max_iter):
            x_new = x + alpha * direction
            f_new = self.f(x_new)
            
            # Armijo条件
            if f_new <= f_x + c1 * alpha * grad * direction:
                return alpha
            
            alpha *= 0.5
        
        return alpha
    
    def optimize_with_history(self, x0: float, learning_rate: Optional[float] = None,
                            max_iterations: Optional[int] = None,
                            tolerance: Optional[float] = None,
                            **kwargs) -> Dict[str, np.ndarray]:
        """
        执行BFGS优化并记录历史
        
        参数:
            x0: 初始点
            learning_rate: 初始学习率（用于线搜索）
            max_iterations: 最大迭代次数
            tolerance: 收敛容忍度
            
        返回:
            包含优化历史的字典
        """
        # 使用配置文件中的默认值
        if learning_rate is None:
            learning_rate = self.bfgs_config.get('learning_rate', 1.0)
        if max_iterations is None:
            max_iterations = self.bfgs_config.get('max_iterations', 100)
        if tolerance is None:
            tolerance = self.bfgs_config.get('tolerance', 1e-6)
        
        # 初始化
        x = x0
        H = 1.0  # 初始Hessian逆矩阵近似（标量情况下）
        
        # 记录历史
        x_values = [x]
        f_values = [self.f(x)]
        gradients = [self.df(x)]
        H_values = [H]
        step_sizes = [0.0]
        directions = [0.0]
        
        converged = False
        
        for i in range(max_iterations):
            # 计算梯度
            grad = self.df(x)
            
            # 检查收敛
            if abs(grad) < tolerance:
                converged = True
                print(f"在第 {i+1} 次迭代时收敛 (梯度: {abs(grad):.6f})")
                break
            
            # 计算搜索方向
            direction = -H * grad
            
            # 线搜索确定步长
            alpha = self._line_search(x, direction, grad)
            
            # 更新参数
            s = alpha * direction  # 位置变化
            x_new = x + s
            
            # 计算新梯度
            grad_new = self.df(x_new)
            y = grad_new - grad  # 梯度变化
            
            # 记录历史
            x_values.append(x_new)
            f_values.append(self.f(x_new))
            gradients.append(grad)
            H_values.append(H)
            step_sizes.append(alpha)
            directions.append(direction)
            
            # BFGS更新Hessian逆矩阵近似
            if abs(y * s) > 1e-12:  # 避免除零
                rho = 1.0 / (y * s)
                H = (1 - rho * s * y) * H * (1 - rho * y * s) + rho * s * s
            
            x = x_new
        
        if not converged:
            print(f"在 {max_iterations} 次迭代后未收敛 (最终梯度: {abs(gradients[-1]):.6f})")
        
        return {
            'x_values': np.array(x_values),
            'f_values': np.array(f_values),
            'gradients': np.array(gradients),
            'H_values': np.array(H_values),
            'step_sizes': np.array(step_sizes),
            'directions': np.array(directions),
            'iterations': len(x_values) - 1,
            'converged': converged
        }
    
    def _get_additional_info(self, frame: int, history: Dict[str, np.ndarray]) -> str:
        """获取BFGS特定的额外信息"""
        if frame < len(history['H_values']):
            H = history['H_values'][frame]
            step_size = history['step_sizes'][frame] if frame < len(history['step_sizes']) else 0
            direction = history['directions'][frame] if frame < len(history['directions']) else 0
            return f"H⁻¹ = {H:.6f}, 方向 = {direction:.6f}, 步长 = {step_size:.6f}"
        return ""
    
    def _get_additional_statistics(self, history: Dict[str, np.ndarray]) -> str:
        """获取BFGS特定的统计信息"""
        if len(history['H_values']) > 0:
            avg_H = np.mean(history['H_values'])
            min_H = np.min(history['H_values'])
            max_H = np.max(history['H_values'])
            
            avg_step_size = np.mean(history['step_sizes'])
            max_step_size = np.max(history['step_sizes'])
            
            return (f"  平均Hessian逆近似: {avg_H:.6f}\n"
                   f"  最小Hessian逆近似: {min_H:.6f}\n"
                   f"  最大Hessian逆近似: {max_H:.6f}\n"
                   f"  平均步长: {avg_step_size:.6f}\n"
                   f"  最大步长: {max_step_size:.6f}")
        return ""