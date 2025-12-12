"""
BFGS 优化算法
"""

import numpy as np
from typing import Dict, Any, Callable, Optional

from algorithms.base_algorithm import OptimizationAlgorithm
from config import get_config
from algorithms import register_algorithm

@register_algorithm('bfgs')
class BFGS(OptimizationAlgorithm):
    """
    BFGS 优化算法
    """
    def __init__(self, max_iterations: Optional[int] = None, 
                 tolerance: Optional[float] = None):
        super().__init__()
        config = get_config().get_algorithm_config('bfgs')
        self.max_iterations = max_iterations or config.get('max_iterations', 50)
        self.tolerance = tolerance or config.get('tolerance', 1e-6)

    def optimize(self, x0: float, f: Callable, df: Callable, d2f: Callable = None, **kwargs) -> Dict[str, Any]:
        max_iterations = kwargs.get('max_iterations', self.max_iterations)
        tolerance = kwargs.get('tolerance', self.tolerance)

        x_values = [x0]
        f_values = [f(x0)]
        gradients = [df(x0)]
        
        x_current = x0
        # Initialize inverse Hessian approximation
        B_inv = 1.0
        
        for i in range(max_iterations):
            gradient = df(x_current)
            
            if abs(gradient) < tolerance:
                break
            
            # Search direction
            p = -B_inv * gradient
            
            # Line search (simple backtracking)
            alpha = 1.0
            c = 0.5
            rho = 0.5
            while f(x_current + alpha * p) > f(x_current) + c * alpha * gradient * p:
                alpha *= rho
            
            x_new = x_current + alpha * p
            
            s = x_new - x_current
            y = df(x_new) - gradient
            
            # Update inverse Hessian approximation
            rho = 1.0 / (y * s)
            B_inv = (1 - rho * s * y) * B_inv * (1 - rho * y * s) + rho * s * s

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
