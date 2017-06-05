
########################################################
##########    FAN MODULE   ############################
########################################################
### Fan Module 2016 Full Year
drGenxSort1617=drGenxSort.loc[drGenxSort['openDate'] >= '2016-01-01 00:00:00'] ## Update
drGenxSort16=drGenxSort1617.loc[drGenxSort1617['openDate'] <= '2017-01-01 00:00:00']## Update
value_list = ['Vikulp Sharma', 'David Rowe', 'Piotr Dabrowski']
drGenxFan=drGenxSort16[drGenxSort16.caseOwner.isin(value_list)]
interim=drGenxFan.loc[drGenxFan['Closed'] == 1]
drGenxFanFinal=interim[['caseOwner','caseRecord']]

drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'PCR']
ff=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()
       
drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'SDR']
jj=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()
     
drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'CDR']
kk=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()

frames=[ff,jj,kk]
result = pd.concat(frames,axis=1)
result.columns=["PCR","SDR","CDR"]
result.plot(kind='bar',title='Fan Module 2016 Full Year', align='center');## Update
plt.savefig('C:/Users/307006397/Desktop/F&B_Priority/DR_Analytics/fanModule2016.png',bbox_inches = 'tight')   ### Update

### Fan Module 2017 Full Year
drGenxSort1617=drGenxSort.loc[drGenxSort['openDate'] >= '2017-01-01 00:00:00'] ## Update
value_list = ['Vikulp Sharma', 'David Rowe', 'Piotr Dabrowski']
drGenxFan=drGenxSort16[drGenxSort16.caseOwner.isin(value_list)]
interim=drGenxFan.loc[drGenxFan['Closed'] == 1]
drGenxFanFinal=interim[['caseOwner','caseRecord']]

drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'PCR']
ff=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()
       
drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'SDR']
jj=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()
     
drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'CDR']
kk=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()

frames=[ff,jj,kk]
result = pd.concat(frames,axis=1)
result.columns=["PCR","SDR","CDR"]
result.plot(kind='bar',title='Fan Module 2017 Full Year', align='center');## Update
plt.savefig('C:/Users/307006397/Desktop/F&B_Priority/DR_Analytics/fanModule2017.png',bbox_inches = 'tight')   ### Update

### Fan Module 2016 First Quarter
drGenxSort1617=drGenxSort.loc[drGenxSort['openDate'] >= '2016-01-01 00:00:00'] ## Update
drGenxSort16=drGenxSort1617.loc[drGenxSort1617['openDate'] <= '2016-03-31 00:00:00']## Update
value_list = ['Vikulp Sharma', 'David Rowe', 'Piotr Dabrowski']
drGenxFan=drGenxSort16[drGenxSort16.caseOwner.isin(value_list)]
interim=drGenxFan.loc[drGenxFan['Closed'] == 1]
drGenxFanFinal=interim[['caseOwner','caseRecord']]

drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'PCR']
ff=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()
       
drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'SDR']
jj=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()
     
drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'CDR']
kk=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()

frames=[ff,jj,kk]
result = pd.concat(frames,axis=1)
result.columns=["PCR","SDR","CDR"]
result.plot(kind='bar',title='Fan Module 2016 First Quarter', align='center');## Update
plt.savefig('C:/Users/307006397/Desktop/F&B_Priority/DR_Analytics/fanModule2016firstQ.png',bbox_inches = 'tight')   ### Update

### Fan Module 2016 Second Quarter
drGenxSort1617=drGenxSort.loc[drGenxSort['openDate'] >= '2016-03-31 00:00:00'] ## Update
drGenxSort16=drGenxSort1617.loc[drGenxSort1617['openDate'] <= '2016-06-30 00:00:00']## Update
value_list = ['Vikulp Sharma', 'David Rowe', 'Piotr Dabrowski']
drGenxFan=drGenxSort16[drGenxSort16.caseOwner.isin(value_list)]
interim=drGenxFan.loc[drGenxFan['Closed'] == 1]
drGenxFanFinal=interim[['caseOwner','caseRecord']]

drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'PCR']
ff=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()
       
drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'SDR']
jj=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()
     
drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'CDR']
kk=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()

frames=[ff,jj,kk]
result = pd.concat(frames,axis=1)
result.columns=["PCR","SDR","CDR"]
result.plot(kind='bar',title='Fan Module 2016 Second Quarter', align='center');## Update
plt.savefig('C:/Users/307006397/Desktop/F&B_Priority/DR_Analytics/fanModule2016SecondQ.png',bbox_inches = 'tight')   ### Update

