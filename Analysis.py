import pandas as pd
import numpy as np


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

# Plot some histogram using plotly

import plotly.express as px
fig = px.histogram(df, x="N_BICYCLES")
fig.show()
