import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams

# 设置字体
rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 数据
x = [0.3, 0.2, 0.15, 0.12, 0.1, 0.08, 0.05]
y = [44, 32, 23, 19, 16, 14, 11]

# 拟合直线
coefficients = np.polyfit(x, y, 1)
polynomial = np.poly1d(coefficients)
xs = np.linspace(min(x), max(x), 100)
ys = polynomial(xs)

# 绘图
plt.figure(figsize=(8, 6))
plt.scatter(x, y, color='blue')
plt.plot(xs, ys, color='red', linestyle='-', linewidth=2)
plt.title('糖浓度 vs 旋转角度')
plt.xlabel('糖浓度(g/cm^3)')
plt.ylabel('旋转角度(°)')
plt.legend()
plt.grid(True)
plt.savefig('糖浓度 vs 旋转角度.png')
plt.show()