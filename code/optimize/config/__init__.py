"""
配置管理模块
提供项目配置的加载、验证和管理功能
"""

from .config_manager import ConfigManager, get_config, update_config

__all__ = ['ConfigManager', 'get_config', 'update_config']