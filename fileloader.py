import pandas as pd
from scipy.stats import pearsonr
import os
# Read the file
outfile = pd.read_excel('/Users/yiwengeng/Documents/PregnantPrj/Data/PLT_stats.xlsx',sheet_name='Summary')
outfile.set_index(keys='SubjectID',append=True,inplace=True) # Set the index

# define all the variables
folder = '/Users/yiwengeng/Documents/PregnantPrj/Data/'
# dirlist = ["PTL01","PTL02","PTL03","PTL05","PTL06","PTL07","PTL09","PTL10","PTL15"]
dirlist = ["PTL01","PTL02","PTL03","PTL05","PTL06","PTL07","PTL09","PTL10","PTL11","PTL12","PTL13","PTL14","PTL15","PTL16","PTL17","PTL18"]#["PTL01","PTL02","PTL03","PTL05","PTL06","PTL07","PTL09","PTL10","PTL15"]
act_names=["activity_score", "score_meet_daily_targets","score_move_every_hour","score_stay_active","steps"]
hr_names=["bpm"]
spo2_names=["spo2"]
hrhrv_names=["5min_hr","5min_hrv"]
ready_names=["readiness_score", "score_previous_night","score_sleep_balance", 
             "score_previous_day","score_activity_balance","score_resting_hr",
             "score_hrv_balance","score_recovery_index","score_temperature"]
sleep_names=["sleep_score", "duration","efficiency","onset_latency","rmssd",
             "score_deep","score_efficiency","score_rem"]

# Loop through all the files
for dir in dirlist:
    ID = int(dir[-2:])-1
    os.chdir(folder+dir)
    files = sorted(os.listdir())

    # activity
    df_act = pd.read_csv(files[0])
    df_act.rename(columns={'score':'activity_score'},inplace=True)
    for name in act_names:
        avg_name = "Avg_" + name
        std_name = "Std_" + name
        outfile.loc[ID,avg_name] = "{:.2f}".format(df_act[name].mean())
        outfile.loc[ID,std_name] = "{:.2f}".format(df_act[name].std())

    # sleep
    df_sleep = pd.read_csv(files[7])
    df_sleep.rename(columns={'score':'sleep_score'},inplace=True)
    for name in sleep_names:
        avg_name = "Avg_" + name
        std_name = "Std_" + name
        outfile.loc[ID,avg_name] = "{:.2f}".format(df_sleep[name].mean())
        outfile.loc[ID,std_name] = "{:.2f}".format(df_sleep[name].std())
    # readiness
    df_ready = pd.read_csv(files[5])
    df_ready.rename(columns={'score':'readiness_score'},inplace=True)
    for name in ready_names:
        avg_name = "Avg_" + name
        std_name = "Std_" + name
        outfile.loc[ID,avg_name] = "{:.2f}".format(df_ready[name].mean())
        outfile.loc[ID,std_name] = "{:.2f}".format(df_ready[name].std())
    # daily_hr
    df_hr = pd.read_csv(files[1])
    for name in hr_names:
        avg_name = "Avg_" + name
        std_name = "Std_" + name
        outfile.loc[ID,avg_name] = "{:.2f}".format(df_hr[name].mean())
        outfile.loc[ID,std_name] = "{:.2f}".format(df_hr[name].std())
    # hr_hrv
    df_hrhrv = pd.read_csv(files[3])
    df_hrhrv.rename(columns={'5-min hr':'5min_hr','5-min hrv':'5min_hrv'},inplace=True)
    for name in hrhrv_names:
        avg_name = "Avg_" + name
        std_name = "Std_" + name
        outfile.loc[ID,avg_name] = "{:.2f}".format(df_hrhrv[name].mean())
        outfile.loc[ID,std_name] = "{:.2f}".format(df_hrhrv[name].std())
    # spo2
    df_spo2 = pd.read_csv(files[2])
    df_spo2.rename(columns={'average spo2':'spo2'},inplace=True)
    for name in spo2_names:
        avg_name = "Avg_" + name
        std_name = "Std_" + name
        outfile.loc[ID,avg_name] = "{:.2f}".format(df_spo2[name].mean())
        outfile.loc[ID,std_name] = "{:.2f}".format(df_spo2[name].std())

outfile.to_excel('/Users/yiwengeng/Documents/PregnantPrj/Data/PLT_stats_out.xlsx', sheet_name='Summary')
# print(outfile.keys())