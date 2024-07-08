# the distribution of reported crimes based on Crime_Code@status
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import pymysql
import warnings
warnings.filterwarnings("ignore", message= "pandas only supports SQLAlchemy connectable (engine/connection) or "
                                           "database string URI or sqlite3 DBAPI2 connection. Other DBAPI2 objects "
                                           "are not tested. Please consider using SQLAlchemy.")
connection=pymysql.connect(host='localhost',user='root',password='Password',database='Project')
crime_df = pd.read_sql("select * from crime_data",connection)
# grouping the data by crimecode@status@crime_description(counting the occurrences of each unique value)
code_distribution=crime_df[['Crm_Cd','Status','Crm_Cd_Desc']].value_counts()
print(code_distribution)
# for plotting the graph  i have chosen count plot  for this and categorized based on status
plt.figure(figsize=(12,6))
sns.countplot(data=crime_df,x='Crm_Cd',hue='Status',palette='dark')
plt.title("Distribution Of Reported Crimes based on Crime codes and Status")
plt.xlabel("Crime Code")
plt.ylabel("Count of reported Crimes")
# rotating axis for readability
plt.xticks(rotation=45,ha='right')
# adding the legend with title
plt.legend(title='status')
# adjusting the layout
plt.tight_layout()
plt.show()
