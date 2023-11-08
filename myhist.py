
import pandas as pd
from scipy.stats import pearsonr
import os
import matplotlib.pyplot as plt
from matplotlib.dates import AutoDateLocator, DateFormatter
from datetime import datetime
import seaborn as sns
import numpy as np
import matplotlib.patches as mpatches

def my_hist(data,column,xlable,left,right,marker):
    fig,ax1 = plt.subplots(figsize=(15, 5))
    custom_palette = {0: "tab:blue", 1: "tab:orange"}
    sns.histplot(data=data, x=column, hue=marker, palette=custom_palette, multiple="dodge", kde=True, line_kws={'linewidth': 3}, ax=ax1, bins=40, alpha=0.3)
    # ax1.legend(['w/o Trama','w/ Trama'],fontsize=20)
    # cualculate the mean and std of each group
    dfg = data.groupby(marker)
    no_trama_mean = dfg[column].mean()[0]
    trama_mean = dfg[column].mean()[1]
    no_trama_std = dfg[column].std()[0]
    trama_std = dfg[column].std()[1]
    
    # cound the number of each group
    no_trama_count = len(data.loc[data[marker]==0])
    trama_count = len(data.loc[data[marker]==1])
    print("no_trama_count: ",no_trama_count)
    print("trama_count: ",trama_count)
    print(len(data))
    # find the count of each group where the value is smaller than 50 and larger than 100
    

    no_trama_less = len(data.loc[(data[marker]==0) & (data[column]<left)])
    trama_less = len(data.loc[(data[marker]==1) & (data[column]<left)])
    no_trama_more = len(data.loc[(data[marker]==0) & (data[column]>right)])
    trama_more = len(data.loc[(data[marker]==1) & (data[column]>right)])
    no_trama_percent = (no_trama_less+no_trama_more)/no_trama_count
    trama_percent = (trama_less+trama_more)/trama_count

    print("no_trama_count: ",no_trama_count,no_trama_less,no_trama_more ,no_trama_percent)
    print("trama_count: ",trama_count, trama_less,trama_more,trama_percent)

    print("no_trama_mean: ",no_trama_mean)
    print("trama_mean: ",trama_mean)
    print("no_trama_std: ",no_trama_std)
    print("trama_std: ",trama_std)
    # print(dfg['bpm'].mean()[0])
    # plot the mean and std
    ax1.axvline(x=no_trama_mean, color="tab:blue", linestyle='dashed', linewidth=3)
    ax1.axvline(x=no_trama_mean-no_trama_std, color="tab:blue", linestyle='dotted', linewidth=2)
    ax1.axvline(x=no_trama_mean+no_trama_std, color="tab:blue", linestyle='dotted', linewidth=2)
    ax1.axvline(x=trama_mean, color="tab:orange", linestyle='dashed', linewidth=3)
    ax1.axvline(x=trama_mean-trama_std, color="tab:orange", linestyle='dotted', linewidth=2)
    ax1.axvline(x=trama_mean+trama_std, color="tab:orange", linestyle='dotted', linewidth=2)
    # ax1.axvline(x=left, color='black', linestyle=':', linewidth=3)
    # ax1.axvline(x=right, color='black', linestyle=':', linewidth=3)
    ax1.set_xticklabels(ax1.get_xticks(), fontsize=18)
    ax1.set_yticklabels(ax1.get_yticks(), fontsize=18)
    # ax1.grid()
    ax1.set_xlabel(xlable,fontsize=18)
    # ax1.set_xlim(40, 3000)
    ax1.set_ylabel('Count',fontsize=18)
    plt.savefig('/Users/yiwengeng/Documents/PregnantPrj/Code/Fig/'+marker+'_'+xlable+'.png', dpi=300)  # Save with a dpi of 300
