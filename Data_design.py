import pandas as pd
import numpy as np
import re

# Read the CSV file
file_name="Aug_22.csv"
df = pd.read_csv(file_name, skiprows=1, header=0)

#Removing unwanted columns

if file_name == "Aug_10.csv":
    df=df.drop(df.columns[[0,1,2,3,39]],axis=1)
    header=pd.read_csv("Header.csv")
    df.columns=header.columns
    df['PARKING']='0'  ## Note: while considering parking study do not load Aug_10.csv file,
                       ## I just created another column PARKING with all values as 0 
                       # inorder to load it for other studies

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

df['PARK_RENT']=0
if file_name=="Aug_10.csv" or file_name=="Aug_14.csv":
    df['PARK_RENT']=10
elif file_name=="Aug_22.csv":
    df['PARK_RENT']=5
else:
    df['PARK_RENT']=15

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

# print(df.columns)
arr=[      'Yes, I own a bicycle or I will buy a bicycle, and use it under current travel conditions between my home and the metro station. .',
 'Yes, I own a bicycle or I will buy a bicycle, and use it if a safe bicycling path is available between my home and the metro station. .',
                                                                        'Not Applicable - because neither ends of my trip is home. .' ,
                                                                                                         'No, I will not use a bicycle. .']
print("PARKING",arr)
###############    PARKING COLUMN ##############
#Creating a new column PARK
df['PARK']=-1

#Using the array of arr, convert the strings of column PARKING into integer values 
# and store then in new column called PARK
for i in range(len(arr)):
    df.loc[df['PARKING'] == str(arr[i]), 'PARK'] = i+1

df.to_csv("parking.csv")

# print(df["PARK"].head(10),df["PARKING"].head(10))

# Converting floats to integers in PARK and TWO_WHEELERcolumn
# df['PARK']=df['PARK'].astype(int)

# print("PARK",df["PARK"].unique())
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


############# AGE #####################################
df['AGE_C']=0
my_dict={'> 60 yrs ': 5, '36-45yrs ': 3, '36-45 yrs ': 3, '18-25 yrs ': 1, 
         '26-35 yrs ': 2, '18-25yrs ': 1, '26-35yrs ': 2, '46-60 yrs ': 4, '46-60yrs ': 4}

#Iterate through the dictionary and replace the values in AGE column
for key, value in my_dict.items():
    df.loc[df['AGE'] == key, 'AGE_C'] = value

##########################################################



###############  ACCESS_DISTANCE and EGRESS_DISTANCE ##########################
access=['< 0.5 km ','0.5 to 1 km ','1 km to 1.5 km ', '1.5 km to 2 km ', '2 km to 2.5 km ',    
  '2.5 km to 3 km ','3 km to 3.5 km ','3.5 km to 4 km ','4 km to 4.5 km ', '4.5 km to 5 km ', '> 5 km ']

print(df["EGRESS_DISTANCE"].unique())

df['ACCESS_DIS']=0
df['EGRESS_DIS']=0

access_mapping = {org: 1+i for i, org in enumerate(access)}

# Map 'D_TYPE' column to integers and fill unmatched types with -1
df['ACCESS_DIS'] = df['ACCESS_DISTANCE'].map(access_mapping).fillna(0).astype(int)
df['EGRESS_DIS'] = df['EGRESS_DISTANCE'].map(access_mapping).fillna(0).astype(int)

########################################################



################# BICYCLE USE ####################

bicycle=['For access trip only ',
         'For egress trip only ',
         'For both access and egress trips ',
    'For neither access nor egress trips ']

df['RENT_BICYCLE']=0

bicycle_mapping={c: 1+i for i,c in enumerate(bicycle)}

df['RENT_BICYCLE']=df['BICYCLE_USE'].map(bicycle_mapping).fillna(0).astype(int)

########################################################


# Enumerating GENDER Column

gender=['Female','Male']

df['MALE']=0

gender_mapping={c: i for i,c in enumerate(gender)}

df['MALE']=df['GENDER'].map(gender_mapping).fillna(0).astype(int)

