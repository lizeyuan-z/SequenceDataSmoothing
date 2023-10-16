import numpy as np
import matplotlib.pyplot as plt
import warnings


warnings.filterwarnings("ignore")
plt.rcParams['font.sans-serif'] = ['STSong']


# 生成示例数据
data = np.array([10, 15, 12, 18, 20, 14, 16, 22, 19, 25])

# 定义平滑参数（通常称为平滑因子）
alpha = 0.2

# 计算EMA
ema = [data[0]]  # 初始EMA值等于第一个数据点
for i in range(1, len(data)):
    ema.append(alpha * data[i] + (1 - alpha) * ema[-1])

# 绘制原始数据和EMA曲线
plt.figure(figsize=(10, 6))
plt.plot(data, label="原始数据", marker='o', color='blue')
plt.plot(ema, label="EMA", color='red')
plt.legend()
plt.title("指数加权移动平均（EMA）示例")
plt.xlabel("数据点")
plt.ylabel("数值")
plt.grid(True)
plt.show()


if __name__ == "__main__":
    pass
