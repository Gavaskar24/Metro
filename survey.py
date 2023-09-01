import pandas as pd
import re

# Read the CSV file
df = pd.read_csv("File.csv", skiprows=1, header=0)

df.columns = [re.sub(r'\(.*?\)', '', col) for col in df.columns]

#Importing dataframe with header columns
header=pd.read_csv("Headers.csv")

#Add header to the DataFrame
df.columns=header.columns

# Drop irrelevelent columns from the DataFrame

# df = df.drop(df.columns[0:4], axis=1)
# df=df.drop(df.columns[-1],axis=1)





print(df.dtypes)
df=df.convert_dtypes()

#Converting data_types into required formats
df['TOTAL_TRAVEL_TIME'] = pd.to_numeric(df['TOTAL_TRAVEL_TIME'], errors='coerce', downcast='integer')
df['WAITING_TIME_FIRST_STATION'] = pd.to_numeric(df['WAITING_TIME_FIRST_STATION'], errors='coerce', downcast='integer')
df['EGRESS_TIME'] = pd.to_numeric(df['EGRESS_TIME'], errors='coerce', downcast='integer')
df['ACCESS_TIME'] = pd.to_numeric(df['ACCESS_TIME'], errors='coerce', downcast='integer')
df['WAITING_TIME_FINAL_STATION'] = pd.to_numeric(df['WAITING_TIME_FINAL_STATION'], errors='coerce', downcast='integer')
df['WALKING_TIME_SECOND_STOP'] = pd.to_numeric(df['WALKING_TIME_SECOND_STOP'], errors='coerce', downcast='integer')
df['CARS'] = pd.to_numeric(df['CARS'], errors='coerce', downcast='integer')
df['TWO_WHEELER'] = pd.to_numeric(df['TWO_WHEELER'], errors='coerce', downcast='integer')
df['BICYCLES'] = pd.to_numeric(df['BICYCLES'], errors='coerce', downcast='integer')
# df['OTHERS'] = pd.to_numeric(df['OTHERS'], errors='coerce', downcast='integer')

print(df.dtypes)
print(df.columns)

# check the dataframe for any null values
print(df.isnull().sum())

#Keeping only english text in O_TYPE, TRIP_SEQUENCE, ACCESS_MODE, EGRESS_MODE, D_TYPE,ACCESS_DISTANCE,EGRESS_DISTANCE,BICYCLE_USE,PASS,CROWDING,GENDER, S1,S2,S3, AGE,EDUCATION, OCCUPATION AND INCOME columns of df
df['O_TYPE'] = df['O_TYPE'].str.extract(r'(\w+)', expand=False)
# df['TRIP_SEQUENCE'] = df['TRIP_SEQUENCE'].str.extract(r'(\w+)', expand=False)
df['ACCESS_MODE'] = df['ACCESS_MODE'].str.extract(r'(\w+)', expand=False)
df['EGRESS_MODE'] = df['EGRESS_MODE'].str.extract(r'(\w+)', expand=False)
df['D_TYPE'] = df['D_TYPE'].str.extract(r'(\w+)', expand=False)
df['ACCESS_DISTANCE'] = df['ACCESS_DISTANCE'].str.extract(r'(\w+)', expand=False)
df['EGRESS_DISTANCE'] = df['EGRESS_DISTANCE'].str.extract(r'(\w+)', expand=False)
df['BICYCLE_USE'] = df['BICYCLE_USE'].str.extract(r'(\w+)', expand=False)
df['PASS'] = df['PASS'].str.extract(r'(\w+)', expand=False)
df['CROWDING'] = df['CROWDING'].str.extract(r'(\w+)', expand=False)
df['GENDER']=df['GENDER'].str.extract(r'(\w+)', expand=False)
df['S_1']=df['S_1'].str.extract(r'(\w+)', expand=False)
df['S_2']=df['S_2'].str.extract(r'(\w+)', expand=False)
df['S_3']=df['S_3'].str.extract(r'(\w+)', expand=False)
df['AGE']=df['AGE'].str.extract(r'(\w+)', expand=False)
df['EDUCATION']=df['EDUCATION'].str.extract(r'(\w+)', expand=False)
df['OCCUPATION']=df['OCCUPATION'].str.extract(r'(\w+)', expand=False)
df['INCOME']=df['INCOME'].str.extract(r'(\w+)', expand=False)

#keeping only english letters and + in TRIP_SEQUENCE column
df['TRIP_SEQUENCE']=df['TRIP_SEQUENCE'].str.extract(r'([a-zA-Z+]+)', expand=False)
#Delete OTHERS column
df=df.drop(['OTHERS'],axis=1)

#printing unique values in TRIP_SEQUENCE column
arr=df['TRIP_SEQUENCE'].unique()

#creating a new trip_sequence column by assigining vlaue to each unique data point in TRIP_SEQUENCE column
# df['TRIP_SEQUENCE_NEW'] = df['TRIP_SEQUENCE'].apply(lambda x: 1 if x='metro' or x='Metro' else 2 if x = 'Bus' else 3 if x = 'Metro+Bus' else 4 if x = 'Train' else 5 if x = 'Bus+metro' else 6 if x='two'or x= 'bike' else 7 if x ='Metro+bus+metro' else 8 if x = 'Bus+metro+bus+bus' else 0)


#output the dataframe into a csv file
# df.to_csv('output.csv', index=False)








