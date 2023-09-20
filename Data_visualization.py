import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

# Reading two csv files and combining them together

df1=pd.read_csv('outputfile_1.csv')
df2=pd.read_csv('outputfile_2.csv')
df3=pd.read_csv('outputfile_3.csv')
df4=pd.read_csv('outputfile_4.csv')

df=pd.concat([df1,df2,df3,df4])
df_park=pd.concat([df2,df3,df4])

print(df.columns)

print(df['N_BICYCLES'].value_counts())

print("Proportion of sample owning atleast 1 Bicycle:",
      round(len(df[df['N_BICYCLES'] > 0])*100/df.shape[0],2),
        "i.e",len(df[df['N_BICYCLES'] > 0]), "out of ",df.shape[0] )



df['N_BICYCLES'].value_counts().plot(kind='pie',autopct='%1.1f%%',figsize=(10,10))

# plt.show()


fig=px.histogram(df,x='BICYCLE_USE',color='MALE')

# fig.show()

# fig=px.histogram(df,x='ACCESS_DISTANCE',color='BICYCLE_USE',histnorm='percent',text_auto=True)
df1=df[df["DESTINATION"]==1]

fig=px.histogram(df,x='BICYCLE_USE',color="EGRESS_DISTANCE",histnorm='percent',
                 text_auto=True,title="EGRESS DISTANCE VS BICYCLE USE")
# fig.show()

# df2=df[df["PARKING"]>0]

# fig=px.histogram(df2,x="PARKING",color="")

# fig.show()
df1=df[df["ACCESS_TIME"]<60]
df1=df1[df1["ACCESS_TIME"]>0]
df1=df1[df1["EGRESS_TIME"]<60]
df1=df1[df1["EGRESS_TIME"]>0]
print(df1.shape)
#Scatter plot between ACCESS_TIME and RENT_BICYCLE 
fig=px.scatter(df1,x="ACCESS_TIME", y="RENT_BICYCLE", color="MALE", title="ACCESS_TIME VS RENT_BICYCLE")
fig.update_traces(marker=dict(size=12,
                              line=dict(width=2,
                                        color='DarkSlateGrey')),
                  selector=dict(mode='markers'))
# fig.show()

fig=px.histogram(df1,x="ACCESS_TIME",y="RENT_BICYCLE",color='MALE',histnorm='percent',text_auto=True)
# fig.show()


# Create 4 bins for plotting histogram of ACCESS_TIME and RENT_BICYCLE
# Divide the column of ACCESS_TIME into intervals of 1 to 15, 16 to 30, 31 to 45, 46 to 60
# bins = [0,15,30,45,60]
# labels = ['1-15','16-30','31-45','46-60']
bins = [0,10,20,30,40,50]
labels = ['1-10','11-20','21-30','31-40','41-50']
df1['ACCESS_TIME_BINNED'] = pd.cut(df1['ACCESS_TIME'], bins=bins, labels=labels)
fig=px.histogram(df1, x='ACCESS_TIME_BINNED', color="RENT_BICYCLE", barmode='group', title="ACCESS TIME BINNED VS RENT BICYCLE")
# fig.show()


#Scatter plot between ACCESS_TIME and RENT_BICYCLE 
fig=px.scatter(df1,x="EGRESS_TIME", y="RENT_BICYCLE", color="MALE", title="EGRESS_TIME VS RENT_BICYCLE")
fig.update_traces(marker=dict(size=12,
                              line=dict(width=2,
                                        color='DarkSlateGrey')),
                  selector=dict(mode='markers'))
# fig.show()
#Sort the column EGRESS_TIME and also make sure all other columns are also sorted based on this column
df1=df1.sort_values(by=['EGRESS_TIME'])

# Doing the same grouped plots for EGRESS_TIME 
bins = [0,10,20,30,40,50]
labels = ['1-10','11-20','21-30','31-40','41-50']
df1['EGRESS_TIME_BINNED'] = pd.cut(df1['EGRESS_TIME'], bins=bins, labels=labels)
fig=px.histogram(df1, x='EGRESS_TIME_BINNED', color="RENT_BICYCLE", barmode='group', title="EGRESS TIME BINNED VS RENT BICYCLE")
# fig.show()

fig=px.scatter(df1,x="ACCESS_DISTANCE", y="RENT_BICYCLE", color="MALE", title="ACCESS_DISTANCE VS RENT_BICYCLE")
fig.update_traces(marker=dict(size=12,
                              line=dict(width=2,
                                        color='DarkSlateGrey')),
                  selector=dict(mode='markers'))
# fig.show()

print(df["ACCESS_DISTANCE"].unique())




fig=px.histogram(df,x='N_BICYCLES',color="PARK",histnorm='percent',
                 text_auto=True,title="PARKING VS BICYCLE USE")
fig.show()