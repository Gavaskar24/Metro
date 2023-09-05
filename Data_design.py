import pandas as pd
import numpy as np
import re

# Read the CSV file
file_name="Aug_31.csv"
df = pd.read_csv(file_name, skiprows=1, header=0)

#Removing unwanted columns
if file_name == "Aug_10.csv":
    df=df.drop(df.columns[[0,1,2,3,39]],axis=1)
    header=pd.read_csv("Header.csv")
    df.columns=header.columns
    df['PARKING']="-1"
    df['N_BICYCLES'] = df['N_BICYCLES'].str.strip()
elif file_name=="Aug_14.csv":
    df=df.drop(df.columns[[0,1,2,3,40]],axis=1)
    header=pd.read_csv("Header_file.csv")
    df.columns=header.columns
    # df['PARKING']="-1"
    # df['N_BICYCLES'] = df['N_BICYCLES'].str.strip()
else:
    df=df.drop(df.columns[[0,1,2,3,4,41]],axis=1)
    header=pd.read_csv("Header_file.csv")
    df.columns=header.columns
#Importing dataframe with header columns



#Add header to the DataFrame



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

df['N_BICYCLES'] = pd.to_numeric(df['N_BICYCLES'], errors='coerce', downcast='integer')
df['N_BICYCLES'] = df['N_BICYCLES'].fillna(4).astype(int)
df['OTHERS'] = pd.to_numeric(df['OTHERS'], errors='coerce', downcast='integer')

# NOTE: Here Nan values are replaced by 4
df['TWO_WHEELER'] = df['TWO_WHEELER'].fillna(4).astype(int)



# check the dataframe for any null values
# print(df.isnull().sum())

#Removing unwanted text from few columns

df['O_TYPE'] = df['O_TYPE'].str.extract(r'(\w+)', expand=False)
df['ACCESS_MODE'] = df['ACCESS_MODE'].str.replace(r'\(.*\)', '',regex=True)
df['EGRESS_MODE'] = df['EGRESS_MODE'].str.replace(r'\(.*\)', '',regex=True)
df['D_TYPE'] = df['D_TYPE'].str.extract(r'(\w+)', expand=False)
df['ACCESS_DISTANCE'] = df['ACCESS_DISTANCE'].str.replace(r'\(.*\)', '',regex=True)
df['EGRESS_DISTANCE'] = df['EGRESS_DISTANCE'].str.replace(r'\(.*\)', '',regex=True)
df['CROWDING'] = df['CROWDING'].str.replace(r'\(.*\)', '',regex=True)
df['BICYCLE_USE'] = df['BICYCLE_USE'].str.replace(r'\(.*\)', '',regex=True)
df['PASS'] = df['PASS'].str.replace(r'\(.*\)', '',regex=True)
df['GENDER']=df['GENDER'].str.extract(r'(\w+)', expand=False)
df['AGE'] = df['AGE'].str.replace(r'\(.*\)', '',regex=True)
df['EDUCATION']=df['EDUCATION'].str.extract(r'(\w+)', expand=False)
df['OCCUPATION']=df['OCCUPATION'].str.extract(r'(\w+)', expand=False)
df['INCOME'] = df['INCOME'].str.replace(r'\(.*\)', '',regex=True)

df['PARKING'] = df['PARKING'].str.replace(r'\(.*?\)', '', regex=True)
df['TRIP_SEQUENCE'] = df['TRIP_SEQUENCE'].str.replace(r'\(.*?\)', '',regex=True)
df['S_1'] = df['S_1'].str.replace(r'\(.*?\)', '', regex=True)
df['S_2'] = df['S_2'].str.replace(r'\(.*?\)', '', regex=True)
df['S_3'] = df['S_3'].str.replace(r'\(.*?\)', '', regex=True)

df=df[df["PARKING"]!='-1']
arr=df["PARKING"].unique()

###############    PARKING COLUMN ##############
#Creating a new column PARK
df['PARK']=-1

