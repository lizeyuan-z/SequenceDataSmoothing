import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline
import warnings


warnings.filterwarnings("ignore")
plt.rcParams['font.sans-serif'] = ['STSong']


# 生成示例数据
x = np.linspace(0, 10, 20)  # X坐标
y = np.random.rand(20) * 10  # 随机生成Y坐标

# 创建贝塞尔曲线插值器
tck = make_interp_spline(x, y, k=3)

# 生成平滑后的数据点
x_new = np.linspace(min(x), max(x), 200)  # 新的X坐标范围
y_smooth = tck(x_new)

# 绘制原始数据和平滑后的贝塞尔曲线
plt.figure(figsize=(10, 6))
plt.scatter(x, y, label="原始数据", color='blue')
plt.plot(x_new, y_smooth, label="平滑后的贝塞尔曲线", color='red')
plt.legend()
plt.title("贝塞尔曲线数据平滑示例")
plt.xlabel("X坐标")
plt.ylabel("Y坐标")
plt.grid(True)
plt.show()