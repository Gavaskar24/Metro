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

# NOTE: Here Nan values are replaced by -1
df['TWO_WHEELER'] = df['TWO_WHEELER'].fillna(-1).astype(int)



# check the dataframe for any null values
# print(df.isnull().sum())

#Removing unwanted text from few columns

df['O_TYPE'] = df['O_TYPE'].str.extract(r'(\w+)', expand=False)
df['ACCESS_MODE'] = df['ACCESS_MODE'].str.extract(r'(\w+)', expand=False)
df['EGRESS_MODE'] = df['EGRESS_MODE'].str.extract(r'(\w+)', expand=False)
df['D_TYPE'] = df['D_TYPE'].str.extract(r'(\w+)', expand=False)
df['ACCESS_DISTANCE'] = df['ACCESS_DISTANCE'].str.replace(r'\(.*\)', '',regex=True)
df['EGRESS_DISTANCE'] = df['EGRESS_DISTANCE'].str.replace(r'\(.*\)', '',regex=True)
df['BICYCLE_USE'] = df['BICYCLE_USE'].str.replace(r'\(.*\)', '',regex=True)
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


###############    PARKING COLUMN ##############
#Creating a new column PARK
df['PARK']=np.nan

#Using the array of arr, convert the strings of column PARKING into integer values 
# and store then in new column called PARK
for i in range(len(arr)):
    df.loc[df['PARKING'] == arr[i], 'PARK'] = i+1

# Converting floats to integers in PARK and TWO_WHEELERcolumn
df['PARK']=df['PARK'].astype(int)

#################################################


############## DESTINATION TYPE #################
#using the array of destination_types, convert the strings of column D_TYPE into integer values not float values
# and store then in new column called DESTINATION

#Creating destination_types array
destination_types=['Home','Work','School ','Shopping','Restaurant','Social','Friend','Other']

#creating a dictionary to map destination_type to integers
destination_mapping = {dest: 1+i for i, dest in enumerate(destination_types)}

# Map 'D_TYPE' column to integers and fill unmatched types with -1
df['DESTINATION'] = df['D_TYPE'].map(destination_mapping).fillna(0).astype(int)

###################################################

############## ORIGIN TYPE #################
#using the array of destination_types, convert the strings of column D_TYPE into integer values not float values
# and store then in new column called DESTINATION

#Creating destination_types array


origin_types=['Home','Work','School ','Shopping','Restaurant','Social','Friend','Other']

#creating a dictionary to map destination_type to integers
origin_mapping = {org: 1+i for i, org in enumerate(origin_types)}

# Map 'D_TYPE' column to integers and fill unmatched types with -1
df['ORIGIN'] = df['O_TYPE'].map(origin_mapping).fillna(0).astype(int)

###################################################


############## TRIP SEQUENCE #################

#Creating sequence array, considered rest of other sequences as 0
sequence=['Metro ','Bus + Metro ','Metro + Bus ','Bus1 + Metro + Bus2 ','Metro1 + Bus + Metro2 ']

#Initiate new array
df['TRIP']=0

# Map 'TRIP_SEQUENCE' column to integers 
for i, value in enumerate(sequence, start=1):
    df.loc[df['TRIP_SEQUENCE'] == value, 'TRIP'] = i

###################################################


###############  ACCESS_DISTANCE and EGRESS_DISTANCE ##########################
access=['< 0.5 km ', '1.5 km to 2 km ',    '0.5 to 1 km ', '1 km to 1.5 km ',
 '3 km to 3.5 km ', '4.5 km to 5 km ', '2.5 km to 3 km ',         '> 5 km ',
 '3.5 km to 4 km ', '4 km to 4.5 km ', '2 km to 2.5 km ']

df['ACCESS_DIS']=0
df['EGRESS_DIS']=0

access_mapping = {org: 1+i for i, org in enumerate(access)}

# Map 'D_TYPE' column to integers and fill unmatched types with -1
df['ACCESS_DIS'] = df['ACCESS_DISTANCE'].map(access_mapping).fillna(0).astype(int)
df['EGRESS_DIS'] = df['EGRESS_DISTANCE'].map(access_mapping).fillna(0).astype(int)

########################################################

################# BICYCLE USE ####################

bicycle=['For neither access nor egress trips ',
                'For access trip only ',
    'For both access and egress trips ',
                'For egress trip only ']

df['BICYCLE']=0

bicycle_mapping={c: 1+i for i,c in enumerate(bicycle)}

df['BICYCLE']=df['BICYCLE_USE'].map(bicycle_mapping).fillna(0).astype(int)

#########################################

print(df['PASS'].unique())

