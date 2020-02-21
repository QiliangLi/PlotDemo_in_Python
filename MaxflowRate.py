import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import random

def plotNodeNumcase(filePath, nodeNumList, K, savePath):
    # 绘图初始化
    fig, ax = plt.subplots(figsize=(8, 4))

    file = pd.read_csv(filePath)
    maxflowList=[]
    srRatioList=[]
    maxflowRateList=[]

    for i in range(len(nodeNumList)):
        nodeNum=nodeNumList[i]
        df=file[file["nodeNum"].isin([nodeNum])]
        srRatioList = df["ratio"]
        maxflowList = df["sourceGraphMaxflow"]
        for f in maxflowList:
            maxflowRateList.append(f/(K*(nodeNum-1)))

    plt.xlabel('Batch No')
    plt.ylabel('Ratio')

    """set interval for y label"""
    yticks = []
    tmp = 0.85
    while tmp <= 1.025:
        yticks.append(tmp)
        tmp += 0.025

    xticks = range(0, 100, 5)
    ax.set_xticks(xticks)
    ax.set_yticks(yticks)

    """set min and max value for axes"""
    ax.set_ylim([0.85, 1.019])
    ax.set_xlim([0, 100])
    # figTitle='K=10, M=4, Gains=100, RepeatTimes=10'
    figTitle = 'K=10, M=4, nodeNum=101'
    ax.set_title(figTitle)

    x = [i for i in range(0, 100)]
    plt.plot(x, maxflowRateList, "x-", label="Source Maxflow Rate")
    plt.plot(x, srRatioList, "+-", label="Repair Parallel Rate")

    """open the grid"""
    plt.grid(False)
    plt.legend(loc=4)

    plt.savefig(savePath, dpi=600, format="pdf")

    plt.show()


if __name__=="__main__":
    filePath=r"F:\Coding\Java\SimulateSR\result\fullbatch-result-K=10-M=4-gains=100.0.csv"
    nodeNumList=[101]
    plotNodeNumcase(filePath, nodeNumList, 10, "Source Maxflow Rate-Repair Parallel Rate-K=10-M=4-nodeNum=101.pdf")