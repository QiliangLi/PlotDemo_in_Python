import scipy.io
import numpy as np
import matplotlib.pylab as pylab
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
params={
    'axes.labelsize': '35',
    'xtick.labelsize':'27',
    'ytick.labelsize':'27',
    'lines.linewidth':2 ,
    'legend.fontsize': '27',
    'figure.figsize': '24, 9'
}
pylab.rcParams.update(params)


y1 = [9.79,7.25,7.24,4.78,4.20]
y2 = [5.88,4.55,4.25,3.78,3.92]
y3 = [4.69,4.04,3.84,3.85,4.0]
y4 = [4.45,3.96,3.82,3.80,3.79]
y5 = [3.82,3.89,3.89,3.78,3.77]



ind = np.arange(5)                # the x locations for the groups
width = 0.15
plt.bar(ind,y1,width,color = 'blue',label = 'm=2')
plt.bar(ind+width,y2,width,color = 'g',label = 'm=4') # ind+width adjusts the left start location of the bar.
plt.bar(ind+2*width,y3,width,color = 'c',label = 'm=6')
plt.bar(ind+3*width,y4,width,color = 'r',label = 'm=8')
plt.bar(ind+4*width,y5,width,color = 'm',label = 'm=10')
plt.xticks(np.arange(5) + 2.5*width, ('10%','15%','20%','25%','30%'))

plt.xlabel('Sample percentage')
plt.ylabel('Error rate')

fmt = '%.0f%%' # Format you want the ticks, e.g. '40%'
xticks = mtick.FormatStrFormatter(fmt)
# Set the formatter
axes = plt.gca()   # get current axes
axes.yaxis.set_major_formatter(xticks) # set % format to ystick.
axes.grid(True)
plt.legend(loc="upper right")
# plt.savefig('D:\\errorRate.eps', format='eps',dpi = 1000,bbox_inches='tight')

plt.show()