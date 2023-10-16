# pip install pykalman

import numpy as np
import matplotlib.pyplot as plt
from pykalman import KalmanFilter
import warnings


warnings.filterwarnings("ignore")
plt.rcParams['font.sans-serif'] = ['STSong']


# 生成示例数据
np.random.seed(0)
n = 100
x = np.linspace(0, 10, n)
y = 0.1 * x + np.random.normal(0, 0.5, n)

# 创建卡尔曼滤波器
kf = KalmanFilter(initial_state_mean=0, n_dim_obs=1)
kf = kf.em(y, n_iter=10)

# 获取平滑后的数据
(filtered_state_means, _) = kf.filter(y)

# 绘制原始数据和卡尔曼滤波后的数据
plt.figure(figsize=(10, 6))
plt.plot(x, y, label="原始数据", color='blue', alpha=0.6)
plt.plot(x, filtered_state_means, label="卡尔曼滤波", color='red')
plt.legend()
plt.title("卡尔曼滤波数据平滑示例")
plt.xlabel("X轴")
plt.ylabel("Y轴")
plt.grid(True)
plt.show()
