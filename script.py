import pandas as pd

df1 = pd.read_csv('data/201701-citibike-tripdata.csv')
df1.head()


df1.rename(columns = {'Trip Duration': 'tripduration', 'Start Time': 'starttime', 
                      'Stop Time': 'stoptime', 'Gender':'gender', "User Type": "usertype",
                      'Bike ID': 'bikeid', 'Birth Year': 'birth year', 'Start Station ID': 'start station id',
                      'Start Station Name': 'start station name', 'Start Station Latitude': 'start station latitude',
                      'Start Station Longitude': 'start station longitude', 'End Station ID': 'end station id', 
                      'End Station Name': 'end station name', 'End Station Latitude': 'end station latitude',
                      'End Station Longitude': 'end station longitude'}, inplace = True)
df1.head()

df2.rename(columns = {'Trip Duration': 'tripduration', 'Start Time': 'starttime', 
                      'Stop Time': 'stoptime', 'Gender':'gender', "User Type": "usertype",
                      'Bike ID': 'bikeid', 'Birth Year': 'birth year', 'Start Station ID': 'start station id',
                      'Start Station Name': 'start station name', 'Start Station Latitude': 'start station latitude',
                      'Start Station Longitude': 'start station longitude', 'End Station ID': 'end station id', 
                      'End Station Name': 'end station name', 'End Station Latitude': 'end station latitude',
                      'End Station Longitude': 'end station longitude'}, inplace = True)
df2.head()

df3.rename(columns = {'Trip Duration': 'tripduration', 'Start Time': 'starttime', 
                      'Stop Time': 'stoptime', 'Gender':'gender', "User Type": "usertype",
                      'Bike ID': 'bikeid', 'Birth Year': 'birth year', 'Start Station ID': 'start station id',
                      'Start Station Name': 'start station name', 'Start Station Latitude': 'start station latitude',
                      'Start Station Longitude': 'start station longitude', 'End Station ID': 'end station id', 
                      'End Station Name': 'end station name', 'End Station Latitude': 'end station latitude',
                      'End Station Longitude': 'end station longitude'}, inplace = True)
df3.head()

df4 = pd.read_csv('data/201704-citibike-tripdata.csv')
df4.head()


df5 = pd.read_csv('data/201705-citibike-tripdata.csv')
df5.head()
