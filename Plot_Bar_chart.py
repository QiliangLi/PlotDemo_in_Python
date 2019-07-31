import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
font_set = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=15)#导入宋体字体文件

# 条形图
x = [0,1,2,4,5,6]
y = [1,2,3,2.1,4,1]
plt.bar(x,y)#竖的条形图
#plt.barh(x,y)#横的条形图，注意x,y坐标
plt.title("条形图",FontProperties=font_set);
plt.xlabel("x轴",FontProperties=font_set);
plt.ylabel("y轴",FontProperties=font_set);
plt.show()
