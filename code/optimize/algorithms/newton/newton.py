"""
牛顿法优化算法
"""

import numpy as np
from typing import Dict, Any, Callable, Optional

from algorithms.base_algorithm import OptimizationAlgorithm
from config import get_config
from algorithms import register_algorithm

@register_algorithm('newton')
class Newton(OptimizationAlgorithm):
    """
    牛顿法优化算法
    """
    def __init__(self, max_iterations: Optional[int] = None, 
                 tolerance: Optional[float] = None,
                 epsilon: float = 1e-8):
        super().__init__()
        config = get_config().get_algorithm_config('newton')
        self.max_iterations = max_iterations or config.get('max_iterations', 50)
        self.tolerance = tolerance or config.get('tolerance', 1e-6)
        self.epsilon = epsilon

    def optimize(self, x0: float, f: Callable, df: Callable, d2f: Callable = None, **kwargs) -> Dict[str, Any]:
        if d2f is None:
            raise ValueError("牛顿法需要二阶导数 (d2f).")

        max_iterations = kwargs.get('max_iterations', self.max_iterations)
        tolerance = kwargs.get('tolerance', self.tolerance)
        epsilon = kwargs.get('epsilon', self.epsilon)

        x_values = [x0]
        f_values = [f(x0)]
        gradients = [df(x0)]
        
        x_current = x0
        
        for i in range(max_iterations):
            gradient = df(x_current)
            hessian = d2f(x_current)
            
            if abs(gradient) < tolerance:
                break
            
            if abs(hessian) < epsilon:
                # 如果二阶导数接近于零，则退化为梯度下降
                x_new = x_current - 0.01 * gradient
            else:
                x_new = x_current - gradient / hessian
            
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
