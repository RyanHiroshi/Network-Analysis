#Libraries for analysis
import pandas as pd
import plotly.graph_objects as go
import numpy as np
from sklearn import svm
import dask.dataframe as dd
from decimal import Decimal

#Libraries for visual
import matplotlib.pyplot as plt
import plotly.express as px

import os
import glob



###READ DATA###
#data = dd.read_csv('D:/frontier/project/data/*.csv') #read all files
#data = pd.read_csv('scan.csv1.csv') #10k
#data = pd.read_csv('D:/frontier/project/data/scan.csv2.csv') #1mil
# dtype={'scr_id':str, 'dst_ip':str, 'time':int, 'asn':int, 'cntry':str, 'scr_port':str, 'time':int}
#data = pd.read_csv('D:/frontier/project/data_large_attacked_lookedup.csv')
# data = pd.read_csv('D:/frontier/project/data/clean/combined_csv.csv')
# data = pd.read_csv('D:/frontier/project/data_large_attacker_lookedup.csv')

##MERGE MULTIPLE FILES###
# os.chdir('D:/frontier/project/data/clean/')
# extension = 'csv'
# all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
# combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ]
# combined_csv.to_csv("combined_csv.csv", index=False)

###DATA ATTACKED###
#       Group data attacked by frequency count of >= 6 attacks
# data_attacked = data[['time','src_id','asn','cntry','dst_ip','src_port']]
# data_large_attacked=data_attacked.groupby(['dst_ip'])['dst_ip'].agg({'Frequency':'count'})
# filtered_data = data_large_attacked[(data_large_attacked['Frequency']>=6)]
# filtered_data.to_csv('data_large_attacked.csv', sep=',', encoding='utf-8')
# data_attacker = data.groupby(['src_id','dst_ip'])['asn'].agg({'Frequency':'count'})


#       Data dst_ip lookedup on data_large_attacked
# data_large_attacked = pd.read_csv('D:/frontier/project/data_large_attacked.csv')
# data_lookup_attacked = data[['time','src_id','cntry','asn','src_port','dst_ip']]
# lookedup = data_lookup_attacked[data_lookup_attacked['dst_ip'].isin(data_large_attacked['dst_ip'])]
# lookedup.to_csv('data_large_attacked_lookedup.csv', sep=',', encoding='utf-8', index=False)

# Merge data attacked with frequency
# data = pd.read_csv('D:/frontier/project/data_large_attacker_lookedup.csv')
# data_freq = pd.read_csv('D:/frontier/project/data_large_attacked.csv')
# data_freq['Frequency']=data_freq['Frequency'].astype(str)
# newData = pd.merge(data,data_freq,on=['src_id'])
# newData.to_csv('data_large_attacker_lookedup.csv', sep=',',encoding='utf-8', index=False)
# print(data.head(10))

# Convert data_large_attacked_lookedup.csv's time to datetime
# data = pd.read_csv('D:/frontier/project/data_large_attacked_lookedup.csv')
# data['time'] = pd.to_datetime(data['time'],unit='s') #convert from epoch to datetime
# data.to_csv('data_large_attacked_lookedup.csv', sep=',',encoding='utf-8', index=False)
# print(data.head())

# Add 3 letter world map country code
# data_country = pd.read_csv('D:/frontier/project/countryMap.txt', sep='\t')
# data = pd.read_csv('D:/frontier/project/data_large_attacker_lookedup.csv')
# newData = data.merge(data_country,how='inner',left_on=['cntry'],right_on=['2let'])
# newData= newData.drop(columns='cntry', axis=1)
# newData= newData.drop(columns='Countrylet', axis=1)
# newData= newData.drop(columns='2let', axis=1)
# newData.to_csv('data_large_attacker_lookedup.csv', index=False, encoding='utf-8', sep=',')


###ATTACKER###

