import numpy as np
import matplotlib.pyplot as plt
import warnings


warnings.filterwarnings("ignore")
plt.rcParams['font.sans-serif'] = ['STSong']


# 示例数据
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
y = np.array([10, 8, 7, 6, 5, 4, 3, 2, 1])

# 三阶多项式拟合
degree = 3
coefficients = np.polyfit(x, y, degree)

# 构建多项式函数
poly = np.poly1d(coefficients)

# 生成用于绘图的新X值
x_new = np.linspace(min(x), max(x), 100)

# 计算拟合后的Y值
y_new = poly(x_new)

# 绘制原始数据和三阶多项式拟合曲线
plt.figure(figsize=(10, 6))
plt.scatter(x, y, label="原始数据", color='blue')
plt.plot(x_new, y_new, label="三阶多项式拟合", color='red')
plt.legend()
plt.title("三阶多项式拟合示例")
plt.xlabel("X轴")
plt.ylabel("Y轴")
plt.grid(True)
plt.show()