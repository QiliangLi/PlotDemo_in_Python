import matplotlib.pyplot as plt

migtime = [16.6, 16.5, 16.9, 17.1, 17.2, 18.1, 18.2, 18.4, 19.4, 19.3, 20.4, 20.3, 22, 21.7, 22]
delay = [108, 98, 92, 83, 87, 77, 85, 48, 31, 58, 35, 43, 36, 31, 19]

fig, ax = plt.subplots()

plt.xlabel('migration speed (MB/s)')
plt.ylabel('migration time (s); request delay (ms)')

"""set interval for y label"""
yticks = range(10, 110, 10)
ax.set_yticks(yticks)

"""set min and max value for axes"""
ax.set_ylim([10, 110])
ax.set_xlim([58, 42])

x = [57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43]
plt.plot(x, migtime, "x-", label="migration time")
plt.plot(x, delay, "+-", label="request delay")

"""open the grid"""
plt.grid(True)

plt.legend(bbox_to_anchor=(1.0, 1), loc=1, borderaxespad=0.)

plt.show()