# pip install statsmodels

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import ExponentialSmoothing
import warnings


warnings.filterwarnings("ignore")
plt.rcParams['font.sans-serif'] = ['STSong']


# 生成示例时间序列数据
np.random.seed(0)
n = 100
index = pd.date_range(start="2022-01-01", periods=n, freq="D")
data = np.sin(np.linspace(0, 4 * np.pi, n)) + np.random.normal(0, 0.2, n)
time_series = pd.Series(data, index=index)

# 执行指数平滑
model = ExponentialSmoothing(time_series, trend='add', seasonal='add', seasonal_periods=7)
results = model.fit()

# 生成平滑后的数据和预测
smoothed = results.fittedvalues
forecast = results.forecast(steps=30)  # 预测未来30个时间点

# 绘制原始数据、平滑后的数据和预测
plt.figure(figsize=(10, 6))
plt.plot(time_series, label="原始数据", color='blue', alpha=0.6)
plt.plot(smoothed, label="指数平滑", color='red')
plt.plot(forecast, label="未来预测", color='green')
plt.legend()
plt.title("指数平滑示例")
plt.xlabel("时间")
plt.ylabel("数据值")
plt.grid(True)
plt.show()


if __name__ == "__main__":
    pass
