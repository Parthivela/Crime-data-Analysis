import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pymysql

connection=pymysql.connect(host='localhost',user='root',password='Pallu@834',database='Project')
crime_df = pd.read_sql("select * from crime_data",connection)
#print(crime_df)
#connection.close()
print(crime_df.describe())
print(crime_df.describe())
crime_df['DATE_OCC'] = pd.to_datetime(crime_df['DATE_OCC'],format='%d-%m-%Y')
crime_df['Date_Rptd']=pd.to_datetime(crime_df['Date_Rptd'],format='%d-%m-%Y')

crime_df['DATE_OCC'] = pd.to_datetime(crime_df['DATE_OCC'])
crime_df['Date_Rptd'] = pd.to_datetime(crime_df['Date_Rptd'])


#Grouping the data
daily_crime_counts = crime_df.groupby(crime_df['DATE_OCC'].dt.date).size()
monthly_crime_counts = crime_df.groupby(crime_df['DATE_OCC'].dt.to_period('M')).size()
yearly_crime_counts=crime_df.groupby(crime_df['DATE_OCC'].dt.to_period('Y')).size()
print(daily_crime_counts,monthly_crime_counts ,yearly_crime_counts)


# Creating  a single subplot for all graphs
#daily analysis
plt.subplot(2,2,1)
daily_crime_counts.plot(color='blue',marker="*")
plt.title('Daily Crime Trends')
plt.xlabel('Date')
plt.ylabel('Number of Crimes')
plt.grid(True)

# Monthly Analysis (Bar plot)
plt.subplot(2, 2, 2)
monthly_crime_counts.plot(kind='bar', color='green')
plt.title('Monthly Crime Trends')
plt.xlabel('Month')
plt.ylabel('Number of Crimes')
plt.xticks(rotation=45, ha='right')
plt.grid(True)

# Yearly Analysis (Line plot)
plt.subplot(2, 1,2)
yearly_crime_counts.plot(kind="bar", color='red')
plt.title('Yearly Crime Trends')
plt.xlabel('Year')
plt.ylabel('Number of Crimes')
plt.xticks(rotation=45, ha='right')
plt.grid(True)

# Adjusts subplot parameters

plt.tight_layout()
plt.show()


