"""
自适应学习率梯度下降算法
"""

import numpy as np
from typing import Dict, Any, Callable, Optional

from algorithms.base_algorithm import OptimizationAlgorithm
from config import get_config
from algorithms import register_algorithm

@register_algorithm('adaptive_gradient_descent')
class AdaptiveGradientDescent(OptimizationAlgorithm):
    """
    自适应学习率梯度下降算法
    """
    def __init__(self, initial_learning_rate: Optional[float] = None, 
                 max_iterations: Optional[int] = None, 
                 tolerance: Optional[float] = None,
                 decay_factor: float = 0.9,
                 patience: int = 5):
        super().__init__()
        config = get_config().get_algorithm_config('gradient_descent')
        self.initial_learning_rate = initial_learning_rate or config.get('learning_rate', 0.1)
        self.max_iterations = max_iterations or config.get('max_iterations', 100)
        self.tolerance = tolerance or config.get('tolerance', 1e-6)
        self.decay_factor = decay_factor
        self.patience = patience

    def optimize(self, x0: float, f: Callable, df: Callable, d2f: Callable = None, **kwargs) -> Dict[str, Any]:
        learning_rate = kwargs.get('initial_learning_rate', self.initial_learning_rate)
        max_iterations = kwargs.get('max_iterations', self.max_iterations)
        tolerance = kwargs.get('tolerance', self.tolerance)
        decay_factor = kwargs.get('decay_factor', self.decay_factor)
        patience = kwargs.get('patience', self.patience)

        x_values = [x0]
        f_values = [f(x0)]
        gradients = [df(x0)]
        learning_rates = [learning_rate]
        
        x_current = x0
        best_f_value = f(x0)
        no_improvement_count = 0
        
        for i in range(max_iterations):
            gradient = df(x_current)
            
            if abs(gradient) < tolerance:
                break
            
            x_new = x_current - learning_rate * gradient
            f_new = f(x_new)
            
            if f_new < best_f_value:
                best_f_value = f_new
                no_improvement_count = 0
            else:
                no_improvement_count += 1
            
            if no_improvement_count >= patience:
                learning_rate *= decay_factor
                no_improvement_count = 0

            x_values.append(x_new)
            f_values.append(f_new)
            gradients.append(gradient)
            learning_rates.append(learning_rate)
            
            x_current = x_new
            
        return {
            'x_values': np.array(x_values),
            'f_values': np.array(f_values),
            'gradients': np.array(gradients),
            'learning_rates': np.array(learning_rates),
            'iterations': len(x_values) - 1,
            'converged': abs(gradients[-1]) < tolerance
        }
