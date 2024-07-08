import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pymysql
import warnings
warnings.filterwarnings("ignore", message= "pandas only supports SQLAlchemy connectable (engine/connection) or "
                                           "database string URI or sqlite3 DBAPI2 connection. Other DBAPI2 objects "
                                           "are not tested. Please consider using SQLAlchemy.")
connection=pymysql.connect(host='localhost',user='root',password='Password',database='Project')
crime_df = pd.read_sql("select * from crime_data",connection)
print(crime_df)

print(crime_df.describe())
print(crime_df.head())

# Converting 'DATE_OCC' column to datetime
crime_df['DATE_OCC'] = pd.to_datetime(crime_df['DATE_OCC'])

# Extracting the  year, month, and day from 'DATE_OCC'
crime_df['Year'] = crime_df['DATE_OCC'].dt.year
crime_df['Month'] = crime_df['DATE_OCC'].dt.month
crime_df['Day'] = crime_df['DATE_OCC'].dt.day

# Grouping by Year, Month, and Day and count occurrences
crime_by_year = crime_df.groupby('Year').size()
crime_by_month = crime_df.groupby(['Year', 'Month']).size()
crime_by_day =  crime_df.groupby(['Year', 'Month', 'Day']).size()

# Group by Year, Month, Day, and Crime Description, and count the occurrences
crime_by_year_month_day_description = crime_df.groupby(['Year', 'Month', 'Day', 'Crm_Cd_Desc']).size()

# Print the result
print("Crime occurrences by year, month, day, and description:")
print(crime_by_year_month_day_description)

print("\nCrime occurrences by day:")
print(crime_by_day)


# unique crime descriptions
unique_crime_descriptions = crime_df['Crm_Cd_Desc'].unique()


# the crime count  for each unique crime description
crime_counts = crime_df['Crm_Cd_Desc'].value_counts()

#  the total number of crimes
total_crimes = crime_counts.sum()

#  the crime percentage for each crime descriptions to the total no of crimes
crime_percentages = (crime_counts / total_crimes) * 100

#  crime descriptions and their corresponding percentages
crime_df = pd.DataFrame({'Crm_Cd_Desc': crime_percentages.index, 'crime_percentage': crime_percentages.values})

# Sorting  crime percentages in descending order
crime_df_sorted = crime_df.sort_values(by='crime_percentage', ascending=False)

# Top most frequent crime descriptions and their percentages
top_crime_descriptions = crime_df_sorted['Crm_Cd_Desc'].head(10)
top_crime_percentages = crime_df_sorted['crime_percentage'].head(10)

# Plot the percentages by using a pie chart
plt.figure(figsize=(10, 10))
plt.pie(top_crime_percentages, labels=top_crime_descriptions, autopct='%1.1f%%', shadow=True)
plt.title('Top Most Frequent Crimes')
# aspect ratio  that pie is drawn as a circle
plt.axis('equal')
plt.show()
