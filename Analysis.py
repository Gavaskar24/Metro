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

df2=df[df["PARKING"]>0]

fig=px.histogram(df2,x="PARKING",color="")