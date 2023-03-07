import matplotlib.pyplot as plt
import numpy as np

# 创建数据
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
y = np.array([3, 5, 7, 9, 11, 13, 15, 17, 19])

# 绘制趋势线
z = np.polyfit(x, y, 1)
p = np.poly1d(z)
plt.plot(x, p(x), "r--")

# 绘制散点图
plt.scatter(x, y)

# 添加标题和标签
plt.title("Trend Chart")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

# 显示图表
plt.show()
