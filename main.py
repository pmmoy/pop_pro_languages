import pandas as pd
import matplotlib.pyplot as pit

# Reads the csv and gives new column names to headers
df = pd.read_csv("QueryResults.csv", names=['DATE', 'TAG', 'POSTS'], header = 0)

#prints dataframe df
df

#detects missing values in the dataframe
df.isna()

#Drops all the entries that have NAN as a value and assigns to a new dataframe object
clean_df = df.dropna()

#finds what programming language had the most posts on Stackoverflow
clean_df.max()


#shows how many posts per language were made since the beginning of stackoverflow
clean_df.groupby('TAG').sum()

#Counts how many posts were made per language per month
clean_df.groupby('TAG').count()


#Cleaning date column to look more presentable by converting the current type 'Str' to a datetime format
df['DATE'][1]
print(pd.to_datetime(df.DATE[1]))
type(df['DATE'][1])

#converts the date column into a datetime format getting rid of the 00:00
df.DATE = pd.to_datetime(df.DATE)
df


#creates a pivot table chart using the pivot function 
reshaped_df = clean_df.pivot(index='DATE', columns='TAG', values = 'POSTS')
reshaped_df


#counts the entries per language NOTE: THIS EXCLUDES THE NAN
reshaped_df.count()

#Cleaning up dataframe to replace the NANS with '0'
reshaped_df.fillna(0, inplace=True)

reshaped_df

#checks if any values that are NAN are left
reshaped_df.isna().values.any()

#plots the dataframe "reshaped_df" to show the trend of Java
#Changes the size of the chart
pit.figure(figsize = (16,10))
pit.plot(reshaped_df.index, reshaped_df.java)


#plots the dataframe using java and python trends
#changes the fontsize of ticks on the chart
#places labels on the x and y axis to show data types
pit.figure(figsize = (16,10))
pit.xticks(fontsize=14)
pit.yticks(fontsize=14)
pit.xlabel('Date', fontsize=14)
pit.ylabel('Number of Posts', fontsize = 14)
pit.ylim(0, 35000)
pit.plot(reshaped_df.index, reshaped_df.java)
pit.plot(reshaped_df.index, reshaped_df.python)

#plots all the programming languages from the "reshaped_df" dataframe
pit.figure(figsize = (16,10))
pit.xticks(fontsize=14)
pit.yticks(fontsize=14)
pit.xlabel('Date', fontsize=14)
pit.ylabel('Number of Posts', fontsize = 14)
pit.ylim(0, 35000)

#Use for loop to iterate through the columns and plots the trends on the chart
for column in reshaped_df.columns:
  pit.plot(reshaped_df.index,reshaped_df[column], linewidth=3, label=reshaped_df[column].name)

#shows legend of lines to inspect data properly
pit.legend(fontsize=16)


#Calculating the roll/mean, which is a sweet spot for an average
roll_df = reshaped_df.rolling(window=6).mean()

pit.figure(figsize = (16,10))
pit.xticks(fontsize=14)
pit.yticks(fontsize=14)
pit.xlabel('Date', fontsize=14)
pit.ylabel('Number of Posts', fontsize = 14)
pit.ylim(0, 35000)

for column in roll_df.columns:
  pit.plot(roll_df.index,roll_df[column], linewidth= 3, label=roll_df[column].name)

pit.legend(fontsize=16)


