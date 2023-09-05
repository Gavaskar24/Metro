import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
from matplotlib.ticker import PercentFormatter

# Reading two csv files and combining them together

df1=pd.read_csv('outputfile_1.csv')
df2=pd.read_csv('outputfile_2.csv')
df3=pd.read_csv('outputfile_3.csv')
df4=pd.read_csv('outputfile_4.csv')

df_parking=pd.read_csv('parking.csv')
df=pd.concat([df1,df2,df3,df4])
df.to_csv('combined.csv')

# print(df.columns)


#percentage of rows with MALE==1 in df


########################   GENDER DISTRIBUTION #################

# counts, bins = np.histogram(df['MALE'], bins=2)

# plt.hist(df["MALE"],bins=2,edgecolor='black',weights=np.ones(len(df))/len(df),rwidth=0.2,histtype='bar')

# plt.gca().yaxis.set_major_formatter(PercentFormatter(1))

# for rect, count in zip(plt.gca().patches, counts):
#     height = rect.get_height()
#     plt.text(rect.get_x() + rect.get_width()/2, height + 0.01, count, ha='center', va='bottom') 

# plt.xlabel('Gender')
# plt.ylabel('Percentage')
# plt.xticks([0.25,0.75], ['Female', 'Male'])

# plt.show()


###########################################################################


######################  Origin distribution #####################

# counts, bins = np.histogram(df['ORIGIN'], bins=8)

# plt.hist(df["ORIGIN"],bins=8,edgecolor='black',weights=np.ones(len(df))/len(df),rwidth=0.2,histtype='bar')

# plt.gca().yaxis.set_major_formatter(PercentFormatter(1))

# for rect, count in zip(plt.gca().patches, counts):
#     height = rect.get_height()
#     plt.text(rect.get_x() + rect.get_width()/2, height + 0.01, count, ha='center', va='bottom') 

# plt.xlabel('Origin')
# plt.ylabel('Percentage')
# plt.title("Distribution trips w.r.t  Origin")
# plt.xticks([1.4,2.3,3.2,4.1,4.95,5.8,6.7,7.55], 
#            ['Home','Work', 'School','Shopping','Restaurant','Social','Friends place','Other'])

# plt.show()


#################################################################

############# DISTRIBUTION OF DESTINATION ######################

# counts, bins = np.histogram(df['DESTINATION'], bins=8)

# plt.hist(df["DESTINATION"],bins=8,edgecolor='black',weights=np.ones(len(df))/len(df),rwidth=0.2,histtype='bar')

# plt.gca().yaxis.set_major_formatter(PercentFormatter(1))

# for rect, count in zip(plt.gca().patches, counts):
#     height = rect.get_height()
#     plt.text(rect.get_x() + rect.get_width()/2, height + 0.01, count, ha='center', va='bottom') 

# plt.xlabel('Destination')
# plt.ylabel('Percentage')
# plt.title("Distribution trips w.r.t  Destination")
# plt.xticks([1.4,2.3,3.2,4.1,4.95,5.8,6.7,7.55], 
#            ['Home','Work', 'School','Shopping','Restaurant','Social','Friends place','Other'])

# plt.show()


################### BICYCLES ################################

# counts, bins = np.histogram(df['N_BICYCLES'], bins=5)

# plt.hist(df["N_BICYCLES"],bins=5,edgecolor='black',weights=np.ones(len(df))/len(df),rwidth=0.2,histtype='bar')

# plt.gca().yaxis.set_major_formatter(PercentFormatter(1))

# for rect, count in zip(plt.gca().patches, counts):
#     height = rect.get_height()
#     plt.text(rect.get_x() + rect.get_width()/2, height + 0.01, count, ha='center', va='bottom') 

# plt.xlabel('Bicycle count')
# plt.ylabel('Percentage')
# # plt.title("Distribution trips w.r.t  Origin")
# plt.xticks([0.4,1.2,2,2.8,3.6],['0','1','2','3','4+'])
# plt.show()
# print(df["N_BICYCLES"].value_counts())

####################################################################


# ### TRIP_SEQUENCE pie chart

# trip_labels=['Metro ','Bus + Metro ','Metro + Bus ','Bus1 + Metro + Bus2 ','Metro1 + Bus + Metro2 ','Other']
    
# df["TRIP"].value_counts().plot(kind='pie',autopct='%1.1f%%',figsize=(10,10),
#                                     labels=trip_labels,title="Distribution of trips by sequence")
# # plt.show()