#Using the array of arr, convert the strings of column PARKING into integer values 
# and store then in new column called PARK
for i in range(len(arr)):
    df.loc[df['PARKING'] == arr[i], 'PARK'] = i+1

print(df["PARK"].head(10),df["PARKING"].head(10))

# Converting floats to integers in PARK and TWO_WHEELERcolumn
# df['PARK']=df['PARK'].astype(int)

# print(df["PARK"].head(10))
#################################################


############## DESTINATION TYPE #################
#using the array of destination_types, convert the strings of column D_TYPE into integer values not float values
# and store then in new column called DESTINATION

#Creating destination_types array
destination_types=['Home','Work','School','Shopping','Restaurant','Social','Friend','Other']


#creating a dictionary to map destination_type to integers
destination_mapping = {dest: 1+i for i, dest in enumerate(destination_types)}

# Map 'D_TYPE' column to integers and fill unmatched types with -1
df['DESTINATION'] = df['D_TYPE'].map(destination_mapping).fillna(0).astype(int)

###################################################

############## ORIGIN TYPE #################
#using the array of destination_types, convert the strings of column D_TYPE into integer values not float values
# and store then in new column called DESTINATION

#Creating destination_types array


origin_types=['Home','Work', 'School','Shopping','Restaurant','Social','Friend','Other']

#creating a dictionary to map destination_type to integers
origin_mapping = {org: 1+i for i, org in enumerate(origin_types)}

# Map 'O_TYPE' column to integers and fill unmatched types with -1
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

df['RENT_BICYCLE']=0

bicycle_mapping={c: 1+i for i,c in enumerate(bicycle)}

df['RENT_BICYCLE']=df['BICYCLE_USE'].map(bicycle_mapping).fillna(0).astype(int)

#################    AGE     ########################

age=['36-45 yrs ', '18-25 yrs ', '26-35 yrs ', '46-60 yrs ', '> 60 yrs ']

df['AGE_NEW']=0

age_mapping={c: 1+i for i,c in enumerate(age)}

df['AGE_NEW']=df['AGE'].map(age_mapping).fillna(0).astype(int)


###################################################

# Enumerating GENDER Column

gender=['Female','Male']

df['MALE']=0

gender_mapping={c: i for i,c in enumerate(gender)}

df['MALE']=df['GENDER'].map(gender_mapping).fillna(0).astype(int)

############### ACCESS MODE ####################

access=[ 'Walk ',
 'Dropped-off by friends/family members/others ',
               'Drove and parked a two-Wheeler ',
                                'Auto Rickshaw ',
                       'Drove and parked a car ',
                                 'Ola/Uber car ',
                                      'Bicycle ',
                               'Indian railway ',
         'Rapido/Uber moto/Ola App two-wheeler ']

df['ACCESS']=0
access_mapping = {org: 1+i for i, org in enumerate(access)}

df['ACCESS']=df['ACCESS_MODE'].map(access_mapping).fillna(0).astype(int)

#######################################################

################# EGRESS MODE #########################

egress=[ 'Walk ',
 'Dropped-off by friends/family members/others ',
               'Drove and parked a two-Wheeler ',
                                'Auto Rickshaw ',
                       'Drove and parked a car ',
                                 'Ola/Uber car ',
                                      'Bicycle ',
                               'Indian railway ',
         'Rapido/Uber moto/Ola App two-wheeler ']

df['EGRESS']=0
egress_mapping = {org: 1+i for i, org in enumerate(egress)}

df['EGRESS']=df['EGRESS_MODE'].map(egress_mapping).fillna(0).astype(int)

print(df["N_BICYCLES"].unique())

#######################################################


if file_name=="Aug_10.csv":
    df.to_csv('outputfile_1.csv',index=True)

elif file_name =="Aug_14.csv":
    df.to_csv('outputfile_2.csv',index=True)

elif file_name=="Aug_22.csv":
    df.to_csv('outputfile_3.csv',index=True)

else:
    df.to_csv('outputfile_4.csv',index=True)

print(df["PARKING"].unique())
print(df["PARK"].unique())



df.to_csv('parking.csv',index=True)