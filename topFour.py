"""
Vikulp Sharma
SB 314 Post Grind Study
"""
import pandas as pd
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from datetime import datetime, date
import seaborn as sns
from collections import Counter
from pandas import Series
from pylab import figure, axes, pie, title, show
from functools import partial
from datetime import timedelta
import math
import pylab


# reading 314 Compliance Data and Snapshot Data for All GENx PIP2 Engines
grindData=pd.read_csv("C:/Users/307006397/Desktop/F&B_Priority/Post_Grind_fanV/sb_72-0314.csv")
snapShotData=pd.read_csv("C:/Users/307006397/Desktop/F&B_Priority/Post_Grind_fanV/vib_data_1B_PIP2.csv")
########################################################
##########    Take Off Forward  ############################
########################################################
snapShotDataTo = snapShotData[pd.notnull(snapShotData['cr_zvb1r_smoothed'])]
#snapShotDataToSort=snapShotDataTo.sort(['serlzd_eng_ser_num','best_datetime'])
#snapShotDataToSortUn=snapShotDataToSort.serlzd_eng_ser_num.unique()
snapShotDataTo['best_datetime'] = pd.to_datetime(snapShotDataTo['best_datetime'])
snapShotDataTo=snapShotDataTo.sort(['serlzd_eng_ser_num','best_datetime'])
grindData['Compliance Date'] = pd.to_datetime(grindData['Compliance Date'])
ESN = []
maxPreGrind=[]
minPreGrind=[]
maxPostGrind=[]
minPostGrind=[]
meanPreGrind=[]
meanPostGrind=[]

i=956172
xx=snapShotDataTo.loc[snapShotDataTo['serlzd_eng_ser_num'] == i]
takeOffData=xx.ix[:,["best_datetime","cr_zvb1r_smoothed"]]

uu=grindData.loc[grindData['Engine Serial Number'] == i]
uu = uu[pd.notnull(uu['Compliance Date'])]

#if uu.empty:
#   print('DataFrame is empty!')
vv=uu['Compliance Date']
#    vv=vv.to_string()
vv=vv.iloc[0]

#    vv=datetime.strptime(vv, '%m/%d/%y')
#    vv['Compliance Date'] = pd.to_datetime(vv['Compliance Date'])
postGrind=takeOffData.loc[takeOffData['best_datetime'] >= vv]
preGrind=takeOffData.loc[takeOffData['best_datetime'] < vv]
#postGrind=postGrind['tk_zvb1f_smoothed']
#preGrind=preGrind['tk_zvb1f_smoothed']
x = postGrind['best_datetime']
y=postGrind['cr_zvb1r_smoothed']
x1 = preGrind['best_datetime']
y1=preGrind['cr_zvb1r_smoothed']

plt.xlabel('Time')
plt.ylabel('Fan Cruise Vibration Parameter')
plt.title('Second High Time Engine pre/post Grinding')
pylab.plot(x,y, '-b', label='PostGrind cr_zvb1r_smoothed')
pylab.plot(x1,y1,'-r', label='PreGrind cr_zvb1r_smoothed')
pylab.legend(loc='upper left')
plt.show()
plt.savefig('C:/Users/307006397/Desktop/F&B_Priority/Post_Grind_fanV/cruiseR.png',bbox_inches = 'tight')   ### Update