### Fan Module 2016 Third Quarter
drGenxSort1617=drGenxSort.loc[drGenxSort['openDate'] >= '2016-06-30 00:00:00'] ## Update
drGenxSort16=drGenxSort1617.loc[drGenxSort1617['openDate'] <= '2016-09-30 00:00:00']## Update
value_list = ['Vikulp Sharma', 'David Rowe', 'Piotr Dabrowski']
drGenxFan=drGenxSort16[drGenxSort16.caseOwner.isin(value_list)]
interim=drGenxFan.loc[drGenxFan['Closed'] == 1]
drGenxFanFinal=interim[['caseOwner','caseRecord']]

drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'PCR']
ff=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()
       
drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'SDR']
jj=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()
     
drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'CDR']
kk=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()

frames=[ff,jj,kk]
result = pd.concat(frames,axis=1)
result.columns=["PCR","SDR","CDR"]
result.plot(kind='bar',title='Fan Module 2016 Third Quarter', align='center');## Update
plt.savefig('C:/Users/307006397/Desktop/F&B_Priority/DR_Analytics/fanModule2016thirdQ.png',bbox_inches = 'tight')   ### Update

### Fan Module 2016 Last Quarter
drGenxSort1617=drGenxSort.loc[drGenxSort['openDate'] >= '2016-09-30 00:00:00'] ## Update
drGenxSort16=drGenxSort1617.loc[drGenxSort1617['openDate'] <= '2017-01-01 00:00:00']## Update
value_list = ['Vikulp Sharma', 'David Rowe', 'Piotr Dabrowski']
drGenxFan=drGenxSort16[drGenxSort16.caseOwner.isin(value_list)]
interim=drGenxFan.loc[drGenxFan['Closed'] == 1]
drGenxFanFinal=interim[['caseOwner','caseRecord']]

drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'PCR']
ff=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()
       
drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'SDR']
jj=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()
     
drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'CDR']
kk=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()

frames=[ff,jj,kk]
result = pd.concat(frames,axis=1)
result.columns=["PCR","SDR","CDR"]
result.plot(kind='bar',title='Fan Module 2016 Last Quarter', align='center');## Update
plt.savefig('C:/Users/307006397/Desktop/F&B_Priority/DR_Analytics/fanModule2016finalQ.png',bbox_inches = 'tight')   ### Update
           
### Fan Module 2017 First Quarter
drGenxSort1617=drGenxSort.loc[drGenxSort['openDate'] >= '2017-01-01 00:00:00'] ## Update
drGenxSort16=drGenxSort1617.loc[drGenxSort1617['openDate'] <= '2017-03-31 00:00:00']## Update
value_list = ['Vikulp Sharma', 'David Rowe', 'Piotr Dabrowski']
drGenxFan=drGenxSort16[drGenxSort16.caseOwner.isin(value_list)]
interim=drGenxFan.loc[drGenxFan['Closed'] == 1]
drGenxFanFinal=interim[['caseOwner','caseRecord']]

drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'PCR']
ff=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()
       
drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'SDR']
jj=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()
     
drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'CDR']
kk=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()

frames=[ff,jj,kk]
result = pd.concat(frames,axis=1)
result.columns=["PCR","SDR","CDR"]
result.plot(kind='bar',title='Fan Module 2017 First Quarter', align='center');## Update
plt.savefig('C:/Users/307006397/Desktop/F&B_Priority/DR_Analytics/fanModule2017firstQ.png',bbox_inches = 'tight')   ### Update

### Fan Module 2017 Second Quarter
drGenxSort1617=drGenxSort.loc[drGenxSort['openDate'] >= '2017-03-30 00:00:00'] ## Update
drGenxSort16=drGenxSort1617.loc[drGenxSort1617['openDate'] <= '2017-06-30 00:00:00']## Update
value_list = ['Vikulp Sharma', 'David Rowe', 'Piotr Dabrowski']
drGenxFan=drGenxSort16[drGenxSort16.caseOwner.isin(value_list)]
interim=drGenxFan.loc[drGenxFan['Closed'] == 1]
drGenxFanFinal=interim[['caseOwner','caseRecord']]

drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'PCR']
ff=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()
       
drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'SDR']
jj=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()
     
drGenxFanFinalPcr=drGenxFanFinal.loc[drGenxFanFinal['caseRecord'] == 'CDR']
kk=drGenxFanFinalPcr.groupby('caseOwner')['caseRecord'].count()

frames=[ff,jj,kk]
result = pd.concat(frames,axis=1)
result.columns=["PCR","SDR","CDR"]
result.plot(kind='bar',title='Fan Module 2016 Last Quarter', align='center');## Update
plt.savefig('C:/Users/307006397/Desktop/F&B_Priority/DR_Analytics/fanModule2017secondQ.png',bbox_inches = 'tight')   ### Update
