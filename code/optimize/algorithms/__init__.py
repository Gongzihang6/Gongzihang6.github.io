"""
优化算法模块
动态发现和注册所有可用的优化算法
"""

import os
import importlib
from pathlib import Path
from typing import Dict, Type
from .base_algorithm import OptimizationAlgorithm

ALGORITHM_REGISTRY: Dict[str, Type[OptimizationAlgorithm]] = {}

def register_algorithm(name: str):
    def decorator(cls: Type[OptimizationAlgorithm]):
        ALGORITHM_REGISTRY[name] = cls
        return cls
    return decorator

def discover_algorithms():
    """
    自动发现并加载所有算法
    """
    algorithms_dir = Path(__file__).parent
    for module_file in algorithms_dir.glob('**/*.py'):
        if module_file.name == '__init__.py' or module_file.name == 'base_algorithm.py':
            continue
        
        # 构建模块路径
        relative_path = module_file.relative_to(algorithms_dir.parent)
        module_path = ".".join(relative_path.with_suffix('').parts)
        
        try:
            importlib.import_module(module_path)
        except ImportError as e:
            print(f"无法导入模块 {module_path}: {e}")

def get_algorithm(algorithm_name: str) -> Type[OptimizationAlgorithm]:
    """
    根据名称获取算法类
    """
    if not ALGORITHM_REGISTRY:
        discover_algorithms()
    
    algorithm_class = ALGORITHM_REGISTRY.get(algorithm_name)
    if not algorithm_class:
        raise ValueError(f"未知的算法: {algorithm_name}. 可用算法: {list(ALGORITHM_REGISTRY.keys())}")
    
    return algorithm_class

def get_available_algorithms() -> list:
    """
    获取所有可用的算法名称
    """
    if not ALGORITHM_REGISTRY:
        discover_algorithms()
    return list(ALGORITHM_REGISTRY.keys())

# 自动发现算法
discover_algorithms()
