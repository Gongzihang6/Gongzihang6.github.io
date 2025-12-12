"""
基础优化算法可视化器
提供所有优化算法可视化的通用框架和接口
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import FancyBboxPatch
import os
from abc import ABC, abstractmethod
from typing import Dict, Any, Tuple, List, Optional, Callable
from pathlib import Path
import json
from datetime import datetime

from config import get_config
from algorithms.base_algorithm import OptimizationAlgorithm

class BaseOptimizationVisualizer:
    """
    基础优化算法可视化器
    """
    
    def __init__(self, algorithm: OptimizationAlgorithm, 
                 x_range: Optional[Tuple[float, float]] = None,
                 figsize: Optional[Tuple[int, int]] = None):
        """
        初始化基础可视化器
        
        参数:
            algorithm: 优化算法实例
            x_range: x轴显示范围
            figsize: 图形大小
        """
        self.algorithm = algorithm
        self.algorithm_name = algorithm.get_name()
        
        # 获取配置
        self.config = get_config()
        
        # 设置参数
        self.x_range = x_range or self.config.get(f'algorithms.{self.algorithm_name}.x_range', [-10, 10])
        
        viz_config = self.config.get_visualization_config()
        figure_config = viz_config.get('figure', {})
        self.figsize = figsize or (figure_config.get('width', 15), figure_config.get('height', 6))
        
        # 初始化图形
        self.fig, (self.ax1, self.ax2) = plt.subplots(1, 2, figsize=self.figsize)
        self.fig.suptitle(f'{self.algorithm_name} 算法可视化', 
                         fontsize=viz_config.get('fonts', {}).get('size', {}).get('title', 16), 
                         fontweight='bold')
        
        # 设置中文字体
        fonts = viz_config.get('fonts', {}).get('chinese', ['SimHei', 'Microsoft YaHei'])
        plt.rcParams['font.sans-serif'] = fonts
        plt.rcParams['axes.unicode_minus'] = False
        
        # 获取颜色配置
        self.colors = viz_config.get('colors', {})
        
        # 初始化历史记录
        self.history = {}
        
        # 输出路径
        self.output_path = self.config.get_output_path(self.algorithm_name)
    
    def setup_plots(self, history: Dict[str, np.ndarray], f: Callable):
        """
        设置绘图区域和初始化图形元素
        
        参数:
            history: 优化历史数据
            f: 目标函数
        """
        # 清空子图
        self.ax1.clear()
        self.ax2.clear()
        
        # 左侧子图：函数曲线和优化路径
        x_plot = np.linspace(self.x_range[0], self.x_range[1], 1000)
        y_plot = f(x_plot)
        
        self.ax1.plot(x_plot, y_plot, 
                     color=self.colors.get('function_curve', '#1f77b4'),
                     linewidth=2, label='目标函数 f(x)')
        self.ax1.set_xlabel('x', fontsize=self.config.get('visualization.fonts.size.label', 12))
        self.ax1.set_ylabel('f(x)', fontsize=self.config.get('visualization.fonts.size.label', 12))
        self.ax1.set_title(f'{self.algorithm_name} 优化路径', 
                          fontsize=self.config.get('visualization.fonts.size.title', 14), 
                          fontweight='bold')
        self.ax1.grid(True, alpha=0.3, color=self.colors.get('grid', '#cccccc'))
        self.ax1.legend()
        
        # 右侧子图：收敛曲线
        self.ax2.set_xlabel('迭代次数', fontsize=self.config.get('visualization.fonts.size.label', 12))
        self.ax2.set_ylabel('函数值 f(x)', fontsize=self.config.get('visualization.fonts.size.label', 12))
        self.ax2.set_title('收敛过程', 
                          fontsize=self.config.get('visualization.fonts.size.title', 14), 
                          fontweight='bold')
        self.ax2.grid(True, alpha=0.3, color=self.colors.get('grid', '#cccccc'))
        
        # 初始化动画元素
        self.current_point, = self.ax1.plot([], [], 'o', 
                                           color=self.colors.get('current_point', '#ff0000'),
                                           markersize=10, label='当前位置')
        self.path_line, = self.ax1.plot([], [], '--', 
                                       color=self.colors.get('path', '#ff0000'),
                                       alpha=0.7, linewidth=2, label='优化路径')
        self.convergence_line, = self.ax2.plot([], [], '-', 
                                              color=self.colors.get('convergence', '#2ca02c'),
                                              linewidth=2, label='函数值')
        
        # 添加图例
        self.ax1.legend()
        self.ax2.legend()
        
        # 添加信息文本框
        self.info_text = self.ax1.text(0.02, 0.98, '', transform=self.ax1.transAxes, 
                                      fontsize=self.config.get('visualization.fonts.size.text', 10), 
                                      verticalalignment='top',
                                      bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))
    
    def animate_frame(self, frame: int, history: Dict[str, np.ndarray]):
        """
        动画帧更新函数
        
        参数:
            frame: 当前帧数
            history: 优化历史数据
        """
        if frame >= len(history['x_values']):
            return self.current_point, self.path_line, self.convergence_line, self.info_text
        
        # 更新当前点位置
        current_x = history['x_values'][frame]
        current_y = history['f_values'][frame]
        self.current_point.set_data([current_x], [current_y])
        
        # 更新路径
        path_x = history['x_values'][:frame+1]
        path_y = history['f_values'][:frame+1]
        self.path_line.set_data(path_x, path_y)
        
        # 更新收敛曲线
        iterations = np.arange(frame + 1)
        convergence_y = history['f_values'][:frame+1]
        self.convergence_line.set_data(iterations, convergence_y)
        
        # 动态调整右侧子图的y轴范围
        if frame > 0:
            y_min, y_max = np.min(convergence_y), np.max(convergence_y)
            y_range = y_max - y_min
            if y_range > 0:
                self.ax2.set_ylim(y_min - 0.1 * y_range, y_max + 0.1 * y_range)
            self.ax2.set_xlim(0, max(10, frame + 1))
        
        # 更新信息文本
        info_str = self._format_info_text(frame, history)
        self.info_text.set_text(info_str)
        
        return self.current_point, self.path_line, self.convergence_line, self.info_text
    
    def _format_info_text(self, frame: int, history: Dict[str, np.ndarray]) -> str:
        """
        格式化信息文本
        
        参数:
            frame: 当前帧数
            history: 优化历史数据
            
        返回:
            格式化的信息字符串
        """
        current_x = history['x_values'][frame]
        current_y = history['f_values'][frame]
        
        # 安全地访问梯度数组，避免索引越界
        if frame < len(history['gradients']):
            gradient = history['gradients'][frame]
        else:
            gradient = history['gradients'][-1]  # 使用最后一个梯度值
        
        info_str = f'迭代: {frame}\n'
        info_str += f'x = {current_x:.4f}\n'
        info_str += f'f(x) = {current_y:.4f}\n'
        info_str += f'梯度 = {gradient:.4f}\n'
        
        # 添加算法特定信息
        additional_info = self._get_additional_info(frame, history)
        if additional_info:
            info_str += additional_info
        
        return info_str
    
    def _get_additional_info(self, frame: int, history: Dict[str, np.ndarray]) -> str:
        """
        获取算法特定的附加信息
        子类可以重写此方法来显示特定的信息
        
        参数:
            frame: 当前帧数
            history: 优化历史数据
            
        返回:
            附加信息字符串
        """
        return ""
    
    def create_animation_from_history(self, history: Dict[str, np.ndarray], 
                                     function_name: str = "custom", 
                                     save_gif: bool = True, 
                                     save_data: bool = True,
                                     x0: Optional[float] = None,
                                     **kwargs):
        """
        基于已有的优化历史创建动画（不重新执行优化）
        
        参数:
            history: 已有的优化历史，键包含x_values, f_values, gradients等
            function_name: 函数名称，用于文件命名
            save_gif: 是否保存为GIF文件
            save_data: 是否保存优化数据
            x0: 初始点（可选，默认取history中的第一个x值）
            **kwargs: 算法参数（用于保存数据时记录）
        """
        print(f"基于历史创建 {self.algorithm_name} 动画...")
        if x0 is None:
            try:
                x0 = float(history['x_values'][0])
            except Exception:
                x0 = float(history.get('x0', 0.0))
        # 注意: 这里无法显示 f(x0)，因为 f 函数没有被传递
        print(f"初始点: x0 = {x0:.4f}")
        print("-" * 50)
        
        # 设置绘图
        # 注意: 这里无法绘制函数曲线，因为 f 函数没有被传递
        # self.setup_plots(history, f)
        
        # 创建动画
        frames = len(history['x_values'])
        anim_config = self.config.get('visualization.animation', {})
        interval = anim_config.get('interval', 200)
        
        anim = animation.FuncAnimation(
            self.fig,
            lambda frame: self.animate_frame(frame, history),
            frames=frames,
            interval=interval,
            blit=False,
            repeat=anim_config.get('repeat', True)
        )
        
        # 生成时间戳
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # 保存GIF动画
        if save_gif:
            gif_filename = self.config.generate_filename(
                self.algorithm_name, function_name, 'gif', timestamp
            )
            gif_path = self.output_path / gif_filename
            print(f"正在保存动画为 {gif_path}...")
            try:
                fps = anim_config.get('fps', 10)
                dpi = self.config.get('visualization.figure.dpi', 100)
                anim.save(str(gif_path), writer='pillow', fps=fps, dpi=dpi)
                print(f"动画已保存为: {gif_path}")
            except Exception as e:
                print(f"保存动画时出错: {e}")
                print("请确保已安装 Pillow 库: pip install Pillow")
        
        # 保存优化数据
        if save_data:
            data_filename = self.config.generate_filename(
                self.algorithm_name, function_name, 'data', timestamp
            )
            data_path = self.output_path / data_filename
            self._save_optimization_data(history, data_path, x0, **kwargs)
        
        # 布局调整但不展示（性能分析时避免阻塞）
        plt.tight_layout()
        
        # 返回动画对象
        return anim
    
    def run(self, x0: float, f: Callable, df: Callable, function_name: str = "custom", 
            save_gif: bool = True, save_data: bool = True, 
            show_plot: bool = True, **kwargs):
        """
        运行优化和可视化
        
        参数:
            x0: 初始点
            f: 目标函数
            df: 目标函数的导数
            function_name: 函数名称，用于文件命名
            save_gif: 是否保存为GIF文件
            save_data: 是否保存优化数据
            show_plot: 是否显示图形窗口
            **kwargs: 算法特定参数
        """
        print(f"开始 {self.algorithm_name} 优化...")
        print(f"初始点: x0 = {x0:.4f}, f(x0) = {f(x0):.4f}")
        print("-" * 50)
        
        # 执行优化并获取历史数据
        history = self.algorithm.optimize(x0, f, df, **kwargs)
        self.history = history
        
        # 设置绘图
        self.setup_plots(history, f)
        
        # 创建动画
        frames = len(history['x_values'])
        anim_config = self.config.get('visualization.animation', {})
        interval = anim_config.get('interval', 200)
        
        anim = animation.FuncAnimation(
            self.fig, 
            lambda frame: self.animate_frame(frame, history),
            frames=frames,
            interval=interval,
            blit=False,
            repeat=anim_config.get('repeat', True)
        )
        
        # 生成时间戳
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # 保存GIF动画
        if save_gif:
            gif_filename = self.config.generate_filename(
                self.algorithm_name, function_name, 'gif', timestamp
            )
            gif_path = self.output_path / gif_filename
            
            print(f"正在保存动画为 {gif_path}...")
            try:
                fps = anim_config.get('fps', 10)
                dpi = self.config.get('visualization.figure.dpi', 100)
                anim.save(str(gif_path), writer='pillow', fps=fps, dpi=dpi)
                print(f"动画已保存为: {gif_path}")
            except Exception as e:
                print(f"保存动画时出错: {e}")
                print("请确保已安装 Pillow 库: pip install Pillow")
        
        # 保存优化数据
        if save_data:
            data_filename = self.config.generate_filename(
                self.algorithm_name, function_name, 'data', timestamp
            )
            data_path = self.output_path / data_filename
            
            self._save_optimization_data(history, data_path, x0, **kwargs)
        
        # 显示动画
        plt.tight_layout()
        if show_plot:
            plt.show()
        
        # 打印最终统计信息
        self._print_final_statistics(history)
        
        return anim, history
    
    def _save_optimization_data(self, history: Dict[str, np.ndarray], 
                               file_path: Path, x0: float, **kwargs):
        """
        保存优化数据到JSON文件
        
        参数:
            history: 优化历史数据
            file_path: 保存路径
            x0: 初始点
            **kwargs: 算法参数
        """
        try:
            # 辅助函数：安全转换为可序列化类型
            def to_serializable(v):
                import numpy as np
                if isinstance(v, np.ndarray):
                    return v.tolist()
                # 处理numpy标量
                if isinstance(v, (np.floating,)):
                    return float(v)
                if isinstance(v, (np.integer,)):
                    return int(v)
                if isinstance(v, (np.bool_,)):
                    return bool(v)
                # 处理Python内建类型
                if isinstance(v, (float, int, bool, str, list, dict)):
                    return v
                return str(v)
            
            # 转换numpy数组为列表以便JSON序列化
            data = {
                'algorithm': self.algorithm_name,
                'algorithm_display_name': self.algorithm_name,
                'initial_point': float(x0),
                'parameters': {k: (bool(v) if isinstance(v, (bool, np.bool_)) else (float(v) if isinstance(v, (int, float, np.number)) else to_serializable(v)))
                              for k, v in kwargs.items()},
                'history': {k: to_serializable(v) for k, v in history.items()},
                'final_result': {
                    'x': float(history['x_values'][-1]),
                    'f_x': float(history['f_values'][-1]),
                    'gradient': float(history['gradients'][-1]),
                    'iterations': int(len(history['x_values']) - 1),
                    'improvement': float(history['f_values'][0] - history['f_values'][-1]),
                    'converged': bool(history.get('converged', False))
                },
                'timestamp': datetime.now().isoformat()
            }
            
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            
            print(f"优化数据已保存为: {file_path}")
            
        except Exception as e:
            print(f"保存优化数据时出错: {e}")
    
    def _print_final_statistics(self, history: Dict[str, np.ndarray]):
        """
        打印最终统计信息
        
        参数:
            history: 优化历史数据
        """
        print("-" * 50)
        print("优化统计信息:")
        print(f"  总迭代次数: {len(history['x_values']) - 1}")
        print(f"  最终位置: x = {history['x_values'][-1]:.6f}")
        print(f"  最终函数值: f(x) = {history['f_values'][-1]:.6f}")
        print(f"  最终梯度: {history['gradients'][-1]:.6f}")
        print(f"  函数值改善: {history['f_values'][0] - history['f_values'][-1]:.6f}")
        
        # 添加算法特定统计信息
        additional_stats = self._get_additional_statistics(history)
        if additional_stats:
            print(additional_stats)
        
        print("=" * 50)
    
    def _get_additional_statistics(self, history: Dict[str, np.ndarray]) -> str:
        """
        获取算法特定的统计信息
        子类可以重写此方法来显示特定的统计信息
        
        参数:
            history: 优化历史数据
            
        返回:
            附加统计信息字符串
        """
        return ""
    
    
    def _save_comparison_results(self, results: List[Dict], function_name: str, x0: float):
        """
        保存参数比较结果
        
        参数:
            results: 比较结果列表
            function_name: 函数名称
            x0: 初始点
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{self.algorithm_name}_{function_name}_comparison_{timestamp}.json"
        file_path = self.output_path / filename
        
        comparison_data = {
            'algorithm': self.algorithm_name,
            'function_name': function_name,
            'initial_point': float(x0),
            'timestamp': datetime.now().isoformat(),
            'results': results,
            'summary': {
                'best_result': min(results, key=lambda x: x['final_f_x']),
                'fastest_convergence': min(results, key=lambda x: x['iterations']),
                'largest_improvement': max(results, key=lambda x: x['improvement'])
            }
        }
        
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(comparison_data, f, indent=2, ensure_ascii=False)
            print(f"参数比较结果已保存为: {file_path}")
        except Exception as e:
            print(f"保存比较结果时出错: {e}")
