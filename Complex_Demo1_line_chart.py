import matplotlib.pyplot as plt
import matplotlib.pylab as pylab
import scipy.io
import numpy as np

params = {
    'axes.labelsize': '35',
    'xtick.labelsize': '27',
    'ytick.labelsize': '27',
    'lines.linewidth': 2,
    'legend.fontsize': '27',
    'figure.figsize': '12, 9'  # set figure size
}
pylab.rcParams.update(params)  # set figure parameter
# line_styles=['ro-','b^-','gs-','ro--','b^--','gs--']  #set line style


# We give the coordinate date directly to give an example.
x1 = [-20, -15, -10, -5, 0, 0, 5, 10, 15, 20]
y1 = [0, 0.04, 0.1, 0.21, 0.39, 0.74, 0.78, 0.80, 0.82, 0.85]
y2 = [0, 0.014, 0.03, 0.16, 0.37, 0.78, 0.81, 0.83, 0.86, 0.92]
y3 = [0, 0.001, 0.02, 0.14, 0.34, 0.77, 0.82, 0.85, 0.90, 0.96]
y4 = [0, 0, 0.02, 0.12, 0.32, 0.77, 0.83, 0.87, 0.93, 0.98]
y5 = [0, 0, 0.02, 0.11, 0.32, 0.77, 0.82, 0.90, 0.95, 1]

plt.plot(x1, y1, 'bo-', label='m=2, p=10%',
         markersize=20)  # in 'bo-', b is blue, o is O marker, - is solid line and so on
plt.plot(x1, y2, 'gv-', label='m=4, p=10%', markersize=20)
plt.plot(x1, y3, 'ys-', label='m=6, p=10%', markersize=20)
plt.plot(x1, y4, 'ch-', label='m=8, p=10%', markersize=20)
plt.plot(x1, y5, 'mD-', label='m=10, p=10%', markersize=20)

fig1 = plt.figure(1)
axes = plt.subplot(111)
# axes = plt.gca()
axes.set_yticks([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
axes.grid(True)  # add grid

plt.legend(loc="lower right")  # set legend location
plt.ylabel('Percentage')  # set ystick label
plt.xlabel('Difference')  # set xstck label

# plt.savefig('D:\\commonNeighbors_CDF_snapshots.eps', dpi=1000, bbox_inches='tight')
plt.show()