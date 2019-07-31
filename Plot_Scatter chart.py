import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
font_set = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=15)#导入宋体字体文件

# 散点图
x = [1,2,3,4,5,6,7,8,9]
y = [0,2,3,4,2,3,4,5,4]
plt.scatter(x,y)
# plt.scatter(x, y,c="g", alpha=0.5, marker=r'$\clubsuit$',label="Luck")
plt.show()
