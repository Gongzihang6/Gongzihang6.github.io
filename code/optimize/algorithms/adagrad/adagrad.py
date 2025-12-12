"""
Adagrad 优化算法
"""

import numpy as np
from typing import Dict, Any, Callable, Optional

from algorithms.base_algorithm import OptimizationAlgorithm
from config import get_config
from algorithms import register_algorithm

@register_algorithm('adagrad')
class Adagrad(OptimizationAlgorithm):
    """
    Adagrad 优化算法
    """
    def __init__(self, learning_rate: Optional[float] = None, 
                 max_iterations: Optional[int] = None, 
                 tolerance: Optional[float] = None,
                 epsilon: float = 1e-8):
        super().__init__()
        config = get_config().get_algorithm_config('adagrad')
        self.learning_rate = learning_rate or config.get('learning_rate', 0.01)
        self.max_iterations = max_iterations or config.get('max_iterations', 100)
        self.tolerance = tolerance or config.get('tolerance', 1e-6)
        self.epsilon = epsilon

    def optimize(self, x0: float, f: Callable, df: Callable, d2f: Callable = None, **kwargs) -> Dict[str, Any]:
        learning_rate = kwargs.get('learning_rate', self.learning_rate)
        max_iterations = kwargs.get('max_iterations', self.max_iterations)
        tolerance = kwargs.get('tolerance', self.tolerance)
        epsilon = kwargs.get('epsilon', self.epsilon)

        x_values = [x0]
        f_values = [f(x0)]
        gradients = [df(x0)]
        
        x_current = x0
        grad_squared = 0
        
        for i in range(max_iterations):
            gradient = df(x_current)
            
            if abs(gradient) < tolerance:
                break
            
            grad_squared += gradient ** 2
            
            adapted_lr = learning_rate / (np.sqrt(grad_squared) + epsilon)
            
            x_new = x_current - adapted_lr * gradient
            
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
