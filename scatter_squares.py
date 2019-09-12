import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

# plt.scatter(x_values, y_values, s=40)
# plt.scatter(x_values, y_values, c='red', edgecolor='none', s=40)
# plt.scatter(x_values, y_values, c=(0, 0, 0.8), edgecolor='none', s=40)

# 根据y值大小，呈现不同的“深度”蓝色
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolor='none', s=40)


# 设置图表标题并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
# 设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=14)

# 设置每个坐标轴的取值范围
plt.axis([0, 1100, 0, 1100000])

# plt.show()
# 保存图片
plt.savefig('squares_plot.png', bbox_inches='tight')  # 第二个实参指定将图表多余的空白区域裁剪掉。

