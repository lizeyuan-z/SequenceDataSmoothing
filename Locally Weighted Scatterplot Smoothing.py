import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
import warnings


warnings.filterwarnings("ignore")
plt.rcParams['font.sans-serif'] = ['STSong']


# 生成示例数据
x = np.linspace(0, 10, 100)
y = np.sin(x) + np.random.normal(0, 0.2, 100)

# 执行Loess平滑
lowess = sm.nonparametric.lowess(y, x, frac=0.3)  # frac参数控制平滑带宽，可以调整以获得不同的平滑度

# 获取平滑后的数据
x_smooth, y_smooth = lowess.T

# 绘制原始数据和Loess平滑曲线
plt.figure(figsize=(10, 6))
plt.scatter(x, y, label="原始数据", color='blue', alpha=0.6)
plt.plot(x_smooth, y_smooth, label="Loess平滑", color='red')
plt.legend()
plt.title("Loess平滑示例")
plt.xlabel("X轴")
plt.ylabel("Y轴")
plt.grid(True)
plt.show()