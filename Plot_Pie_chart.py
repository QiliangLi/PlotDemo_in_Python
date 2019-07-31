import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
font_set = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=15)#导入宋体字体文件

# 饼图
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']
#解决中文不显示，pie没有FontProperties属性，不能使用上面的方法

labels = ("红","绿","蓝","黄","灰")
colors = ("red","green","blue","yellow","gray")
fracs = [10,20,30,20,20]

plt.pie(fracs,labels=labels,colors=colors,autopct='%1.0f%%')
plt.show()
