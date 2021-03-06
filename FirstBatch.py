import matplotlib.pyplot as plt
import pandas as pd

avgRatio1 = []
avgRatio2 = []
avgRatio3 = []
randRatio1 = []
randRatio2 = []
randRatio3 = []

avgFile=pd.read_csv(r"F:\Coding\Java\SimulateSR\result\avg-result-K=3-M=2-gains=100.0.csv")
for ratio in avgFile["RatioAvg"]:
    avgRatio1.append(ratio)

randFile=pd.read_csv(r"F:\Coding\Java\SimulateSR\result\rand-avg-result-K=3-M=2-gains=100.0-repeatTimes=10.csv")
for ratio in randFile["RatioAvg"]:
    randRatio1.append(ratio)

avgFile=pd.read_csv(r"F:\Coding\Java\SimulateSR\result\avg-result-K=6-M=3-gains=100.0.csv")
for ratio in avgFile["RatioAvg"]:
    avgRatio2.append(ratio)

randFile=pd.read_csv(r"F:\Coding\Java\SimulateSR\result\rand-avg-result-K=6-M=3-gains=100.0-repeatTimes=10.csv")
for ratio in randFile["RatioAvg"]:
    randRatio2.append(ratio)

avgFile=pd.read_csv(r"F:\Coding\Java\SimulateSR\result\avg-result-K=10-M=4-gains=100.0.csv")
for ratio in avgFile["RatioAvg"]:
    avgRatio3.append(ratio)

randFile=pd.read_csv(r"F:\Coding\Java\SimulateSR\result\rand-avg-result-K=10-M=4-gains=100.0-repeatTimes=10.csv")
for ratio in randFile["RatioAvg"]:
    randRatio3.append(ratio)

fig, ax = plt.subplots(figsize=(10, 4))

plt.xlabel('Node Number')
plt.ylabel('Parallel Rate Ratio')

"""set interval for y label"""
yticks=[]
tmp=0.4
while tmp<=1.05:
    yticks.append(tmp)
    tmp+=0.05

xticks=range(21, 202, 10)
ax.set_xticks(xticks)
ax.set_yticks(yticks)

"""set min and max value for axes"""
ax.set_ylim([0.4, 1.05])
ax.set_xlim([21, 201])
# figTitle='K=10, M=4, Gains=100, RepeatTimes=10'
figTitle='Gains=100, RepeatTimes=10'
ax.set_title(figTitle)

x = [i for i in range(21, 202, 10)]
plt.plot(x, avgRatio1, "rx-", label="SR-3+2 Ratio")
plt.plot(x, randRatio1, "r+-", label="Rand-3+2 Ratio")
plt.plot(x, avgRatio2, "bx-", label="SR-6+3 Ratio")
plt.plot(x, randRatio2, "b+-", label="Rand-6+3 Ratio")
plt.plot(x, avgRatio3, "gx-", label="SR-10+4 Ratio")
plt.plot(x, randRatio3, "g+-", label="Rand-10+4 Ratio")

"""open the grid"""
plt.grid(False)

#plt.legend(bbox_to_anchor=(1.0, 1), loc=4, borderaxespad=0.)
plt.legend(loc=4)

plt.savefig("First Batch "+figTitle+".pdf", dpi=600, format="pdf")

plt.show()