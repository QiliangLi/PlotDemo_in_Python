import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import random

def plotNodeNumcase(filePath, nodeNumList, savePath):
    # 绘图初始化
    fig, ax = plt.subplots(figsize=(10, 4))

    colorList=["r","g","b","c","m","y","k"]

    file = pd.read_csv(filePath)

    for i in range(len(nodeNumList)):
        nodeNum=nodeNumList[i]
        df=file[file["nodeNum"].isin([nodeNum])]
        srRatioList = df["ratio"]
        randRatioList = df["randRatio"]

        # plot the cumulative histogram
        n, bins, patches = ax.hist(srRatioList, 50, normed=True, histtype='step',color=colorList[i],
                                   cumulative=True, label='SR-'+str(nodeNum))
        n, bins, patches = ax.hist(randRatioList, 50, normed=True, histtype='step',color=colorList[i],
                                   cumulative=True, label='Rand-'+str(nodeNum))

    # tidy up the figure
    ax.grid(False)
    ax.legend(loc='best')
    ax.set_title('Cumulative Ratio')
    ax.set_xlabel('Ratio')
    ax.set_ylabel('Likelihood of occurrence')

    plt.savefig(savePath, dpi=600, format="pdf")

    plt.show()


if __name__=="__main__":
    filePath=r"F:\Coding\Java\SimulateSR\result\fullbatch-result-K=10-M=4-gains=100.0.csv"
    nodeNumList=[101,401,701,1001]
    plotNodeNumcase(filePath, nodeNumList, "fullbatch-result-K=10-M=4-gains=100.0.pdf")