# # Merge data attacker with frequency
# data = pd.read_csv('D:/frontier/project/data_large_attacker_lookedup.csv')
# data_freq = pd.read_csv('D:/frontier/project/data_large_attacker.csv')
# data_freq['Frequency']=data_freq['Frequency'].astype(str)
# newData = pd.merge(data,data_freq,on=['src_id'])
# newData.to_csv('data_large_attacker_lookedup.csv', sep=',',encoding='utf-8', index=False)
# print(data.head())

#       Group data attacker by frequency count of >= 10 attacks
# data_attack = data[['time','src_id','asn','cntry','dst_ip','src_port','lat','long']]
# data_large_attacker = data_attack.groupby(['src_id'])['src_id'].agg({'Frequency':'count'})
# filtered_data = data_large_attacker[(data_large_attacker['Frequency']>=10)]
# filtered_data.to_csv('data_large_attacker.csv', sep=',', encoding='utf-8')

#       Data src_ip lookedup on data_large_attacker
# data_large_attacker = pd.read_csv('D:/frontier/project/data_large_attacker.csv')
# data_lookup_attacker = data[['time','src_id','cntry','long','lat']]
# lookedup = data_lookup_attacker[data_lookup_attacker['src_id'].isin(data_large_attacker['src_id'])]
# lookedup.to_csv('data_large_attacker_lookedup.csv', sep=',', encoding='utf-8', index=False)

# Convert data_large_attacker_lookedup.csv's time to datetime
# data = pd.read_csv('D:/frontier/project/data_large_attacker_lookedup.csv')
# data_lookup = pd.read_csv('D:/frontier/project/data_large_attacker_lookedup.csv')
# data['time'] = pd.to_datetime(data['time'],unit='s') #convert from epoch to datetime
# data['time'] = data['time'].dt.floor('D')
# data['time'] = data['time'].dt.date
# data['long'] = data['long'].astype(str)
# data['lat'] = data['lat'].astype(str)
# data['src_id'] = data['src_id'].astype(str)
# data['3let'] = data['3let'].astype(str)
# data_lookup['long'] = data_lookup['long'].astype(str)
# data_lookup['lat'] = data_lookup['lat'].astype(str)
# data_large_attacked= data_attacked.groupby(['dst_ip'])['dst_ip'].agg({'Frequency':'count'})
# data = data.groupby(['time', 'src_id'], as_index=False).agg({'Frequency':'sum'}).reset_index() #automatic nuisance control removes long, lat, and 3let
# data = data.groupby(['src_id','time']).agg(lambda x : x.sum()).reset_index()
# data = pd.crosstab(index=data.head(100), columns=[data['time','src_id']], values=data['Frequency'], aggfunc='sum')
# data.to_csv('D:/frontier/project/data_lookedup_plotting.csv',sep=',', encoding='utf-8', index=False)
# df = pd.merge(data,data_lookup, on=['src_id'])
# cols = df.columns.tolist()
# df = df[cols[:2]+cols[2:-1]]
# df = df.rename(columns={'Frequency_x':'Frequency'})
# df['time'] = pd.to_datetime(df['time'],unit='s') #convert from epoch to datetime
# df['time'] = df['time'].dt.floor('D')
# df['time'] = df['time'].dt.date
# newdf = df.groupby(['time','src_id'], as_index=False)
# newdf = df.drop_duplicates() # substitute to groupby cause groupby doesnt work (i dont really know)
# df.to_csv('data_large_attacker_lookedup_plotting.csv', sep=',',encoding='utf-8', index=False)


###VISUALIZATION###
## Make the file smaller ##
# data_world = data[['src_id','cntry','lat','long','Frequency','time']]
# data_world.to_csv('data_world.csv', sep=',', encoding='utf-8')
# data_world = pd.read_csv('D:/frontier/project/data_world.csv')

# data = pd.read_csv('D:/frontier/project/data_large_attacked_lookedup.csv')
# print(data.head())

