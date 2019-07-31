import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
font_set = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=15)#导入宋体字体文件
import numpy as np
#标签
labels = np.array(['进攻','防御','生存','补刀','魔法'])
#数据个数
dataLenth = 5
#数据
data = np.array([2,4,3,5,1])

angles = np.linspace(0, 2*np.pi, dataLenth, endpoint=False)
# linspace创建等差数列 0到2pi之间dataLength个数据
# 第二个数据是否是最后的数据，默认为True
data = np.concatenate((data, [data[0]])) # 闭合
# 加入第一个数据，闭合

angles = np.concatenate((angles, [angles[0]])) # 闭合
# 角度也闭合

fig = plt.figure()
ax = fig.add_subplot(111, polar=True)# polar参数！！
# 111表示1行1列处于第1个，polar设为极坐标

ax.plot(angles, data, 'bo-', linewidth=2)# 画线
ax.fill(angles, data, facecolor='b', alpha=0.25)# 填充
ax.set_thetagrids(angles * 180/np.pi, labels, fontproperties=font_set)
ax.set_title("能力图", va='bottom', fontproperties=font_set)
ax.set_rlim(0,5)
ax.grid(True)
plt.show()
