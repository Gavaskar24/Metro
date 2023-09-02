import pandas as pd
import numpy as np

# Reading two csv files and combining them together

df1=pd.read_csv('edited_data.csv')
df2=pd.read_csv('edited_data1.csv')

df=pd.concat([df1,df2])

print(df.shape)