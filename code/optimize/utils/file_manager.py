"""
文件管理工具
提供统一的文件和目录管理功能
"""

import os
import json
import shutil
from pathlib import Path
from typing import Dict, Any, List, Optional, Union
from datetime import datetime
import logging

from config import get_config

class FileManager:
    """
    文件管理器类
    负责处理所有文件和目录相关的操作
    """
    
    def __init__(self):
        """初始化文件管理器"""
        self.config = get_config()
        self.logger = self._setup_logger()
        
        # 确保所有必要的目录存在
        self._ensure_directories()
    
    def _setup_logger(self) -> logging.Logger:
        """
        设置日志记录器
        
        返回:
            配置好的日志记录器
        """
        logger = logging.getLogger('FileManager')
        
        # 如果已经配置过，直接返回
        if logger.handlers:
            return logger
        
        log_config = self.config.get('logging', {})
        log_level = getattr(logging, log_config.get('level', 'INFO').upper())
        logger.setLevel(log_level)
        
        # 创建日志目录
        log_dir = Path(self.config.get('paths.logs', 'logs'))
        log_dir.mkdir(parents=True, exist_ok=True)
        
        # 文件处理器
        if log_config.get('file_enabled', True):
            log_file = log_dir / f"file_manager_{datetime.now().strftime('%Y%m%d')}.log"
            file_handler = logging.FileHandler(log_file, encoding='utf-8')
            file_handler.setLevel(log_level)
            
            # 格式化器
            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                datefmt='%Y-%m-%d %H:%M:%S'
            )
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)
        
        # 控制台处理器
        if log_config.get('console_enabled', False):
            console_handler = logging.StreamHandler()
            console_handler.setLevel(log_level)
            console_handler.setFormatter(formatter)
            logger.addHandler(console_handler)
        
        return logger
    
    def _ensure_directories(self):
        """确保所有必要的目录存在"""
        try:
            # 主要目录
            main_dirs = [
                self.config.get('paths.output', 'output'),
                self.config.get('paths.temp', 'temp'),
                self.config.get('paths.logs', 'logs')
            ]
            
            for dir_path in main_dirs:
                Path(dir_path).mkdir(parents=True, exist_ok=True)
            
            # 算法特定的输出目录
            algorithms = self.config.get('algorithms', {}).keys()
            output_base = Path(self.config.get('paths.output', 'output'))
            
            for algorithm in algorithms:
                algorithm_dir = output_base / algorithm
                algorithm_dir.mkdir(parents=True, exist_ok=True)
            
            self.logger.info("所有必要目录已创建或确认存在")
            
        except Exception as e:
            self.logger.error(f"创建目录时出错: {e}")
            raise
    
    def get_output_path(self, algorithm_name: str) -> Path:
        """
        获取算法的输出路径
        
        参数:
            algorithm_name: 算法名称
            
        返回:
            输出路径
        """
        output_base = Path(self.config.get('paths.output', 'output'))
        algorithm_path = output_base / algorithm_name
        algorithm_path.mkdir(parents=True, exist_ok=True)
        return algorithm_path
    
    def get_temp_path(self) -> Path:
        """
        获取临时文件路径
        
        返回:
            临时文件路径
        """
        temp_path = Path(self.config.get('paths.temp', 'temp'))
        temp_path.mkdir(parents=True, exist_ok=True)
        return temp_path
    
    def generate_filename(self, algorithm_name: str, function_name: str, 
                         file_type: str, timestamp: Optional[str] = None) -> str:
        """
        生成标准化的文件名
        
        参数:
            algorithm_name: 算法名称
            function_name: 函数名称
            file_type: 文件类型 ('gif', 'data', 'comparison', 'log')
            timestamp: 时间戳，如果为None则自动生成
            
        返回:
            生成的文件名
        """
        if timestamp is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # 获取文件扩展名
        extensions = {
            'gif': '.gif',
            'data': '.json',
            'comparison': '.json',
            'log': '.log',
            'png': '.png',
            'pdf': '.pdf'
        }
        
        ext = extensions.get(file_type, '.txt')
        
        # 生成文件名
        filename = f"{algorithm_name}_{function_name}_{file_type}_{timestamp}{ext}"
        
        self.logger.debug(f"生成文件名: {filename}")
        return filename
    
    def save_json(self, data: Dict[str, Any], file_path: Union[str, Path], 
                  indent: int = 2, ensure_ascii: bool = False) -> bool:
        """
        保存JSON数据到文件
        
        参数:
            data: 要保存的数据
            file_path: 文件路径
            indent: 缩进空格数
            ensure_ascii: 是否确保ASCII编码
            
        返回:
            是否保存成功
        """
        try:
            file_path = Path(file_path)
            file_path.parent.mkdir(parents=True, exist_ok=True)
            
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=indent, ensure_ascii=ensure_ascii)
            
            self.logger.info(f"JSON数据已保存到: {file_path}")
            return True
            
        except Exception as e:
            self.logger.error(f"保存JSON文件时出错: {e}")
            return False
    
    def load_json(self, file_path: Union[str, Path]) -> Optional[Dict[str, Any]]:
        """
        从文件加载JSON数据
        
        参数:
            file_path: 文件路径
            
        返回:
            加载的数据，如果失败则返回None
        """
        try:
            file_path = Path(file_path)
            
            if not file_path.exists():
                self.logger.warning(f"文件不存在: {file_path}")
                return None
            
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            self.logger.debug(f"JSON数据已从 {file_path} 加载")
            return data
            
        except Exception as e:
            self.logger.error(f"加载JSON文件时出错: {e}")
            return None
    
    def list_files(self, directory: Union[str, Path], pattern: str = "*", 
                   recursive: bool = False) -> List[Path]:
        """
        列出目录中的文件
        
        参数:
            directory: 目录路径
            pattern: 文件模式（如 "*.json"）
            recursive: 是否递归搜索
            
        返回:
            文件路径列表
        """
        try:
            directory = Path(directory)
            
            if not directory.exists():
                self.logger.warning(f"目录不存在: {directory}")
                return []
            
            if recursive:
                files = list(directory.rglob(pattern))
            else:
                files = list(directory.glob(pattern))
            
            # 只返回文件，不包括目录
            files = [f for f in files if f.is_file()]
            
            self.logger.debug(f"在 {directory} 中找到 {len(files)} 个文件")
            return files
            
        except Exception as e:
            self.logger.error(f"列出文件时出错: {e}")
            return []
    
    def clean_old_files(self, directory: Union[str, Path], days: int = 30, 
                       pattern: str = "*", dry_run: bool = True) -> List[Path]:
        """
        清理旧文件
        
        参数:
            directory: 目录路径
            days: 保留天数
            pattern: 文件模式
            dry_run: 是否只是预览，不实际删除
            
        返回:
            被删除（或将被删除）的文件列表
        """
        try:
            directory = Path(directory)
            
            if not directory.exists():
                self.logger.warning(f"目录不存在: {directory}")
                return []
            
            # 计算截止时间
            cutoff_time = datetime.now().timestamp() - (days * 24 * 60 * 60)
            
            # 找到旧文件
            old_files = []
            for file_path in directory.glob(pattern):
                if file_path.is_file() and file_path.stat().st_mtime < cutoff_time:
                    old_files.append(file_path)
            
            if dry_run:
                self.logger.info(f"预览模式: 找到 {len(old_files)} 个超过 {days} 天的文件")
                for file_path in old_files:
                    file_age = (datetime.now().timestamp() - file_path.stat().st_mtime) / (24 * 60 * 60)
                    self.logger.info(f"  - {file_path} (已存在 {file_age:.1f} 天)")
            else:
                # 实际删除文件
                deleted_count = 0
                for file_path in old_files:
                    try:
                        file_path.unlink()
                        deleted_count += 1
                        self.logger.info(f"已删除旧文件: {file_path}")
                    except Exception as e:
                        self.logger.error(f"删除文件 {file_path} 时出错: {e}")
                
                self.logger.info(f"成功删除 {deleted_count} 个旧文件")
            
            return old_files
            
        except Exception as e:
            self.logger.error(f"清理旧文件时出错: {e}")
            return []
    
    def backup_file(self, file_path: Union[str, Path], 
                   backup_dir: Optional[Union[str, Path]] = None) -> Optional[Path]:
        """
        备份文件
        
        参数:
            file_path: 要备份的文件路径
            backup_dir: 备份目录，如果为None则使用默认备份目录
            
        返回:
            备份文件路径，如果失败则返回None
        """
        try:
            file_path = Path(file_path)
            
            if not file_path.exists():
                self.logger.warning(f"要备份的文件不存在: {file_path}")
                return None
            
            # 确定备份目录
            if backup_dir is None:
                backup_dir = self.get_temp_path() / "backups"
            else:
                backup_dir = Path(backup_dir)
            
            backup_dir.mkdir(parents=True, exist_ok=True)
            
            # 生成备份文件名
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_name = f"{file_path.stem}_{timestamp}{file_path.suffix}"
            backup_path = backup_dir / backup_name
            
            # 复制文件
            shutil.copy2(file_path, backup_path)
            
            self.logger.info(f"文件已备份: {file_path} -> {backup_path}")
            return backup_path
            
        except Exception as e:
            self.logger.error(f"备份文件时出错: {e}")
            return None
    
    def get_file_info(self, file_path: Union[str, Path]) -> Optional[Dict[str, Any]]:
        """
        获取文件信息
        
        参数:
            file_path: 文件路径
            
        返回:
            文件信息字典，如果失败则返回None
        """
        try:
            file_path = Path(file_path)
            
            if not file_path.exists():
                return None
            
            stat = file_path.stat()
            
            info = {
                'name': file_path.name,
                'path': str(file_path.absolute()),
                'size': stat.st_size,
                'size_mb': stat.st_size / (1024 * 1024),
                'created': datetime.fromtimestamp(stat.st_ctime).isoformat(),
                'modified': datetime.fromtimestamp(stat.st_mtime).isoformat(),
                'accessed': datetime.fromtimestamp(stat.st_atime).isoformat(),
                'is_file': file_path.is_file(),
                'is_directory': file_path.is_dir(),
                'suffix': file_path.suffix,
                'stem': file_path.stem
            }
            
            return info
            
        except Exception as e:
            self.logger.error(f"获取文件信息时出错: {e}")
            return None
    
    def create_directory_structure(self, base_path: Union[str, Path], 
                                 structure: Dict[str, Any]) -> bool:
        """
        创建目录结构
        
        参数:
            base_path: 基础路径
            structure: 目录结构字典
            
        返回:
            是否创建成功
        """
        try:
            base_path = Path(base_path)
            
            def create_recursive(current_path: Path, struct: Dict[str, Any]):
                for name, content in struct.items():
                    new_path = current_path / name
                    
                    if isinstance(content, dict):
                        # 这是一个目录
                        new_path.mkdir(parents=True, exist_ok=True)
                        create_recursive(new_path, content)
                    else:
                        # 这是一个文件（如果content是字符串）
                        new_path.parent.mkdir(parents=True, exist_ok=True)
                        if isinstance(content, str):
                            new_path.write_text(content, encoding='utf-8')
            
            create_recursive(base_path, structure)
            self.logger.info(f"目录结构已创建在: {base_path}")
            return True
            
        except Exception as e:
            self.logger.error(f"创建目录结构时出错: {e}")
            return False
    
    def get_disk_usage(self, path: Union[str, Path]) -> Dict[str, float]:
        """
        获取磁盘使用情况
        
        参数:
            path: 路径
            
        返回:
            磁盘使用情况字典
        """
        try:
            path = Path(path)
            
            if not path.exists():
                return {}
            
            usage = shutil.disk_usage(path)
            
            return {
                'total_gb': usage.total / (1024**3),
                'used_gb': (usage.total - usage.free) / (1024**3),
                'free_gb': usage.free / (1024**3),
                'used_percent': ((usage.total - usage.free) / usage.total) * 100
            }
            
        except Exception as e:
            self.logger.error(f"获取磁盘使用情况时出错: {e}")
            return {}
    
    def compress_directory(self, directory: Union[str, Path], 
                          output_path: Union[str, Path], 
                          format: str = 'zip') -> bool:
        """
        压缩目录
        
        参数:
            directory: 要压缩的目录
            output_path: 输出文件路径（不包括扩展名）
            format: 压缩格式 ('zip', 'tar', 'gztar', 'bztar', 'xztar')
            
        返回:
            是否压缩成功
        """
        try:
            directory = Path(directory)
            output_path = Path(output_path)
            
            if not directory.exists():
                self.logger.warning(f"要压缩的目录不存在: {directory}")
                return False
            
            # 创建输出目录
            output_path.parent.mkdir(parents=True, exist_ok=True)
            
            # 压缩
            shutil.make_archive(str(output_path), format, str(directory))
            
            self.logger.info(f"目录已压缩: {directory} -> {output_path}.{format}")
            return True
            
        except Exception as e:
            self.logger.error(f"压缩目录时出错: {e}")
            return False