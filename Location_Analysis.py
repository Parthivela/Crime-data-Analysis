import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pymysql
connection=pymysql.connect(host='localhost',user='root',password='Password',database='Project')
crime_df = pd.read_sql("select * from crime_data",connection)

# to get location counts we have to use group by
unique_locations=crime_df['Location'].unique()
crime_counts=crime_df.groupby('Location').size()

# sorting the location based on crimes
crime_counts_sorted=crime_counts.sort_values(ascending=False)

# print the top 10 locations
print("Most crime Locations:")
print(crime_counts_sorted.head(10))

# plot the graph i have choosed bar graph to plot the visualization
top_locations=crime_counts_sorted.head(10)
plt.figure(figsize=(10,6))
top_locations.plot(kind='bar',edgecolor='Yellow',facecolor='skyblue',linewidth=2)
plt.title("Top 10 Locations of Most Crimes")
plt.xlabel('Location')
plt.ylabel("Number of Crimes")
# its for better readability
plt.xticks(rotation=45,ha="right")
# it will adjust the layout
plt.tight_layout()
plt.show()
