"""
Adam 优化算法
"""

import numpy as np
from typing import Dict, Any, Callable, Optional

from algorithms.base_algorithm import OptimizationAlgorithm
from config import get_config
from algorithms import register_algorithm

@register_algorithm('adam')
class Adam(OptimizationAlgorithm):
    """
    Adam 优化算法
    """
    def __init__(self, learning_rate: Optional[float] = None, 
                 max_iterations: Optional[int] = None, 
                 tolerance: Optional[float] = None,
                 beta1: float = 0.9,
                 beta2: float = 0.999,
                 epsilon: float = 1e-8):
        super().__init__()
        config = get_config().get_algorithm_config('adam')
        self.learning_rate = learning_rate or config.get('learning_rate', 0.001)
        self.max_iterations = max_iterations or config.get('max_iterations', 100)
        self.tolerance = tolerance or config.get('tolerance', 1e-6)
        self.beta1 = beta1
        self.beta2 = beta2
        self.epsilon = epsilon

    def optimize(self, x0: float, f: Callable, df: Callable, d2f: Callable = None, **kwargs) -> Dict[str, Any]:
        learning_rate = kwargs.get('learning_rate', self.learning_rate)
        max_iterations = kwargs.get('max_iterations', self.max_iterations)
        tolerance = kwargs.get('tolerance', self.tolerance)
        beta1 = kwargs.get('beta1', self.beta1)
        beta2 = kwargs.get('beta2', self.beta2)
        epsilon = kwargs.get('epsilon', self.epsilon)

        x_values = [x0]
        f_values = [f(x0)]
        gradients = [df(x0)]
        
        x_current = x0
        m = 0
        v = 0
        
        for t in range(1, max_iterations + 1):
            gradient = df(x_current)
            
            if abs(gradient) < tolerance:
                break
            
            m = beta1 * m + (1 - beta1) * gradient
            v = beta2 * v + (1 - beta2) * (gradient ** 2)
            
            m_hat = m / (1 - beta1 ** t)
            v_hat = v / (1 - beta2 ** t)
            
            x_new = x_current - learning_rate * m_hat / (np.sqrt(v_hat) + epsilon)
            
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