# #Pie chart for column DESTINATION with labels from labels
# labels=['Home','Work','School ','Shopping','Restaurant','Social','Friend','Other']
# df["DESTINATION"].value_counts().plot(kind='pie',autopct='%1.1f%%',figsize=(10,10),labels=labels,
#                                  title="Distribution of trips by destination")
# # plt.show()

# #Pie chart for column ORIGIN with labels from labels

# df["ORIGIN"].value_counts().plot(kind='pie',autopct='%1.1f%%',figsize=(10,10),
#                                  labels=labels,title="Distribution of trips by origin")
# plt.show()


##################################################################


############ ACCESS DISTANCE#################################

# counts, bins = np.histogram(df['ACCESS_DIS'], bins=11)

# plt.hist(df["ACCESS_DIS"],bins=11,edgecolor='black',weights=np.ones(len(df))/len(df),
#                                       rwidth=2,histtype='bar')

# plt.gca().yaxis.set_major_formatter(PercentFormatter(1))

# for rect, count in zip(plt.gca().patches, counts):
#     height = rect.get_height()
#     plt.text(rect.get_x() + rect.get_width()/2, height + 0.01, count, ha='center', va='bottom') 

# plt.xlabel('DISTANCE RANGES (kms)')
# plt.ylabel('Percentage')
# plt.title("Distribution trips w.r.t Access distances")
# plt.xticks([1,1.9,2.8,3.75,4.65,5.5,6.5,7.35,8.3,9.2,10.1],['0','0.5','1','1.5','2','2.5','3','3.5','4','4.5','5+'])
# plt.show()

################################################################


################## EGRESS distance ################
# df=df[df["EGRESS_DIS"]>0]
# counts, bins = np.histogram(df['EGRESS_DIS'], bins=11)

# plt.hist(df["EGRESS_DIS"],bins=11,edgecolor='black',weights=np.ones(len(df))/len(df),
#                                       rwidth=2,histtype='bar')

# plt.gca().yaxis.set_major_formatter(PercentFormatter(1))

# for rect, count in zip(plt.gca().patches, counts):
#     height = rect.get_height()
#     plt.text(rect.get_x() + rect.get_width()/2, height + 0.01, count, ha='center', va='bottom') 

# plt.xlabel('DISTANCE RANGES (kms)')
# plt.ylabel('Percentage')
# plt.title("Distribution trips w.r.t Egress distances")
# plt.xticks([1,1.9,2.8,3.75,4.65,5.5,6.5,7.35,8.3,9.2,10.1],['0','0.5','1','1.5','2','2.5','3','3.5','4','4.5','5+'])
# plt.show()



############  willingness to use own bicycle ###########
# df1=df[df["DESTINATION"]==1]
# df1=df1[df1["MALE"]==0]


# print(df1["RENT_BICYCLE"].unique())

# counts, bins = np.histogram(df1['PARK'], bins=4)

# plt.hist(df1["PARK"],bins=4,edgecolor='black',weights=np.ones(len(df1))/len(df1),
#                                       rwidth=1.5,histtype='bar')

# plt.gca().yaxis.set_major_formatter(PercentFormatter(1))

# for rect, count in zip(plt.gca().patches, counts):
#     height = rect.get_height()
#     plt.text(rect.get_x() + rect.get_width()/2, height + 0.01, count, ha='center', va='bottom') 

# plt.ylabel('Percentage')
# plt.title("Preferences of female respondents with home as destination")
# plt.xticks([1.3,2.1,2.9,3.7],['Present condition','Cycle track','Not applicable','Will not use'])
# plt.show()

# ########################################################




###################### Combined plot ##################

# df1=df[df["ORIGIN"]==1]
# df1=df1[df1["MALE"]==1]

# df2=df[df["DESTINATION"]==1]
# df2=df2[df2["MALE"]==1]

# counts1, bins1 = np.histogram(df1["RENT_BICYCLE"]) 
# counts1 = (100*counts1) / np.sum(counts1)

# # Plot 2 data 
# counts2, bins2 = np.histogram(df2["RENT_BICYCLE"])
# counts2 = (100*counts2) / np.sum(counts2)

# bar_width=0.5
# import matplotlib.pyplot as plt

# fig, ax = plt.subplots()

# # Get bins for each histogram
# bins1 = np.arange(len(counts1)) 
# bins2 = bins1 + bar_width  

# # Plot 1
# ax.bar(bins1, counts1, width=bar_width, edgecolor='black', alpha=0.5, label='Home as origin')

