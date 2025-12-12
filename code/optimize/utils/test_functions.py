"""
测试函数库
提供各种用于测试优化算法的数学函数
"""

import numpy as np
from typing import Callable, Tuple, Dict, Any

class TestFunctions:
    """
    测试函数集合类
    包含各种常用的优化测试函数及其导数
    """
    
    @staticmethod
    def quadratic(a: float = 1.0, b: float = 0.0, c: float = 0.0) -> Tuple[Callable, Callable, Callable]:
        """
        二次函数: f(x) = a(x-b)² + c
        
        参数:
            a: 二次项系数
            b: 对称轴位置
            c: 常数项
            
        返回:
            (函数, 一阶导数, 二阶导数)
        """
        def f(x):
            return a * (x - b) ** 2 + c
        
        def df(x):
            return 2 * a * (x - b)
            
        def d2f(x):
            return 2 * a
        
        return f, df, d2f
    
    @staticmethod
    def cubic(a: float = 1.0, b: float = 0.0, c: float = 0.0, d: float = 0.0) -> Tuple[Callable, Callable]:
        """
        三次函数: f(x) = a(x-b)³ + c(x-b) + d
        
        参数:
            a: 三次项系数
            b: 平移参数
            c: 一次项系数
            d: 常数项
            
        返回:
            (函数, 导数函数)
        """
        def f(x):
            return a * (x - b) ** 3 + c * (x - b) + d
        
        def df(x):
            return 3 * a * (x - b) ** 2 + c
        
        return f, df
    
    @staticmethod
    def quartic(a: float = 1.0, b: float = 0.0, c: float = 0.0) -> Tuple[Callable, Callable]:
        """
        四次函数: f(x) = a(x-b)⁴ + c
        
        参数:
            a: 四次项系数
            b: 对称轴位置
            c: 常数项
            
        返回:
            (函数, 导数函数)
        """
        def f(x):
            return a * (x - b) ** 4 + c
        
        def df(x):
            return 4 * a * (x - b) ** 3
        
        return f, df
    
    @staticmethod
    def rosenbrock_1d(a: float = 1.0, b: float = 100.0) -> Tuple[Callable, Callable]:
        """
        一维Rosenbrock函数: f(x) = (a-x)² + b(x²-x)²
        
        参数:
            a: 第一项系数
            b: 第二项系数
            
        返回:
            (函数, 导数函数)
        """
        def f(x):
            return (a - x) ** 2 + b * (x ** 2 - x) ** 2
        
        def df(x):
            return -2 * (a - x) + 2 * b * (x ** 2 - x) * (2 * x - 1)
        
        return f, df
    
    @staticmethod
    def beale_1d(x_center: float = 0.0) -> Tuple[Callable, Callable]:
        """
        修改的Beale函数（一维版本）: f(x) = (1.5 - x + x²)² + (2.25 - x + x³)²
        
        参数:
            x_center: 中心点偏移
            
        返回:
            (函数, 导数函数)
        """
        def f(x):
            x_shifted = x - x_center
            term1 = (1.5 - x_shifted + x_shifted ** 2) ** 2
            term2 = (2.25 - x_shifted + x_shifted ** 3) ** 2
            return term1 + term2
        
        def df(x):
            x_shifted = x - x_center
            term1 = 1.5 - x_shifted + x_shifted ** 2
            term2 = 2.25 - x_shifted + x_shifted ** 3
            dterm1 = 2 * term1 * (-1 + 2 * x_shifted)
            dterm2 = 2 * term2 * (-1 + 3 * x_shifted ** 2)
            return dterm1 + dterm2
        
        return f, df
    
    @staticmethod
    def multi_modal(peaks: list = None) -> Tuple[Callable, Callable]:
        """
        多峰函数: 多个高斯峰的组合
        
        参数:
            peaks: 峰的参数列表，每个峰包含 (amplitude, center, width)
            
        返回:
            (函数, 导数函数)
        """
        if peaks is None:
            peaks = [(1.0, -2.0, 0.5), (-0.8, 1.0, 0.3), (0.6, 3.0, 0.7)]
        
        def f(x):
            result = 0
            for amp, center, width in peaks:
                result += amp * np.exp(-((x - center) / width) ** 2)
            return -result  # 负号使其成为最小化问题
        
        def df(x):
            result = 0
            for amp, center, width in peaks:
                gaussian = amp * np.exp(-((x - center) / width) ** 2)
                result += gaussian * (-2 * (x - center) / (width ** 2))
            return -result  # 负号使其成为最小化问题
        
        return f, df
    
    @staticmethod
    def rastrigin_1d(A: float = 10.0, omega: float = 2 * np.pi) -> Tuple[Callable, Callable]:
        """
        一维Rastrigin函数: f(x) = A + x² - A*cos(ωx)
        
        参数:
            A: 振幅参数
            omega: 频率参数
            
        返回:
            (函数, 导数函数)
        """
        def f(x):
            return A + x ** 2 - A * np.cos(omega * x)
        
        def df(x):
            return 2 * x + A * omega * np.sin(omega * x)
        
        return f, df
    
    @staticmethod
    def ackley_1d(a: float = 20.0, b: float = 0.2, c: float = 2 * np.pi) -> Tuple[Callable, Callable]:
        """
        一维Ackley函数: f(x) = -a*exp(-b*|x|) - exp(cos(c*x)) + a + e
        
        参数:
            a: 第一项系数
            b: 指数衰减系数
            c: 余弦频率
            
        返回:
            (函数, 导数函数)
        """
        def f(x):
            term1 = -a * np.exp(-b * np.abs(x))
            term2 = -np.exp(np.cos(c * x))
            return term1 + term2 + a + np.e
        
        def df(x):
            sign_x = np.sign(x)
            dterm1 = -a * (-b * sign_x) * np.exp(-b * np.abs(x))
            dterm2 = -np.exp(np.cos(c * x)) * (-np.sin(c * x)) * c
            return dterm1 + dterm2
        
        return f, df
    
    @staticmethod
    def schwefel_1d(alpha: float = 418.9829) -> Tuple[Callable, Callable]:
        """
        一维Schwefel函数: f(x) = α - x*sin(√|x|)
        
        参数:
            alpha: 常数项
            
        返回:
            (函数, 导数函数)
        """
        def f(x):
            return alpha - x * np.sin(np.sqrt(np.abs(x)))
        
        def df(x):
            if np.abs(x) < 1e-10:
                return -np.sin(0) - 0  # 在x=0附近的近似
            
            sqrt_abs_x = np.sqrt(np.abs(x))
            sign_x = np.sign(x)
            
            # df/dx = -sin(√|x|) - x * cos(√|x|) * (1/(2√|x|)) * sign(x)
            term1 = -np.sin(sqrt_abs_x)
            term2 = -x * np.cos(sqrt_abs_x) * (sign_x / (2 * sqrt_abs_x))
            
            return term1 + term2
        
        return f, df
    
    @staticmethod
    def griewank_1d(scale: float = 1.0) -> Tuple[Callable, Callable]:
        """
        一维Griewank函数: f(x) = x²/4000 - cos(x) + 1
        
        参数:
            scale: 缩放因子
            
        返回:
            (函数, 导数函数)
        """
        def f(x):
            scaled_x = x / scale
            return scaled_x ** 2 / 4000 - np.cos(scaled_x) + 1
        
        def df(x):
            scaled_x = x / scale
            return (2 * scaled_x / 4000 + np.sin(scaled_x)) / scale
        
        return f, df

    @staticmethod
    def get_function(name: str, **params) -> Tuple[Callable, ...]:
        """
        根据名称获取函数
        """
        if not hasattr(TestFunctions, name):
            raise ValueError(f"函数 '{name}' 不存在.")
        
        func_method = getattr(TestFunctions, name)
        return func_method(**params)
    
    @staticmethod
    def get_function_info() -> Dict[str, Dict[str, Any]]:
        """
        获取所有测试函数的信息
        
        返回:
            包含函数信息的字典
        """
        return {
            'quadratic': {
                'name': '二次函数',
                'description': '简单的二次函数，单一最小值点',
                'difficulty': '简单',
                'recommended_range': [-10, 10],
                'global_minimum': '取决于参数'
            },
            'cubic': {
                'name': '三次函数',
                'description': '三次函数，可能有局部极值',
                'difficulty': '中等',
                'recommended_range': [-5, 5],
                'global_minimum': '取决于参数'
            },
            'quartic': {
                'name': '四次函数',
                'description': '四次函数，对称性好',
                'difficulty': '简单',
                'recommended_range': [-5, 5],
                'global_minimum': '取决于参数'
            },
            'rosenbrock_1d': {
                'name': 'Rosenbrock函数',
                'description': '经典优化测试函数，收敛困难',
                'difficulty': '困难',
                'recommended_range': [-2, 2],
                'global_minimum': 'x = 1'
            },
            'beale_1d': {
                'name': 'Beale函数',
                'description': '多项式函数，有多个局部极值',
                'difficulty': '中等',
                'recommended_range': [-5, 5],
                'global_minimum': '约在x = 3附近'
            },
            'multi_modal': {
                'name': '多峰函数',
                'description': '多个局部最优解，测试全局优化能力',
                'difficulty': '困难',
                'recommended_range': [-5, 5],
                'global_minimum': '取决于峰的配置'
            },
            'rastrigin_1d': {
                'name': 'Rastrigin函数',
                'description': '高度多峰函数，大量局部最优解',
                'difficulty': '非常困难',
                'recommended_range': [-5, 5],
                'global_minimum': 'x = 0'
            },
            'ackley_1d': {
                'name': 'Ackley函数',
                'description': '指数和三角函数组合，多峰',
                'difficulty': '困难',
                'recommended_range': [-5, 5],
                'global_minimum': 'x = 0'
            },
            'schwefel_1d': {
                'name': 'Schwefel函数',
                'description': '复杂的多峰函数',
                'difficulty': '非常困难',
                'recommended_range': [-500, 500],
                'global_minimum': 'x ≈ 420.97'
            },
            'griewank_1d': {
                'name': 'Griewank函数',
                'description': '多峰函数，远离原点时振荡',
                'difficulty': '困难',
                'recommended_range': [-10, 10],
                'global_minimum': 'x = 0'
            }
        }
    
    @staticmethod
    def create_custom_function(expression: str, derivative_expression: str) -> Tuple[Callable, Callable]:
        """
        创建自定义函数
        
        参数:
            expression: 函数表达式（字符串形式）
            derivative_expression: 导数表达式（字符串形式）
            
        返回:
            (函数, 导数函数)
            
        注意:
            表达式中应使用numpy函数，如np.sin, np.cos, np.exp等
            变量名应为'x'
        """
        # 安全的命名空间，只包含必要的函数
        safe_namespace = {
            'np': np,
            'sin': np.sin,
            'cos': np.cos,
            'tan': np.tan,
            'exp': np.exp,
            'log': np.log,
            'sqrt': np.sqrt,
            'abs': np.abs,
            'pi': np.pi,
            'e': np.e
        }
        
        def f(x):
            safe_namespace['x'] = x
            return eval(expression, safe_namespace)
        
        def df(x):
            safe_namespace['x'] = x
            return eval(derivative_expression, safe_namespace)
        
        return f, df
    
    @classmethod
    def get_function_by_name(cls, name: str, **kwargs) -> Tuple[Callable, Callable]:
        """
        根据名称获取函数
        
        参数:
            name: 函数名称
            **kwargs: 函数参数
            
        返回:
            (函数, 导数函数)
        """
        function_map = {
            'quadratic': cls.quadratic,
            'cubic': cls.cubic,
            'quartic': cls.quartic,
            'rosenbrock_1d': cls.rosenbrock_1d,
            'beale_1d': cls.beale_1d,
            'multi_modal': cls.multi_modal,
            'rastrigin_1d': cls.rastrigin_1d,
            'ackley_1d': cls.ackley_1d,
            'schwefel_1d': cls.schwefel_1d,
            'griewank_1d': cls.griewank_1d
        }
        
        if name not in function_map:
            raise ValueError(f"未知的函数名称: {name}. 可用的函数: {list(function_map.keys())}")
        
        return function_map[name](**kwargs)