#plt.figure();
#postGrind.plot()
#plt.gcf().autofmt_xdate()
#
#plt.show()
#
#result = postGrind
#result.columns=["best_datetime","tk_zvb1f_smoothed"]
#result.plot(kind='line',title='Fan Module 2016 Full Year', align='center');## Update
#plt.savefig('C:/Users/307006397/Desktop/F&B_Priority/DR_Analytics/fanModule2016.png',bbox_inches = 'tight')   ### Update
########################################################
###########    Take Off Rear   ##########################
#########################################################
#snapShotDataTo = snapShotData[pd.notnull(snapShotData['tk_zvb1r_smoothed'])]
#snapShotDataToSort=snapShotDataTo.sort(['serlzd_eng_ser_num','best_datetime'])
#snapShotDataToSortUn=snapShotDataToSort.serlzd_eng_ser_num.unique()
#snapShotDataToSort['best_datetime'] = pd.to_datetime(snapShotDataToSort['best_datetime'])
#grindData['Compliance Date'] = pd.to_datetime(grindData['Compliance Date'])
#ESN = []
#maxPreGrind=[]
#minPreGrind=[]
#maxPostGrind=[]
#minPostGrind=[]
#meanPreGrind=[]
#meanPostGrind=[]
#
##takeOffData.plot(kind='bar')
#for i in snapShotDataToSortUn:
#    xx=snapShotDataToSort.loc[snapShotDataToSort['serlzd_eng_ser_num'] == i]
#    takeOffData=xx.ix[:,["best_datetime","tk_zvb1r_smoothed"]]
#    uu=grindData.loc[grindData['Engine Serial Number'] == i]
#    uu = uu[pd.notnull(uu['Compliance Date'])]
#    if uu.empty:
#       print('DataFrame is empty!')
#       continue
#    vv=uu['Compliance Date']
##    vv=vv.to_string()
#    vv=vv.iloc[0]
##    vv=datetime.strptime(vv, '%m/%d/%y')
##    vv['Compliance Date'] = pd.to_datetime(vv['Compliance Date'])
#    postGrind=takeOffData.loc[takeOffData['best_datetime'] >= vv]
#    preGrind=takeOffData.loc[takeOffData['best_datetime'] < vv]
#    postGrind=postGrind['tk_zvb1r_smoothed']
#    preGrind=preGrind['tk_zvb1r_smoothed']
#    ESN.append(i)
#    maxPreGrind.append(preGrind.max())
#    minPreGrind.append(preGrind.min())
#    maxPostGrind.append(postGrind.max())
#    minPostGrind.append(postGrind.min())
#    meanPreGrind.append(preGrind.mean())
#    meanPostGrind.append(postGrind.mean())
#np.savetxt("rfesn.csv", ESN, delimiter=",")
#np.savetxt("rf1.csv", maxPreGrind, delimiter=",")
#np.savetxt("rf2.csv", minPreGrind, delimiter=",")
#np.savetxt("rf3.csv", maxPostGrind, delimiter=",")
#np.savetxt("rf4.csv", minPostGrind, delimiter=",")
#np.savetxt("rf5.csv", meanPreGrind, delimiter=",")
#np.savetxt("rf6.csv", meanPostGrind, delimiter=",")
#########################################################
###########  Climb Forward  #############################
#########################################################
#snapShotDataTo = snapShotData[pd.notnull(snapShotData['cl_zvb1f_smoothed'])]
#snapShotDataToSort=snapShotDataTo.sort(['serlzd_eng_ser_num','best_datetime'])
#snapShotDataToSortUn=snapShotDataToSort.serlzd_eng_ser_num.unique()
#snapShotDataToSort['best_datetime'] = pd.to_datetime(snapShotDataToSort['best_datetime'])
#grindData['Compliance Date'] = pd.to_datetime(grindData['Compliance Date'])
#ESN = []
#maxPreGrind=[]
#minPreGrind=[]
#maxPostGrind=[]
#minPostGrind=[]
#meanPreGrind=[]
#meanPostGrind=[]
#
##takeOffData.plot(kind='bar')
#for i in snapShotDataToSortUn:
#    xx=snapShotDataToSort.loc[snapShotDataToSort['serlzd_eng_ser_num'] == i]
#    takeOffData=xx.ix[:,["best_datetime","cl_zvb1f_smoothed"]]
#    uu=grindData.loc[grindData['Engine Serial Number'] == i]
#    uu = uu[pd.notnull(uu['Compliance Date'])]
#    if uu.empty:
#       print('DataFrame is empty!')
#       continue
#    vv=uu['Compliance Date']
##    vv=vv.to_string()
#    vv=vv.iloc[0]
##    vv=datetime.strptime(vv, '%m/%d/%y')
##    vv['Compliance Date'] = pd.to_datetime(vv['Compliance Date'])
#    postGrind=takeOffData.loc[takeOffData['best_datetime'] >= vv]
#    preGrind=takeOffData.loc[takeOffData['best_datetime'] < vv]
#    postGrind=postGrind['cl_zvb1f_smoothed']
#    preGrind=preGrind['cl_zvb1f_smoothed']
#    ESN.append(i)
#    maxPreGrind.append(preGrind.max())
#    minPreGrind.append(preGrind.min())
#    maxPostGrind.append(postGrind.max())
#    minPostGrind.append(postGrind.min())
#    meanPreGrind.append(preGrind.mean())
#    meanPostGrind.append(postGrind.mean())
#np.savetxt("cfesn.csv", ESN, delimiter=",")
#np.savetxt("cf1.csv", maxPreGrind, delimiter=",")
#np.savetxt("cf2.csv", minPreGrind, delimiter=",")
#np.savetxt("cf3.csv", maxPostGrind, delimiter=",")
#np.savetxt("cf4.csv", minPostGrind, delimiter=",")
#np.savetxt("cf5.csv", meanPreGrind, delimiter=",")
#np.savetxt("cf6.csv", meanPostGrind, delimiter=",")
#########################################################
###########  Climb Rear  ################################
#########################################################
#snapShotDataTo = snapShotData[pd.notnull(snapShotData['cl_zvb1r_smoothed'])]
#snapShotDataToSort=snapShotDataTo.sort(['serlzd_eng_ser_num','best_datetime'])
#snapShotDataToSortUn=snapShotDataToSort.serlzd_eng_ser_num.unique()
#snapShotDataToSort['best_datetime'] = pd.to_datetime(snapShotDataToSort['best_datetime'])
#grindData['Compliance Date'] = pd.to_datetime(grindData['Compliance Date'])
#ESN = []
#maxPreGrind=[]
#minPreGrind=[]
#maxPostGrind=[]
#minPostGrind=[]
#meanPreGrind=[]
#meanPostGrind=[]
#
##takeOffData.plot(kind='bar')
#for i in snapShotDataToSortUn:
#    xx=snapShotDataToSort.loc[snapShotDataToSort['serlzd_eng_ser_num'] == i]
#    takeOffData=xx.ix[:,["best_datetime","cl_zvb1r_smoothed"]]
#    uu=grindData.loc[grindData['Engine Serial Number'] == i]
#    uu = uu[pd.notnull(uu['Compliance Date'])]
#    if uu.empty:
#       print('DataFrame is empty!')
#       continue
#    vv=uu['Compliance Date']
##    vv=vv.to_string()
#    vv=vv.iloc[0]
##    vv=datetime.strptime(vv, '%m/%d/%y')
##    vv['Compliance Date'] = pd.to_datetime(vv['Compliance Date'])
#    postGrind=takeOffData.loc[takeOffData['best_datetime'] >= vv]
#    preGrind=takeOffData.loc[takeOffData['best_datetime'] < vv]
#    postGrind=postGrind['cl_zvb1r_smoothed']
#    preGrind=preGrind['cl_zvb1r_smoothed']
#    ESN.append(i)
#    maxPreGrind.append(preGrind.max())
#    minPreGrind.append(preGrind.min())
#    maxPostGrind.append(postGrind.max())
#    minPostGrind.append(postGrind.min())
#    meanPreGrind.append(preGrind.mean())
#    meanPostGrind.append(postGrind.mean())
#np.savetxt("crfesn.csv", ESN, delimiter=",")
#np.savetxt("crf1.csv", maxPreGrind, delimiter=",")
#np.savetxt("crf2.csv", minPreGrind, delimiter=",")
#np.savetxt("crf3.csv", maxPostGrind, delimiter=",")
#np.savetxt("crf4.csv", minPostGrind, delimiter=",")
#np.savetxt("crf5.csv", meanPreGrind, delimiter=",")
#np.savetxt("crf6.csv", meanPostGrind, delimiter=",")
#########################################################
###########  Cruise Forward #############################
#########################################################
#snapShotDataTo = snapShotData[pd.notnull(snapShotData['cr_zvb1f_smoothed'])]
#snapShotDataToSort=snapShotDataTo.sort(['serlzd_eng_ser_num','best_datetime'])
#snapShotDataToSortUn=snapShotDataToSort.serlzd_eng_ser_num.unique()
#snapShotDataToSort['best_datetime'] = pd.to_datetime(snapShotDataToSort['best_datetime'])
#grindData['Compliance Date'] = pd.to_datetime(grindData['Compliance Date'])
#ESN = []
#maxPreGrind=[]
#minPreGrind=[]
#maxPostGrind=[]
#minPostGrind=[]
#meanPreGrind=[]
#meanPostGrind=[]
#
##takeOffData.plot(kind='bar')
#for i in snapShotDataToSortUn:
#    xx=snapShotDataToSort.loc[snapShotDataToSort['serlzd_eng_ser_num'] == i]
#    takeOffData=xx.ix[:,["best_datetime","cr_zvb1f_smoothed"]]
#    uu=grindData.loc[grindData['Engine Serial Number'] == i]
#    uu = uu[pd.notnull(uu['Compliance Date'])]
#    if uu.empty:
#       print('DataFrame is empty!')
#       continue
#    vv=uu['Compliance Date']
##    vv=vv.to_string()
#    vv=vv.iloc[0]
##    vv=datetime.strptime(vv, '%m/%d/%y')
##    vv['Compliance Date'] = pd.to_datetime(vv['Compliance Date'])
#    postGrind=takeOffData.loc[takeOffData['best_datetime'] >= vv]
#    preGrind=takeOffData.loc[takeOffData['best_datetime'] < vv]
#    postGrind=postGrind['cr_zvb1f_smoothed']
#    preGrind=preGrind['cr_zvb1f_smoothed']
#    ESN.append(i)
#    maxPreGrind.append(preGrind.max())
#    minPreGrind.append(preGrind.min())
#    maxPostGrind.append(postGrind.max())
#    minPostGrind.append(postGrind.min())
#    meanPreGrind.append(preGrind.mean())
#    meanPostGrind.append(postGrind.mean())
#np.savetxt("clfesn.csv", ESN, delimiter=",")
#np.savetxt("clf1.csv", maxPreGrind, delimiter=",")
#np.savetxt("clf2.csv", minPreGrind, delimiter=",")
#np.savetxt("clf3.csv", maxPostGrind, delimiter=",")
#np.savetxt("clf4.csv", minPostGrind, delimiter=",")
#np.savetxt("clf5.csv", meanPreGrind, delimiter=",")
#np.savetxt("clf6.csv", meanPostGrind, delimiter=",")
#########################################################
###########  Cruise Rear     ############################
#########################################################
#snapShotDataTo = snapShotData[pd.notnull(snapShotData['cr_zvb1r_smoothed'])]
#snapShotDataToSort=snapShotDataTo.sort(['serlzd_eng_ser_num','best_datetime'])
#snapShotDataToSortUn=snapShotDataToSort.serlzd_eng_ser_num.unique()
#snapShotDataToSort['best_datetime'] = pd.to_datetime(snapShotDataToSort['best_datetime'])
#grindData['Compliance Date'] = pd.to_datetime(grindData['Compliance Date'])
#ESN = []
#maxPreGrind=[]
#minPreGrind=[]
#maxPostGrind=[]
#minPostGrind=[]
#meanPreGrind=[]
#meanPostGrind=[]
#
##takeOffData.plot(kind='bar')
#for i in snapShotDataToSortUn:
#    xx=snapShotDataToSort.loc[snapShotDataToSort['serlzd_eng_ser_num'] == i]
#    takeOffData=xx.ix[:,["best_datetime","cr_zvb1r_smoothed"]]
#    uu=grindData.loc[grindData['Engine Serial Number'] == i]
#    uu = uu[pd.notnull(uu['Compliance Date'])]
#    if uu.empty:
#       print('DataFrame is empty!')
#       continue
#    vv=uu['Compliance Date']
##    vv=vv.to_string()
#    vv=vv.iloc[0]
##    vv=datetime.strptime(vv, '%m/%d/%y')
##    vv['Compliance Date'] = pd.to_datetime(vv['Compliance Date'])
#    postGrind=takeOffData.loc[takeOffData['best_datetime'] >= vv]
#    preGrind=takeOffData.loc[takeOffData['best_datetime'] < vv]
#    postGrind=postGrind['cr_zvb1r_smoothed']
#    preGrind=preGrind['cr_zvb1r_smoothed']
#    ESN.append(i)
#    maxPreGrind.append(preGrind.max())
#    minPreGrind.append(preGrind.min())
#    maxPostGrind.append(postGrind.max())
#    minPostGrind.append(postGrind.min())
#    meanPreGrind.append(preGrind.mean())
#    meanPostGrind.append(postGrind.mean())
#np.savetxt("clrfesn.csv", ESN, delimiter=",")
#np.savetxt("clrf1.csv", maxPreGrind, delimiter=",")
#np.savetxt("clrf2.csv", minPreGrind, delimiter=",")
#np.savetxt("clrf3.csv", maxPostGrind, delimiter=",")
#np.savetxt("clrf4.csv", minPostGrind, delimiter=",")
#np.savetxt("clrf5.csv", meanPreGrind, delimiter=",")
#np.savetxt("clrf6.csv", meanPostGrind, delimiter=",")
###########################################################################