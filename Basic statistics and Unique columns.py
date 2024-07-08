import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pymysql
import warnings
warnings.filterwarnings("ignore", message= "pandas only supports SQLAlchemy connectable (engine/connection) or "
                                           "database string URI or sqlite3 DBAPI2 connection. Other DBAPI2 objects "
                                           "are not tested. Please consider using SQLAlchemy.")

# Establishing a connection to the database
pymysql.connect(host='localhost',
                        user='root',
                          password='Password',
                            database='Project')
# Execute the query and read the results
connection=pymysql.connect(host='localhost',user='root',password='Password',database='Project')
crime_df = pd.read_sql("select * from crime_data",connection)
print(crime_df)
connection.close()
crime_df['DATE_OCC'] = pd.to_datetime(crime_df['DATE_OCC'],format='%d-%m-%Y')

# total no of records
total_records=len(crime_df)
# information of a dataframe
print(crime_df.info())

# Adjusting to show all columns and rows
#pd.set_option('display.max_columns', None)
#pd.set_option('display.max_rows', None)
#print(crime_df)

# Data Frame volume and data types
print('Rows:\t{}'.format(crime_df.shape[0]))
print('Variables:\t{}'.format(crime_df.shape[1]))
print(crime_df.dtypes)

# checking missing values
missing_values = crime_df.isnull()
# count of missing values in each column
missing_count = crime_df.isnull().sum()
print("Missing Values Count:")
print(missing_count)
# If Missing values are true means there are missing values in DataFrame
print("DataFrame of Missing Values:")
print(missing_values)

# Get unique values in specific columns
unique_crime_location = crime_df['Location'].unique()
unique_crime_code = crime_df['Crm_Cd'].unique()
unique_crime_descrip = crime_df['Crm_Cd_Desc'].unique()
unique_Age = crime_df['Vict_Age'].unique()
unique_sex = crime_df['Vict_Sex'].unique()

# Basic statistics
print("Total number of records:", total_records)
print("Unique values in Location column:", unique_crime_location)
print("Unique values in Crm_Cd column:", unique_crime_code)
print("Unique values in Crm_Cd_Desc column:", unique_crime_descrip)
print("Unique values in Vict_Age column:", unique_Age)
print("Unique values in Vict_Sex column:", unique_sex)


# Basic statistics
statistics_data = {
    'Statistic': ['Total number of records', 'Unique locations', 'Unique crime codes',
                   'Unique descriptions', 'Unique ages', 'Unique sexes'],
    'Value': [total_records,unique_crime_location, unique_crime_code,
unique_crime_descrip, unique_Age, unique_sex]
}

# a DataFrame for unique columns
statistics_df = pd.DataFrame(statistics_data)
print(statistics_df)
print(statistics_df.describe())
# to get the actual statistics of crime_data like mean and count and standard deviation
print(crime_df.describe())



