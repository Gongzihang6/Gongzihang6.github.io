"""
定义优化算法的基础接口
"""

from abc import ABC, abstractmethod
from typing import Dict, Any, Callable

class OptimizationAlgorithm(ABC):
    """
    优化算法的抽象基类
    """
    def __init__(self, **kwargs):
        self.params = kwargs

    @abstractmethod
    def optimize(self, x0: float, f: Callable, df: Callable, d2f: Callable = None, **kwargs) -> Dict[str, Any]:
        """
        执行优化

        参数:
            x0 (float): 初始点
            f (Callable): 目标函数
            df (Callable): 目标函数的导数
            d2f (Callable, optional): 目标函数的二阶导数. Defaults to None.
            **kwargs: 算法特定的超参数

        返回:
            Dict[str, Any]: 包含优化历史和结果的字典
        """
        pass

    def get_name(self) -> str:
        """
        获取算法的名称
        """
        return self.__class__.__name__
