import matplotlib.pyplot as plt
import pandas as pd

avgRatio = []
randRatio = []

avgFile=pd.read_csv(r"F:\Coding\Java\SimulateSR\result\avg-result-K=10-M=4-gains=100.0.csv")
for ratio in avgFile["RatioAvg"]:
    avgRatio.append(ratio)

randFile=pd.read_csv(r"F:\Coding\Java\SimulateSR\result\rand-avg-result-K=10-M=4-gains=100.0-repeatTimes=10.csv")
for ratio in randFile["RatioAvg"]:
    randRatio.append(ratio)

fig, ax = plt.subplots(figsize=(10, 4))

plt.xlabel('Node Number')
plt.ylabel('Parallel Rate Ratio')

"""set interval for y label"""
xticks=range(21, 202, 10)
ax.set_xticks(xticks)

"""set min and max value for axes"""
ax.set_ylim([0, 1.1])
ax.set_xlim([21, 201])
figTitle='K=10, M=4, Gains=100, RepeatTimes=10'
ax.set_title(figTitle)

x = [i for i in range(21, 202, 10)]
plt.plot(x, avgRatio, "x-", label="SR Ratio")
plt.plot(x, randRatio, "+-", label="Rand Ratio")

"""open the grid"""
plt.grid(False)

#plt.legend(bbox_to_anchor=(1.0, 1), loc=4, borderaxespad=0.)
plt.legend(loc=4)

plt.savefig("First Batch "+figTitle+".pdf", dpi=600, format="pdf")

plt.show()