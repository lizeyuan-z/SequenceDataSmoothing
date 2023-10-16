import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter
import warnings


warnings.filterwarnings("ignore")
plt.rcParams['font.sans-serif'] = ['STSong']


# 生成示例数据
fs = 1000  # 采样频率
t = np.linspace(0, 5, 5 * fs, endpoint=False)
data = 5 * np.sin(2 * np.pi * 3 * t) + 2 * np.sin(2 * np.pi * 50 * t)

# 设计巴特沃斯低通滤波器
cutoff_freq = 10  # 截止频率（以Hz为单位）
nyquist_freq = 0.5 * fs
normal_cutoff = cutoff_freq / nyquist_freq
b, a = butter(4, normal_cutoff, btype='low', analog=False)

# 使用滤波器平滑数据
smoothed_data = lfilter(b, a, data)

# 绘制原始数据和平滑后的数据
plt.figure(figsize=(10, 6))
plt.plot(t, data, label="原始数据", color='blue')
plt.plot(t, smoothed_data, label="低通滤波后的数据", color='red')
plt.legend()
plt.title("巴特沃斯低通滤波器示例")
plt.xlabel("时间 (秒)")
plt.ylabel("数值")
plt.grid(True)
plt.show()