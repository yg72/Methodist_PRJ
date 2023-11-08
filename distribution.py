import pandas as pd
from scipy.stats import pearsonr
import os
import matplotlib.pyplot as plt
from matplotlib.dates import AutoDateLocator, DateFormatter
from datetime import datetime
import seaborn as sns
import numpy as np
import matplotlib.patches as mpatches
from myhist import my_hist
folder = '/Users/yiwengeng/Documents/PregnantPrj/Data/PTL_Data/'
dirlist = ["PTL01","PTL02","PTL03","PTL05","PTL06","PTL07","PTL09","PTL10","PTL11","PTL12","PTL13","PTL14","PTL15","PTL16","PTL17"]
# dirlist = ["PTL02","PTL03"]
act_names=["activity_score", "score_meet_daily_targets","score_move_every_hour","score_stay_active","steps"]
hr_names=["bpm"]
spo2_names=["spo2"]
hrhrv_names=["5min_hr","5min_hrv"]
ready_names=["readiness_score", "score_previous_night","score_sleep_balance", 
             "score_previous_day","score_activity_balance","score_resting_hr",
             "score_hrv_balance","score_recovery_index","score_temperature"]
sleep_names=["sleep_score", "duration","efficiency","onset_latency","rmssd",
             "score_deep","score_efficiency","score_rem"]

df_act = {}
df_sleep = {}
df_ready = {}
df_hr = {}
df_hrhrv = {}
df_spo2 = {}