# Plot world choropleth Map
# data_world = pd.read_csv('D:/frontier/project/data_cntry.csv')
# data_world['text'] = data_world['3let'].astype(str) + ' Frequency: ' + data_world['Frequency'].astype(str)
#
# fig = go.Figure(data=go.Choropleth(
#     locations = data_world['3let'],
#     z = data_world['Frequency'],
#     text = data_world['text'],
#     colorscale = 'Blues',
#     autocolorscale=True,
#     reversescale=False,
#     marker_line_color='darkgray',
#     marker_line_width=0.5,
#     colorbar_title = 'Frequency of attack attempts by Country',
# ))
# fig.update_layout(
#     title_text='2011 Network Attacks',
#     geo=dict(
#         showframe=False,
#         showcoastlines=False,
#         projection_type='equirectangular'
#     )
# )
# fig.write_html('heatmap.html',auto_open=True)

#Scatter geographic map
# data['text'] = 'ASN: ' + data['asn'].astype(str) + ' ' + data['time'].astype(str) + ' ' + 'Source IP: ' + data['src_id'].astype(str) + ', Dest IP: ' + data['dst_ip'].astype(str) + ' ' + data['cntry'] +' Port: ' + data['src_port'].astype(str) #teks keterangan
# fig = go.Figure(data=go.Scattergeo(
#         lon = data['long'],
#         lat = data['lat'],
#         text = data['text'],
#         ))
# fig.update_layout(
#         title = 'BPG Location',
#         geo_scope='world',
#     )
# fig.write_html('first_figure.html',auto_open=True)

# Bubble map
data_world = pd.read_csv("data_lookedup_plotting.csv")
# country3letter = data_world['3let'].str[:3]
fig = px.scatter_geo(data_world, lat='lat', lon='long', color='3let',
                     hover_name='3let', size="Frequency",
                     animation_frame='time',
                     projection='natural earth')
fig.write_html('attacker.html',auto_open=True)

# #Group data #1
# grouped_data1 = data.groupby(['cntry','src_id']).size().reset_index().groupby('cntry')[[0]].max()
# print(grouped_data1.sort_values(by=grouped_data.columns[0], ascending=False))
#print(data['cntry'].value_counts().head(10))

#       Group data by asn with most attacks
# data_asn = data[['src_id','cntry','asn']].copy()
# data_asn.groupby(['cntry','asn'])['cntry'].agg({'Frequency':'count'}).to_csv('data_asn.csv', sep=',',encoding='utf-8')

#       Group data by country with most attacks
# data_cntry = data[['cntry','src_id']]
# data_cntry.groupby(['cntry'])['src_id'].agg({'Frequency':'count'}).to_csv('data_cntry.csv', sep=',',encoding='utf-8')
























#
# #Group data #2 sort by list of country with the most attacks
# fig, ax = plt.subplots()
# GD2 = data['cntry'].value_counts().head(10).plot(ax=ax, kind='bar')
# GD2.set_ylabel("Number of attack attempts")
#
# for p in GD2.patches:
#     GD2.annotate('{:.2E}'.format(Decimal(str(p.get_height()))), (p.get_x(), p.get_height()), fontsize=10)
#
# fig.subplots_adjust(left=0.15, right=0.97)
# fig.savefig('GD2.png')
#
# #Group data #3 sort by port number
# fig2, ax2 = plt.subplots()
# GD3 = data['src_port'].value_counts().head(15).plot(ax=ax2, kind='bar')
# GD3.set_ylabel("Number of attack to specified port")
#
# for q in GD3.patches:
#     GD3.annotate('{:.2E}'.format(Decimal(str(q.get_height()))), (q.get_x(), q.get_height()), fontsize=10)
#
# fig2.subplots_adjust(left=0.15, right=0.97)
# fig2.savefig('GD3.png')

# grouped_data3 = data['src_port'].value_counts()
# print(grouped_data3)

# print(data['time'].max())
# print(data['time'].min())
# plt.bar(x=np.arange(1,21), height=data[data.column[]])

#Grouping data
#grouped_data=data.groupby(data.columns[2]) #group by src_id
# for x, item in grouped_data:
#     print(grouped_data.get_group(x),"\n\n")
#

#Layout group data 2
