import pandas as pd
import matplotlib.pyplot as plt
import pymysql
import seaborn as sns
import folium
import warnings
warnings.filterwarnings("ignore", message= "pandas only supports SQLAlchemy connectable (engine/connection) or "
                                           "database string URI or sqlite3 DBAPI2 connection. Other DBAPI2 objects "
                                           "are not tested. Please consider using SQLAlchemy.")

connection=pymysql.connect(host='localhost',user='root',password='Pallu@834',database='Project')
crime_df = pd.read_sql("select * from crime_data",connection)

# Created a base map and centered at an average location
crime_map = folium.Map(location=[crime_df['LAT'].mean(), crime_df['LON'].mean()], zoom_start=10)

# Adding  crime data points to the map
for index, row in crime_df.iterrows():
    # Set the  marker color to blue
    marker_color = 'blue'

    # Changing marker color based on the type of crime
    if row['Crm_Cd_Desc'] == 'BURGLARY FROM VEHICLE':
        marker_color = 'darkred'
    elif row['Crm_Cd_Desc'] == 'BATTERY -SAMPLE ASSAULT':
        marker_color = 'darkgreen'
    elif row['Crm_Cd_Desc'] == 'THEFT PLAIN - PETTY ($950 & UNDER)' or \
         row['Crm_Cd_Desc'] == 'SHOPLIFTING - PETTY THEFT ($950 & UNDER)' or \
         row['Crm_Cd_Desc'] == 'VEHICLE - STOLEN' or \
         row['Crm_Cd_Desc'] == 'THEFT-GRAND ($950.01 & OVER)EXCPT,GUNS,FOWL,LIVESTK,PROD':
        marker_color = 'orange'
    elif row['Crm_Cd_Desc'] == 'VANDALISM - FELONY ($400 & OVER, ALL CHURCH VANDALISMS)' or \
         row['Crm_Cd_Desc'] == 'ASSAULT WITH DEADLY WEAPON, AGGRAVATED ASSAULT' or \
         row['Crm_Cd_Desc'] == 'VANDALISM - MISDEMEANOR ($399 OR UNDER)' or \
         row['Crm_Cd_Desc'] == 'TRESPASSING':
        marker_color = 'darkblue'

    # Adding the  marker with latitude and longitude
    folium.Marker(location=[row['LAT'], row['LON']],
                  popup=f"Latitude: {row['LAT']}, Longitude: {row['LON']}",
                  icon=folium.Icon(color=marker_color)).add_to(crime_map)

# the map was saved to an HTML file
crime_map.save('crime_hotspots_map.html')


#From this what i have observed was
#from Hydepark to glendale (in that distribution) are  crime hostpots areas which are proned to crimes