marker_L = [ "eACEScore"," cEmotAbuse"," cPhysAbuse"," cSexAbuse"," cEmoNeglect"," cPhysNeglect"," cDV"," cHSA"," cHMI"," cPSD"," cIHM"," eWV"," eFD"," eANE"," eBullied"," eFOSTER"]
for marker in marker_L:
# plot the histogram of 5min_hr
    print(marker,"*"*20,"\n")
    print("steps")
    if marker == 'eACEScore':
        healthy = [1,2,3,9,10,11,12,13,14,15,17,18]
        unhealthy = [5,6,7,16] 
    elif marker == 'cEmotAbuse':
        healthy = [1,2,3,8,9,10,12,13,14,15,18]
        unhealthy = [4,5,6,7,11,16,17]
    elif marker == 'cPhysAbuse':
        healthy = [1,2,3,6,8,9,10,12,13,15,16,18]
        unhealthy = [4,5,7,11,14,17]  
    elif marker == 'cSexAbuse':
        healthy = [1,2,3,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
        unhealthy = [4]
    elif marker == 'cEmoNeglect':
        healthy = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
        unhealthy = []
    elif marker == 'cPhysNeglect':
        healthy = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
        unhealthy = []
    elif marker == 'cDV':
        healthy = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
        unhealthy = []
    elif marker == 'cHSA':
        healthy = [1,2,3,4,5,6,8,9,10,11,12,13,15,16,17,18]
        unhealthy = [7,14]
    elif marker == 'cHMI':
        healthy = [1,2,4,5,7,8,9,10,11,12,13,14,15,17,18]
        unhealthy = [3,6,16]
    elif marker == 'cPSD':
        healthy = [1,2,4,6,7,8,9,10,11,12,13,14,15,16,17,18]
        unhealthy = [3,5]
    elif marker == 'cIHM':
        healthy = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
        unhealthy = []
    elif marker == 'eWV':
        healthy = [1,2,3,4,5,7,8,9,10,12,13,14,15,16,17,18]
        unhealthy = [6,11]
    elif marker == 'eFD':
        healthy = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,17,18]
        unhealthy = [16]
    elif marker == 'eANE':
        healthy = [1,2,5,8,9,10,11,12,13,14,15,16,17,18]
        unhealthy = [3,4,6,7]
    elif marker == 'eBullied':
        healthy = [1,2,3,4,6,7,8,9,10,11,12,13,14,15,16,17,18]
        unhealthy = [5]
    elif marker == 'eFOSTER':
        healthy = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,17,18]
        unhealthy = [16]

    for dir in dirlist:
        ID = int(dir[-2:])
        os.chdir(folder+dir)
        files = sorted(os.listdir())
        # print("ID",ID)
        # activity
        df_act[ID] = pd.read_csv(files[0], parse_dates = [0])
        df_act[ID].rename(columns={'score':'activity_score'},inplace=True)
        df_act[ID]['ID'] =  ID
        df_act[ID][marker] = 0 if ID in healthy else 1 if ID in unhealthy else None
        # print('act',len(df_act[ID]))

        # sleep
        df_sleep[ID] = pd.read_csv(files[7], parse_dates = [0])
        df_sleep[ID].rename(columns={'score':'sleep_score'},inplace=True)
        df_sleep[ID]['ID'] =  ID
        df_sleep[ID][marker] = 0 if ID in healthy else 1 if ID in unhealthy else None
        # print('sleep',len(df_sleep[ID]))
        # readiness
        df_ready[ID] = pd.read_csv(files[5], parse_dates = [0])
        df_ready[ID].rename(columns={'score':'readiness_score'},inplace=True)
        df_ready[ID]['ID'] =  ID
        df_ready[ID][marker] = 0 if ID in healthy else 1 if ID in unhealthy else None
        # print('ready',len(df_ready[ID]))

        # daily_hr
        df_hr[ID] = pd.read_csv(files[1], parse_dates = [0])
        df_hr[ID]['ID'] =  ID
        df_hr[ID][marker] = 0 if ID in healthy else 1 if ID in unhealthy else None    
        # print('hr',len(df_hr[ID]))

        # hr_hrv
        df_hrhrv[ID] = pd.read_csv(files[3], parse_dates = [0])
        df_hrhrv[ID].rename(columns={'5-min hr':'5min_hr','5-min hrv':'5min_hrv'},inplace=True)
        df_hrhrv[ID]['ID'] =  ID
        df_hrhrv[ID][marker] = 0 if ID in healthy else 1 if ID in unhealthy else None   
        df_hrhrv[ID] = df_hrhrv[ID].loc[df_hrhrv[ID]['5min_hr'] != 0]
        df_hrhrv[ID]['timestamp'] = pd.to_datetime(df_hrhrv[ID]['timestamp'], utc=True)
        df_hrhrv[ID]['days_from_start'] = (df_hrhrv[ID]['timestamp'] - df_hrhrv[ID]['timestamp'].min()).dt.days
        df_hrhrv[ID]['Date'] = pd.to_datetime(df_hrhrv[ID]['timestamp'].dt.date, utc=True)

        # print("hrhrv",len(df_hrhrv[ID]))

        # spo2
        df_spo2[ID] = pd.read_csv(files[2], parse_dates = [0])
        df_spo2[ID].rename(columns={'average spo2':'spo2'},inplace=True)
        df_spo2[ID]['ID'] =  ID
        df_spo2[ID][marker] = 0 if ID in healthy else 1 if ID in unhealthy else None    
        # print('spo2',len(df_spo2[ID]))

        # print("*"*20)  
        
    # combine all dataframes
    df_act_all = pd.concat([df_act[int(dir[-2:])] for dir in dirlist], axis=0,ignore_index=True)
    print("df_act_all: ",len(df_act_all))
    df_sleep_all = pd.concat([df_sleep[int(dir[-2:])] for dir in dirlist], axis=0,ignore_index=True)
    print("df_sleep_all: ",len(df_sleep_all))
    df_ready_all = pd.concat([df_ready[int(dir[-2:])] for dir in dirlist], axis=0,ignore_index=True)
    print("df_ready_all: ",len(df_ready_all))
    df_hr_all = pd.concat([df_hr[int(dir[-2:])] for dir in dirlist],ignore_index=True)
    print("df_hr_all: ",len(df_hr_all))
    df_hrhrv_all = pd.concat([df_hrhrv[int(dir[-2:])] for dir in dirlist],ignore_index=True)
    print("df_hrhrv_all: ",len(df_hrhrv_all))
    df_spo2_all = pd.concat([df_spo2[int(dir[-2:])] for dir in dirlist],ignore_index=True)
    print("df_spo2_all: ",len(df_spo2_all))

    
    my_hist(df_act_all,'steps','steps',left=71, right=71,marker=marker)

    