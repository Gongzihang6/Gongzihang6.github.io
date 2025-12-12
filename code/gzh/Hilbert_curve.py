import turtle

# ==========================================
# 代码名称：2D Hilbert 曲线递归绘制 (Turtle版)
# 功能：使用递归算法在屏幕上绘制指定阶数的二维 Hilbert 曲线。
# 实现原理：
#   1. 基于 Lindenmayer 系统 (L-System) 的递归逻辑。
#   2. 将曲线分解为 左旋(A) 和 右旋(B) 两种基本形态。
#   3. 在递归过程中，通过翻转角度 (angle vs -angle) 来处理四个子区域的旋转方向，
#      确保曲线在进入和离开子区域时能正确连接。
# ==========================================

def hilbert_curve(t, order, step, angle):
    """
    递归绘制 Hilbert 曲线的核心函数
    
    参数:
    t     : turtle 对象 (画笔)
    order : 当前递归阶数 (当 order=0 时停止递归)
    step  : 每次前进的步长 (线段长度)
    angle : 转弯角度 (通常为 90度，正负决定旋转方向)
    """
    
    # 递归终止条件：如果是 0 阶，什么都不画，直接返回
    if order == 0:
        return

    # === 步骤分解 ===
    # 这是一个经典的 Hilbert 递归模式：
    # 1. 转向并进入第一个子区域 (递归调用，角度翻转)
    # 2. 前进
    # 3. 反向转向并进入第二个子区域 (递归调用，角度不变)
    # 4. 前进
    # 5. 进入第三个子区域 (递归调用，角度不变)
    # 6. 前进
    # 7. 转向并进入第四个子区域 (递归调用，角度翻转)

    # --- 第一部分 (左下) ---
    t.right(angle)
    hilbert_curve(t, order - 1, step, -angle) # 递归：注意这里角度取反
    
    t.forward(step) # 连接线
    
    # --- 第二部分 (左上) ---
    t.left(angle)
    hilbert_curve(t, order - 1, step, angle)  # 递归：角度不变
    
    t.forward(step) # 连接线
    
    # --- 第三部分 (右上) ---
    hilbert_curve(t, order - 1, step, angle)  # 递归：角度不变
    
    t.left(angle)
    t.forward(step) # 连接线
    
    # --- 第四部分 (右下) ---
    hilbert_curve(t, order - 1, step, -angle) # 递归：注意这里角度取反
    t.right(angle)

# ==========================================
# 主程序设置
# ==========================================
def main():
    # 1. 参数设置
    ORDER = 2        # 阶数：建议设置在 1 到 6 之间
    SIZE = 600       # 窗口绘图区域的大小 (像素)
    
    # 根据窗口大小自动计算每一步的长度
    # 2^ORDER 是网格一边的格子数，-1 是因为步数比点数少1，但在高阶时忽略-1简化计算
    step_size = SIZE / (2 ** ORDER)

    # 2. 初始化 Turtle 画布
    window = turtle.Screen()
    window.title(f"2D Hilbert Curve - Order {ORDER} (Recursive)")
    window.bgcolor("black")
    window.setup(width=SIZE + 100, height=SIZE + 100)

    # 3. 初始化画笔
    pen = turtle.Turtle()
    pen.color("cyan")      # 线条颜色
    pen.speed(0.8)           # 设置绘图速度：0 为最快，1 为最慢
    pen.width(2)           # 线条粗细

    # 4. 调整起始位置
    # 默认从屏幕中心开始，为了画满整个正方形，我们需要把画笔移到左上角
    offset = SIZE / 2
    pen.penup()
    pen.goto(-offset + step_size/2, offset - step_size/2)
    pen.pendown()

    # 5. 开始递归绘制
    # 初始调用：order=ORDER, step=step_size, angle=90
    print(f"开始绘制 {ORDER} 阶 Hilbert 曲线...")
    hilbert_curve(pen, ORDER, step_size, 90)
    print("绘制完成。")

    # 6. 保持窗口打开，点击窗口关闭
    window.exitonclick()

if __name__ == "__main__":
    main()