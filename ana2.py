import pandas as pd
import numpy as np
import re
import sys

# Read the CSV file
df = pd.read_csv("Data2.csv",encoding='utf-8', skiprows=1, header=0)
df = df.applymap(str)

#This was needed to avoid an error
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf8', buffering=1)
#print columns
print(df.shape)

#drop columns 1,2,3,4,5,41
df=df.drop(df.columns[[0,1,2,3,4,41]],axis=1)   

print(df.shape)

#output the file into csv
df.to_csv('Data3.csv',index=False,encoding='utf-8')

# #Importing dataframe with header columns
header=pd.read_csv("Header_file.csv")

#Add header to the DataFrame
df.columns=header.columns
print(df.columns)

#converting all values in columns 9,11,13,15,17,19,20,22,28 into integer type and column 9 is taken as 8 in df




print(df.dtypes)






 
