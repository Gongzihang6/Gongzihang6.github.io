"""
配置管理器
负责加载、验证和管理项目配置
"""

import os
import yaml
import json
from pathlib import Path
from typing import Dict, Any, Optional
import logging

class ConfigManager:
    """
    配置管理器类
    
    功能：
    - 加载YAML配置文件
    - 提供配置项访问接口
    - 支持配置验证和默认值
    - 支持运行时配置更新
    """
    
    def __init__(self, config_path: Optional[str] = None):
        """
        初始化配置管理器
        
        参数:
            config_path: 配置文件路径，默认为 config/config.yaml
        """
        if config_path is None:
            # 获取项目根目录
            project_root = Path(__file__).parent.parent
            config_path = project_root / "config" / "config.yaml"
        
        self.config_path = Path(config_path)
        self.config = {}
        self._load_config()
        self._setup_logging()
        
    def _load_config(self):
        """加载配置文件"""
        try:
            if self.config_path.exists():
                with open(self.config_path, 'r', encoding='utf-8') as f:
                    self.config = yaml.safe_load(f)
                print(f"配置文件加载成功: {self.config_path}")
            else:
                print(f"配置文件不存在: {self.config_path}")
                self.config = self._get_default_config()
        except Exception as e:
            print(f"加载配置文件时出错: {e}")
            self.config = self._get_default_config()
    
    def _get_default_config(self) -> Dict[str, Any]:
        """获取默认配置"""
        return {
            'paths': {
                'output_root': 'output',
                'algorithms': {
                    'gradient_descent': 'gradient_descent',
                    'sgd': 'sgd',
                    'adam': 'adam',
                    'momentum': 'momentum'
                }
            },
            'visualization': {
                'figure': {'width': 15, 'height': 6, 'dpi': 100},
                'animation': {'interval': 200, 'fps': 10, 'repeat': True}
            },
            'algorithms': {
                'gradient_descent': {
                    'learning_rate': 0.1,
                    'max_iterations': 100,
                    'tolerance': 1e-6,
                    'x_range': [-10, 10]
                }
            }
        }
    
    def _setup_logging(self):
        """设置日志系统"""
        log_config = self.get('logging', {})
        level = getattr(logging, log_config.get('level', 'INFO'))
        format_str = log_config.get('format', '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        
        logging.basicConfig(level=level, format=format_str)
        self.logger = logging.getLogger(__name__)
    
    def get(self, key_path: str, default: Any = None) -> Any:
        """
        获取配置项
        
        参数:
            key_path: 配置项路径，支持点号分隔的嵌套路径，如 'algorithms.gradient_descent.learning_rate'
            default: 默认值
            
        返回:
            配置项值
        """
        keys = key_path.split('.')
        value = self.config
        
        try:
            for key in keys:
                value = value[key]
            return value
        except (KeyError, TypeError):
            return default
    
    def set(self, key_path: str, value: Any):
        """
        设置配置项
        
        参数:
            key_path: 配置项路径
            value: 配置项值
        """
        keys = key_path.split('.')
        config = self.config
        
        # 导航到最后一级的父级
        for key in keys[:-1]:
            if key not in config:
                config[key] = {}
            config = config[key]
        
        # 设置最后一级的值
        config[keys[-1]] = value
    
    def get_algorithm_config(self, algorithm_name: str) -> Dict[str, Any]:
        """
        获取指定算法的配置
        
        参数:
            algorithm_name: 算法名称
            
        返回:
            算法配置字典
        """
        return self.get(f'algorithms.{algorithm_name}', {})
    
    def get_output_path(self, algorithm_name: str, create_if_not_exists: bool = True) -> Path:
        """
        获取算法输出路径
        
        参数:
            algorithm_name: 算法名称
            create_if_not_exists: 如果目录不存在是否创建
            
        返回:
            输出路径
        """
        project_root = Path(__file__).parent.parent
        output_root = self.get('paths.output_root', 'output')
        algorithm_subdir = self.get(f'paths.algorithms.{algorithm_name}', algorithm_name)
        
        output_path = project_root / output_root / algorithm_subdir
        
        if create_if_not_exists and not output_path.exists():
            output_path.mkdir(parents=True, exist_ok=True)
            self.logger.info(f"创建输出目录: {output_path}")
        
        return output_path
    
    def get_visualization_config(self) -> Dict[str, Any]:
        """获取可视化配置"""
        return self.get('visualization', {})
    
    def get_test_function_config(self, function_name: str) -> Dict[str, Any]:
        """
        获取测试函数配置
        
        参数:
            function_name: 函数名称
            
        返回:
            函数配置字典
        """
        return self.get(f'test_functions.{function_name}', {})
    
    def generate_filename(self, algorithm_name: str, function_name: str, 
                         file_type: str = 'gif', timestamp: str = None) -> str:
        """
        生成输出文件名
        
        参数:
            algorithm_name: 算法名称
            function_name: 函数名称
            file_type: 文件类型 (gif, png, log, data)
            timestamp: 时间戳，如果为None则自动生成
            
        返回:
            文件名
        """
        if timestamp is None:
            from datetime import datetime
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        naming_pattern = self.get(f'output.naming.{file_type}', 
                                f'{algorithm_name}_{function_name}_{timestamp}.{file_type}')
        
        return naming_pattern.format(
            algorithm=algorithm_name,
            function=function_name,
            timestamp=timestamp
        )
    
    def save_config(self, output_path: Optional[str] = None):
        """
        保存当前配置到文件
        
        参数:
            output_path: 输出路径，默认为原配置文件路径
        """
        if output_path is None:
            output_path = self.config_path
        
        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                yaml.dump(self.config, f, default_flow_style=False, 
                         allow_unicode=True, indent=2)
            self.logger.info(f"配置已保存到: {output_path}")
        except Exception as e:
            self.logger.error(f"保存配置文件时出错: {e}")
    
    def validate_config(self) -> bool:
        """
        验证配置文件的完整性
        
        返回:
            验证是否通过
        """
        required_keys = [
            'paths.output_root',
            'visualization.figure.width',
            'visualization.figure.height',
            'algorithms.gradient_descent.learning_rate'
        ]
        
        for key in required_keys:
            if self.get(key) is None:
                self.logger.error(f"缺少必需的配置项: {key}")
                return False
        
        self.logger.info("配置验证通过")
        return True
    
    def get_all_algorithms(self) -> list:
        """获取所有已配置的算法列表"""
        algorithms = self.get('algorithms', {})
        return list(algorithms.keys())
    
    def get_all_test_functions(self) -> list:
        """获取所有已配置的测试函数列表"""
        functions = self.get('test_functions', {})
        return list(functions.keys())

# 全局配置管理器实例
_config_manager = None

def get_config() -> ConfigManager:
    """
    获取全局配置管理器实例
    
    返回:
        ConfigManager实例
    """
    global _config_manager
    if _config_manager is None:
        _config_manager = ConfigManager()
    return _config_manager

def update_config(key_path: str, value: Any):
    """
    更新全局配置
    
    参数:
        key_path: 配置项路径
        value: 配置项值
    """
    config_manager = get_config()
    config_manager.set(key_path, value)