# # Plot 2  
# ax.bar(bins2, counts2, width=bar_width, edgecolor='black', alpha=0.5, label='Home as destination')

# ax.set_title('Usage of public bicycle by male respondents')
# ax.set_xlabel('Usage')
# ax.set_ylabel('Percentage')
# ax.set_xticks([0.3,3.2,6.2,9],['Only Access','Only Egress','For Both','For Neither'])


# ax.legend()

# plt.show()


############################################
# df=df[df["MALE"]==1]

# cross_tab=pd.crosstab(df["EGRESS_DIS"],df["RENT_BICYCLE"],margins=True,normalize='index')*100
# #rounding the values in cross_tab to 2 decimals
# cross_tab=np.round(cross_tab,decimals=2)
# print(cross_tab)
# # cross_tab=cross_tab.iloc[:-1,:-1] 0 
# cross_tab.plot(kind='bar',stacked=True)
# plt.xlabel('Egress distance')
# plt.ylabel('Percentage')
# plt.title("Egress distance vs Rent bicycle")
# plt.xticks([0,1,2,3,4,5,6,7,8,9,10,11],['<0.5','0.5-1','1-1.5','1.5-2','2-2.5','2.5-3','3-3.5','3.5-4','4-4.5','4.5-5','5+','All'])
# legend_labels=['Only Access','Only Egress','For Both','For Neither']
# plt.legend(legend_labels)
# plt.xticks(rotation=0)
# plt.show()
# cross_tab.to_csv('Egress distance vs Rented bicycle use.csv')

# print(df["RENT_BICYCLE"].value_counts())


############## Combined cross tabulation ##############################
# df1=df[df["MALE"]==1]
# df2=df[df["MALE"]==0]
# # Create cross-tabulations for Male and Female
# cross_tab_male = pd.crosstab(df1["MALE"],df1['RENT_BICYCLE'], normalize='index') * 100
# cross_tab_female = pd.crosstab(df2["MALE"],df2['RENT_BICYCLE'], normalize='index') * 100

# # Create subplots
# fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# # Plot Male cross-tabulation
# axes[0].bar(cross_tab_male.columns, cross_tab_male.iloc[0], label='Category 1', alpha=0.7)
# axes[0].set_title('Male Cross-Tabulation')
# axes[0].set_xlabel('Region')
# axes[0].set_ylabel('Percentage')
# axes[0].legend()

# # Plot Female cross-tabulation
# axes[1].bar(cross_tab_female.columns, cross_tab_female.iloc[0], label='Category 1', alpha=0.7)
# # axes[1].bar(cross_tab_female.columns, cross_tab_female.iloc[1], label='Category 2', bottom=cross_tab_female.iloc[0], alpha=0.7)
# axes[1].set_title('Female Cross-Tabulation')
# axes[1].set_xlabel('Region')
# axes[1].set_ylabel('Percentage')
# axes[1].legend()

# plt.tight_layout()
# plt.show()


############################################################



############## PARKING crosstab #####################
# df=df_parking
# # df=df[df["MALE"]==1]
# df=df[df["N_BICYCLES"]==0]
# df=df[(df["DESTINATION"]==1) ]

# cross_tab=pd.crosstab(df["ACCESS_DIS"],df["PARK"],margins=True,normalize='index')*100
# #rounding the values in cross_tab to 2 decimals
# cross_tab=np.round(cross_tab,decimals=2)
# print(cross_tab)
# # cross_tab=cross_tab.iloc[:-1,:-1] 0 
# cross_tab.plot(kind='bar',stacked=True)
# plt.xlabel('Egress distance (km)')
# plt.ylabel('Percentage')
# plt.title("Crosstabulation plot for Egress distance & Bicycle parking \n for respondents who  own bicycle and with home as destination")
# plt.xticks([0,1,2,3,4,5,6,7,8,9,10,11],['<0.5','0.5-1','1-1.5','1.5-2','2-2.5','2.5-3','3-3.5','3.5-4','4-4.5','4.5-5','5+','All'])
# legend_labels=['Will not use','Not Applicable','Cycle track','Present condition']
# plt.legend(legend_labels)
# plt.xticks(rotation=0)
# plt.show()
# # new_df=df[df["PARK"]==2]
# df.to_csv('check.csv')
# cross_tab.to_csv('Egress_distance vs Parking for respondents with home as destination and  owning bicycle.csv')

# ############################################