"""
标准梯度下降算法
"""

import numpy as np
from typing import Dict, Any, Callable, Optional

from algorithms.base_algorithm import OptimizationAlgorithm
from config import get_config
from algorithms import register_algorithm

@register_algorithm('gradient_descent')
class GradientDescent(OptimizationAlgorithm):
    """
    标准梯度下降算法
    """
    def __init__(self, learning_rate: Optional[float] = None, 
                 max_iterations: Optional[int] = None, 
                 tolerance: Optional[float] = None):
        super().__init__()
        config = get_config().get_algorithm_config('gradient_descent')
        self.learning_rate = learning_rate or config.get('learning_rate', 0.1)
        self.max_iterations = max_iterations or config.get('max_iterations', 100)
        self.tolerance = tolerance or config.get('tolerance', 1e-6)

    def optimize(self, x0: float, f: Callable, df: Callable, d2f: Callable = None, **kwargs) -> Dict[str, Any]:
        # 覆盖参数
        learning_rate = kwargs.get('learning_rate', self.learning_rate)
        max_iterations = kwargs.get('max_iterations', self.max_iterations)
        tolerance = kwargs.get('tolerance', self.tolerance)

        x_values = [x0]
        f_values = [f(x0)]
        gradients = [df(x0)]
        
        x_current = x0
        
        for i in range(max_iterations):
            gradient = df(x_current)
            
            if abs(gradient) < tolerance:
                break
            
            x_new = x_current - learning_rate * gradient
            
            x_values.append(x_new)
            f_values.append(f(x_new))
            gradients.append(gradient)
            
            x_current = x_new
            
        return {
            'x_values': np.array(x_values),
            'f_values': np.array(f_values),
            'gradients': np.array(gradients),
            'iterations': len(x_values) - 1,
            'converged': abs(gradients[-1]) < tolerance
        }
