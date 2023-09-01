import pandas as pd
import numpy as np
import re

# Read the CSV file
df = pd.read_csv("Data2.csv", skiprows=1, header=0)

#Removing unwanted columns
df=df.drop(df.columns[[0,1,2,3,4,41]],axis=1) 

#Importing dataframe with header columns
header=pd.read_csv("Header_file.csv")

#Add header to the DataFrame
df.columns=header.columns


# Converting columns into most probable datatypes
df=df.convert_dtypes()

#Converting data_types into required formats
df['TOTAL_TIME'] = pd.to_numeric(df['TOTAL_TIME'], errors='coerce', downcast='integer')
df['WT_FS'] = pd.to_numeric(df['WT_FS'], errors='coerce', downcast='integer')
df['EGRESS_TIME'] = pd.to_numeric(df['EGRESS_TIME'], errors='coerce', downcast='integer')
df['ACCESS_TIME'] = pd.to_numeric(df['ACCESS_TIME'], errors='coerce', downcast='integer')
df['WT_FIS'] = pd.to_numeric(df['WT_FIS'], errors='coerce', downcast='integer')
df['WAITING_TIME_SECOND_STOP'] = pd.to_numeric(df['WAITING_TIME_SECOND_STOP'], errors='coerce', downcast='integer')
df['CARS'] = pd.to_numeric(df['CARS'], errors='coerce', downcast='integer')
df['TWO_WHEELER'] = pd.to_numeric(df['TWO_WHEELER'], errors='coerce', downcast='integer')
df['BICYCLES'] = pd.to_numeric(df['BICYCLES'], errors='coerce', downcast='integer')
df['OTHERS'] = pd.to_numeric(df['OTHERS'], errors='coerce', downcast='integer')




# check the dataframe for any null values
# print(df.isnull().sum())

#Removing unwanted text from few columns

df['O_TYPE'] = df['O_TYPE'].str.extract(r'(\w+)', expand=False)
df['ACCESS_MODE'] = df['ACCESS_MODE'].str.extract(r'(\w+)', expand=False)
df['EGRESS_MODE'] = df['EGRESS_MODE'].str.extract(r'(\w+)', expand=False)
df['D_TYPE'] = df['D_TYPE'].str.extract(r'(\w+)', expand=False)
df['ACCESS_DISTANCE'] = df['ACCESS_DISTANCE'].str.extract(r'(\w+)', expand=False)
df['EGRESS_DISTANCE'] = df['EGRESS_DISTANCE'].str.extract(r'(\w+)', expand=False)
df['BICYCLE_USE'] = df['BICYCLE_USE'].str.extract(r'(\w+)', expand=False)
df['PASS'] = df['PASS'].str.extract(r'(\w+)', expand=False)
df['CROWDING'] = df['CROWDING'].str.extract(r'(\w+)', expand=False)
df['GENDER']=df['GENDER'].str.extract(r'(\w+)', expand=False)
df['AGE']=df['AGE'].str.extract(r'(\w+)', expand=False)
df['EDUCATION']=df['EDUCATION'].str.extract(r'(\w+)', expand=False)
df['OCCUPATION']=df['OCCUPATION'].str.extract(r'(\w+)', expand=False)
df['INCOME']=df['INCOME'].str.extract(r'(\w+)', expand=False)

df['PARKING'] = df['PARKING'].str.replace(r'\(.*?\)', '', regex=True)
df['TRIP_SEQUENCE'] = df['TRIP_SEQUENCE'].str.replace(r'\(.*?\)', '',regex=True)
df['S_1'] = df['S_1'].str.replace(r'\(.*?\)', '', regex=True)
df['S_2'] = df['S_2'].str.replace(r'\(.*?\)', '', regex=True)
df['S_3'] = df['S_3'].str.replace(r'\(.*?\)', '', regex=True)

arr=df['PARKING'].unique()

print(arr)


#Creating a new column PARK
df['PARK']=np.nan

#Using the array of arr, convert the strings of column PARKING into integer values 
# and store then in new column called PARK
for i in range(len(arr)):
    df.loc[df['PARKING'] == arr[i], 'PARK'] = i

# Converting floats to integers in PARK and TWO_WHEELERcolumn
df['PARK']=df['PARK'].astype(int)
mask=df['TWO_WHEELER'].notna()
df['TWO_WHEELER']=df.loc[mask,'TWO_WHEELER'].astype('int64')

print(df.dtypes)


#using the array of destination_types, convert the strings of column D_TYPE into integer values not float values
# and store then in new column called DESTINATION

#Creating destination_types array
destination_types=df['D_TYPE'].unique()

#creating a dictionary to map destination_type to integers
destination_mapping = {dest: 1+i for i, dest in enumerate(destination_types)}

# Map 'D_TYPE' column to integers and fill unmatched types with -1
df['DESTINATION'] = df['D_TYPE'].map(destination_mapping).fillna(0).astype(int)
# df['DESTINATION'].astype(int)
print(df['DESTINATION'].unique())
print(destination_types)
#Create a new column DESTINATION with 




