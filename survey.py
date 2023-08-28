import pandas as pd
import plotly.express as px
import re
# Read the CSV file
df = pd.read_csv("C:\\Users\\CistupAdmin\\Downloads\\File.csv", skiprows=1, header=0)

df.columns = [re.sub(r'\(.*?\)', '', col) for col in df.columns]
# print(df.head(10))
header=pd.read_csv("F:\\Headers.csv")

# Drop specific columns from the DataFrame
df1 = df.drop(df.columns[0:4], axis=1)
df1=df1.drop(df1.columns[-1],axis=1)

# Adding a header file to existing DataFrame 
# df2= pd.concat([header, df1], ignore_index=True)
# print(df2.columns)

# df1.to_csv('Filtered')

data_df=pd.read_csv("C:\\Users\\CistupAdmin\\OneDrive - Indian Institute of Science\\Cistup\\Survey\\File.csv")

print(data_df.dtypes)
data_df=data_df.convert_dtypes()

#Converting data_types into required formats
data_df['TOTAL_TRAVEL_TIME'] = pd.to_numeric(data_df['TOTAL_TRAVEL_TIME'], errors='coerce', downcast='integer')
data_df['WAITING_TIME_FIRST_STATION'] = pd.to_numeric(data_df['WAITING_TIME_FIRST_STATION'], errors='coerce', downcast='integer')
data_df['EGRESS_TIME'] = pd.to_numeric(data_df['EGRESS_TIME'], errors='coerce', downcast='integer')
data_df['ACCESS_TIME'] = pd.to_numeric(data_df['ACCESS_TIME'], errors='coerce', downcast='integer')
data_df['WAITING_TIME_FINAL_STATION'] = pd.to_numeric(data_df['WAITING_TIME_FINAL_STATION'], errors='coerce', downcast='integer')
data_df['WALKING_TIME_SECOND_STOP'] = pd.to_numeric(data_df['WALKING_TIME_SECOND_STOP'], errors='coerce', downcast='integer')
data_df['CARS'] = pd.to_numeric(data_df['CARS'], errors='coerce', downcast='integer')
data_df['TWO_WHEELER'] = pd.to_numeric(data_df['TWO_WHEELER'], errors='coerce', downcast='integer')
data_df['BICYCLES'] = pd.to_numeric(data_df['BICYCLES'], errors='coerce', downcast='integer')
data_df['OTHERS'] = pd.to_numeric(data_df['OTHERS'], errors='coerce', downcast='integer')

fig=px.histogram(data_df,x='ACCESS_TIME')
fig.show()
print(data_df.head(10))





