# pip install PyWavelets

import numpy as np
import matplotlib.pyplot as plt
import pywt
import warnings


warnings.filterwarnings("ignore")
plt.rcParams['font.sans-serif'] = ['STSong']


# 生成示例数据
x = np.linspace(0, 2 * np.pi, 400)
y = np.sin(x) + np.random.normal(0, 0.1, len(x))

# 执行小波变换
wavelet = 'db4'  # 选择小波基函数
level = 3  # 分解的级数
coeffs = pywt.wavedec(y, wavelet, level=level)

# 将高频部分系数置零，以实现平滑
coeffs_smoothed = [coeffs[0]] + [np.zeros_like(coeffs[i]) for i in range(1, len(coeffs))]

# 重构平滑后的信号
y_smoothed = pywt.waverec(coeffs_smoothed, wavelet)

# 绘制原始数据和平滑后的数据
plt.figure(figsize=(10, 6))
plt.plot(x, y, label="原始数据", color='blue', alpha=0.6)
plt.plot(x, y_smoothed, label="小波平滑", color='red')
plt.legend()
plt.title("小波变换数据平滑示例")
plt.xlabel("X轴")
plt.ylabel("Y轴")
plt.grid(True)
plt.show()