"""
梯度下降算法的可视化封装
"""

from utils.base_visualizer import BaseOptimizationVisualizer
from algorithms.gradient_descent.gradient_descent import GradientDescent
from algorithms.gradient_descent.adaptive_gradient_descent import AdaptiveGradientDescent
from algorithms.gradient_descent.momentum_gradient_descent import MomentumGradientDescent

class GradientDescentVisualizer(BaseOptimizationVisualizer):
    def __init__(self, x_range=None, figsize=None):
        super().__init__(GradientDescent(), x_range, figsize)

class AdaptiveGradientDescentVisualizer(BaseOptimizationVisualizer):
    def __init__(self, x_range=None, figsize=None):
        super().__init__(AdaptiveGradientDescent(), x_range, figsize)

class MomentumGradientDescentVisualizer(BaseOptimizationVisualizer):
    def __init__(self, x_range=None, figsize=None):
        super().__init__(MomentumGradientDescent(), x_range, figsize)