############### ACCESS MODE ####################
my_dict={'Walk':1,'Auto Rickshaw':5,'Two-Wheeler':3,'Dropped-off by friends/others':8,
         'Car':4,'Ola/Uber car':6,'Bicycle':2,'Rapido/Uber moto/Ola App two-wheeler':7,
         'Office shuttles':9,'Car pooling':6,'Office vehicle':10,'Car pooling ':6,
         'Rapido/uber moto/Ola App two-wheeler':7,'Car from KLN driving school':6,
         'Office vehicle':10,'Office vehicle ':10,'Train ':11,'Train':11,'Walk':1,'Friends two wheeler':8,'Ksrtc bus':12,
         'Rapido/Uber Moto/Ola App two-wheeler':7,'Bus':12,'Company cab':10,'Shuttle':9,
         'Dropped by coleg':8,'Dropped by friend':8,'Uber auto':5,'College bus':12,
         'Company shuttle':9,'Office cab':10,'Company bus':9,'Company cab':10,
         'Office Bus':9,'Railway train':11,'Office metro feeder':9,
         'Dropped-off by friends/family members/others':8,'Drove and parked a two-Wheeler':3,
         'Drove and parked a car':4,'Indian railway':11,'Auto Rickshaw ':5, 'Walk ':1, 'Dropped-off by friends/others ':8 ,
         'Two-Wheeler ':3,'Ola/Uber car ':6, 'They will travel by normal train in yeshwantpur ':11, 'Car ':4,
        'Bicycle ':2, 'Rapido/Uber moto/Ola App two-wheeler ':7, 'Company cab':10, 'Bus':12,
        'Metro feeder':9, 'Shuttle bus':9, 'Company vehicle ':10, 'Office cab':10,
        'Rapido/Uber Moto/Ola two-wheeler ':7, 'Nil':0, 'Shuttle':10,
        'Their own two wheeler ':3, 'Bike':3, 'Own vehicle ':3, '2 wheller':3, 'Ksrtc':12,
        'Cycle':2, 'Their own bik':3, 'Pick up':8, 'Two wheeler ':3, 'Office vehicle':10,
        "He should look how he should travel correnty he don't know ":0, 'Train':11,
        'College bus':12, 'Dropped-off by friends/others':8, 'Own bike':3, 'Pick up ':8,
        'Bike ':3, 'Company shuttle bus':9, 'Office shuttle ':9,
        'Drove and parked a two-Wheeler ':3, 'Office shuttle bus':9, 'Office bus':9,
        'Dropped-off by friends/family members/others ':8, 'Ksrtc bus':12,
        'Drove and parked a car ':4, 'Yulu':7, 'Rapido/uber moto/Ola App two-wheeler ':7,
        'Office shuttle bus ':9,'Dropped by coleg ':8, 'Dropped by friend ':8, 'Uber auto ':5,'Company cab ':10,
        'Railway train ':11,'Indian railway ':11,'Rapido/Uber Moto/Ola App two-wheeler ':7}

df['ACCESS_M']=0

for key, value in my_dict.items():
    df.loc[df['ACCESS_MODE'] == key, 'ACCESS_M'] = value


#######################################################

################# EGRESS MODE #########################

df['EGRESS_M']=0

for key, value in my_dict.items():
    df.loc[df['EGRESS_MODE'] == key, 'EGRESS_M'] = value


#######################################################
#### Mapping ACCESS and EGRESS Distances

def map_access_dis(ACCESS_DIS):
    if ACCESS_DIS in [1, 2]:
        return ACCESS_DIS
    elif ACCESS_DIS in [3,4]:
        return 3
    elif ACCESS_DIS in [5,6,7,8]:
        return 4
    elif ACCESS_DIS in [9,10,11]:
        return 5

# Apply the mapping function to create the 'ACCESS_DIS_B' column
df['ACCESS_DIS_B'] = df['ACCESS_DIS'].apply(map_access_dis)



# convert all values of EGRESS_DIS into integers
df["EGRESS_DIS"]=df["EGRESS_DIS"].astype(int)

def map_egress_dis(EGRESS_DIS):
    if EGRESS_DIS in [1,2]:
        return int(EGRESS_DIS)
    if EGRESS_DIS in [3,4]:
        return 3
    if EGRESS_DIS in [5,6,7,8]:
        return 4
    if EGRESS_DIS in [9,10,11]:
        return 5
    elif EGRESS_DIS in [0]:
        return 2
    
    

# Apply the mapping function to create the 'EGRESS_DIS_B' column
df['EGRESS_DIS_B'] = df['EGRESS_DIS'].apply(map_egress_dis)

##########################
# Mapping INCOME to numeric values



########################################################

if file_name=="Aug_10.csv":
    df.to_csv('outputfile_1.csv',index=True)

elif file_name =="Aug_14.csv":
    df.to_csv('outputfile_2.csv',index=True)

elif file_name=="Aug_22.csv":
    df.to_csv('outputfile_3.csv',index=True)

else:
    df.to_csv('outputfile_4.csv',index=True)

