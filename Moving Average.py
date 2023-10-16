import numpy as np
import matplotlib.pyplot as plt
import warnings


warnings.filterwarnings("ignore")
plt.rcParams['font.sans-serif'] = ['STSong']

# 生成示例数据
data = np.array([10, 15, 12, 18, 20, 14, 16, 22, 19, 25])

# 定义移动平均窗口大小
window_size = 3

# 计算简单移动平均
sma = np.convolve(data, np.ones(window_size) / window_size, mode='valid')

# 绘制原始数据和移动平均曲线
plt.figure(figsize=(10, 6))
plt.plot(data, label="原始数据", marker='o', color='blue')
plt.plot(np.arange(window_size - 1, len(data)), sma, label="移动平均", color='red')
plt.legend()
plt.title("简单移动平均示例")
plt.xlabel("数据点")
plt.ylabel("数值")
plt.grid(True)
plt.show()


if __name__ == "__main__":
    pass