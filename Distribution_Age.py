import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pymysql
import scipy
from scipy import stats
import warnings
warnings.filterwarnings("ignore", message= "pandas only supports SQLAlchemy connectable (engine/connection) or "
                                           "database string URI or sqlite3 DBAPI2 connection. Other DBAPI2 objects "
                                           "are not tested. Please consider using SQLAlchemy.")
connection = pymysql.connect(host='localhost', user='root', password='Pallu@834', database='Project')
crime_df = pd.read_sql("select * from crime_data", connection)

#Distribution of ages by sex in reported crimes
#Unique age and sex distribution
unique_age_sex_distribution = crime_df[['Vict_Sex', 'Vict_Age']].drop_duplicates()
print(unique_age_sex_distribution)
# chosen histogram for age distribution and categorizing based on sex
plt.figure(figsize=(10,6))
sns.histplot(data=unique_age_sex_distribution,x='Vict_Age',hue='Vict_Sex',multiple="stack", bins=20, palette='pastel')
# setting the plot title and labels
plt.title('Distribution Of Victim Ages By Sex in Reported Crimes')
plt.xlabel('Victim Ages')
plt.ylabel('Frequency of crimes')
plt.show() #showing the plot
#to know whether  there is  a significant difference in crime rates between male and female victims
male_vict=unique_age_sex_distribution[unique_age_sex_distribution['Vict_Sex']=='m']['Vict_Age']
female_vict=unique_age_sex_distribution[unique_age_sex_distribution['Vict_Sex']=='female']['Vict_Age']

#performing testing in order to get statistics i have to deal with null values or empty values
print("unique values in victims_sex:",unique_age_sex_distribution['Vict_Sex'].unique())
print("data types in victim ages:",unique_age_sex_distribution['Vict_Age'].dtype)

#checking for missing values
print("missing values in victim age:",unique_age_sex_distribution['Vict_Age'].isnull().sum())

#Replacing empty strings in victim sex column with Nan
unique_age_sex_distribution['Vict_Sex']=unique_age_sex_distribution['Vict_Sex'].replace('',np.nan)
print(unique_age_sex_distribution)

#length of male and female victim variables
male_vict=unique_age_sex_distribution[unique_age_sex_distribution['Vict_Sex']=='M']['Vict_Age']
female_vict=unique_age_sex_distribution[unique_age_sex_distribution['Vict_Sex']=='F']['Vict_Age']
print("number of males:",len(male_vict))
print("number of females:",len(female_vict))

#performing statistics i.e testing(the scipy module automatically performs stats based on the male and female victims)
if len(male_vict)>0 and len(female_vict)>0:
    tstatistics,pvalue=stats.ttest_ind(male_vict,female_vict)
    print("tstatistics_value:",tstatistics)
    print("p_value:",pvalue)
else:
    print("insufficient data for analysis")

#According to analysis there is no significant crime rates between male and females
#tstatistics_value: -0.28163449492931913
#p_value: 0.7787343814135936
#i have plotted the plot after removing empty values for distribution of ages by sex for better understanding
plt.figure(figsize=(10,6))
sns.histplot(data=unique_age_sex_distribution,x='Vict_Age',hue='Vict_Sex',multiple="stack", bins=20, palette='pastel')
#  plot title and labels
plt.title('Distribution Of Victim Ages By Sex in Reported Crimes')
plt.xlabel('Victim Ages')
plt.ylabel('Frequency of crimes')
# showing the plot
plt.show()
