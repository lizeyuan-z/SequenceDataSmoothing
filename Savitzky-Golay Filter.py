# pip install scipy

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter
import warnings


warnings.filterwarnings("ignore")
plt.rcParams['font.sans-serif'] = ['STSong']


# 生成示例数据
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x) + np.random.normal(0, 0.2, len(x))

# 执行Savitzky-Golay滤波
window_length = 11  # 窗口长度（奇数）
polyorder = 2  # 多项式阶数
y_smoothed = savgol_filter(y, window_length, polyorder)

# 绘制原始数据和平滑后的数据
plt.figure(figsize=(10, 6))
plt.plot(x, y, label="原始数据", color='blue', alpha=0.6)
plt.plot(x, y_smoothed, label="Savitzky-Golay滤波", color='red')
plt.legend()
plt.title("Savitzky-Golay滤波器数据平滑示例")
plt.xlabel("X轴")
plt.ylabel("Y轴")
plt.grid(True)
plt.show()