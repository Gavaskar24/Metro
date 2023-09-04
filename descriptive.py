import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
from matplotlib.ticker import PercentFormatter

# Reading two csv files and combining them together

df1=pd.read_csv('outputfile_1.csv')
df2=pd.read_csv('outputfile_2.csv')
df3=pd.read_csv('outputfile_3.csv')
df4=pd.read_csv('outputfile_4.csv')

df=pd.concat([df1,df2,df3,df4])

# print(df.columns)


#percentage of rows with MALE==1 in df

male=(df[df["MALE"]==1].shape[0])*100/(df.shape[0])

print("Percentage of male respondents:", round(male,2), "%")

print("Percentage of female respondents",round(100-male,2),"%")

#percentage of rows with N_BICYCLE is greater than 0 in df

bicycle=(df[df["N_BICYCLES"]>0].shape[0])*100/(df.shape[0])

print("Percentage of respondents owning atleast 1 Bicycle:", round(bicycle,2), "%")

home_dest=df[df["DESTINATION"]==1].shape[0]

print("Percentage of respondents with home as destination:", round(home_dest*100/df.shape[0],2), "%")


### TRIP_SEQUENCE pie chart

trip_labels=['Metro ','Bus + Metro ','Metro + Bus ','Bus1 + Metro + Bus2 ','Metro1 + Bus + Metro2 ','Other']
    
df["TRIP"].value_counts().plot(kind='pie',autopct='%1.1f%%',figsize=(10,10),
                                    labels=trip_labels,title="Distribution of trips by sequence")
# plt.show()


#Pie chart for column DESTINATION with labels from labels
labels=['Home','Work','School ','Shopping','Restaurant','Social','Friend','Other']
df["DESTINATION"].value_counts().plot(kind='pie',autopct='%1.1f%%',figsize=(10,10),labels=labels,
                                 title="Distribution of trips by destination")
# plt.show()

#Pie chart for column ORIGIN with labels from labels

df["ORIGIN"].value_counts().plot(kind='pie',autopct='%1.1f%%',figsize=(10,10),
                                 labels=labels,title="Distribution of trips by origin")
# plt.show()





############ ACCESS DISTANCE#################################
# x_labels=['< 0.5 km ', '1.5 km to 2 km ', '0.5 to 1 km ', '1 km to 1.5 km ', '3 km to 3.5 km ',
#          '4.5 km to 5 km ', '2.5 km to 3 km ', '> 5 km ', '3.5 km to 4 km ', '4 km to 4.5 km ', '2 km to 2.5 km ']

# mapping= dict(zip(df["ACCESS_DIS"].unique(),df["ACCESS_DISTANCE"].unique()))

# df["ACCESS_DISTANCE_LABEL"]=df["ACCESS_DIS"].map(mapping)

# fig=px.histogram(df,x='ACCESS_DIS',labels={'ACCESS_DIS':'ACCESS_DISTANCE'},histnorm='percent',title="Distribution of Access Distance")

# total_count = len(df)
# percentage_labels = [(count / total_count) * 100 for count in df['ACCESS_DIS'].value_counts().sort_index()]
# percentage_labels = [f'{label:.2f}%' for label in percentage_labels]

# # Customize the bar labels and add the percentage labels
# fig.update_traces(text=df['ACCESS_DISTANCE_LABEL'], textposition='outside')
# fig.update_layout(annotations=[dict(text=label, x=distance) for 
#                                label, distance in 
#                                zip(percentage_labels, df['ACCESS_DIS'].value_counts().sort_index().index)])
# # fig.show()


################## EGRESS distance ################

# x_labels=['< 0.5 km ', '1.5 km to 2 km ', '0.5 to 1 km ', '1 km to 1.5 km ', '3 km to 3.5 km ',
#          '4.5 km to 5 km ', '2.5 km to 3 km ', '> 5 km ', '3.5 km to 4 km ', '4 km to 4.5 km ', '2 km to 2.5 km ']

# mapping= dict(zip(df["EGRESS_DIS"].unique(),df["EGRESS_DISTANCE"].unique()))

# df["EGRESS_DISTANCE_LABEL"]=df["EGRESS_DIS"].map(mapping)

# fig=px.histogram(df,x='EGRESS_DIS',labels={'EGRESS_DIS':'EGRESS_DISTANCE'},histnorm='percent',
#                         title="Distribution of Access Distance")

# total_count = len(df)
# percentage_labels = [(count / total_count) * 100 for count in df['EGRESS_DIS'].value_counts().sort_index()]
# percentage_labels = [f'{label:.2f}%' for label in percentage_labels]

# # Customize the bar labels and add the percentage labels
# fig.update_traces(text=df['EGRESS_DISTANCE_LABEL'], textposition='outside')
# fig.update_layout(annotations=[dict(text=label, x=distance) for 
#                                label, distance in 
#                                zip(percentage_labels, df['EGRESS_DIS'].value_counts().sort_index().index)])
# fig.show()

# plt.figure()
#plot a histogram of column ACCESS_DIS
plt.hist(df["ACCESS_DIS"],bins=11,edgecolor='black',weights=np.ones(len(df)) / len(df))
plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
plt.xlabel('ACCESS_DISTANCE')
plt.ylabel('Percentage')
plt.xticks(sorted(df["ACCESS_DIS"].unique()))
# plt.show()

# plt.figure()
#plot a histogram of column ACCESS_DIS
plt.hist(df["EGRESS_DIS"],bins=11,edgecolor='black',weights=np.ones(len(df)) / len(df))
plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
plt.xlabel('EGRESS_DISTANCE')
plt.ylabel('Percentage')
plt.xticks(sorted(df["EGRESS_DIS"].unique()))
# plt.show()

# plt.figure()
#plot a histogram of column ACCESS_DIS

plt.hist(df["ACCESS_MODE"],bins=11,edgecolor='black',weights=np.ones(len(df)) / len(df))
plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
plt.xlabel('ACCESS')
plt.ylabel('Percentage')
plt.xticks(sorted(df["ACCESS_MODE"].unique()))
plt.show()

