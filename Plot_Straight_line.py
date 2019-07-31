import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
font_set = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=15)#导入宋体字体文件

dataX = [1,2,3,4]
dataY = [1,2,3,1]
plt.plot(dataX,dataY)#plot还有很多参数，可以查API修改，如颜色，虚线等
plt.title("绘制直线",FontProperties=font_set);
plt.xlabel("x轴",FontProperties=font_set);
plt.ylabel("y轴",FontProperties=font_set);
plt.show()
