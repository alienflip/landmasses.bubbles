# import pandas with shortcut 'pd'
import pandas as pd
import csv

# read_csv function which is used to read the required CSV file
# source: https://www.cia.gov/the-world-factbook/field/area/country-comparison/
df = pd.read_csv('Area.csv', thousands=',')

# drop function which is used in removing or deleting rows or columns from the CSV files
df.drop('slug', inplace=True, axis=1)
df.drop('ranking', inplace=True, axis=1)
df.drop('date_of_information', inplace=True, axis=1)

new_df = pd.DataFrame()
new_df["region"] = df["region"].astype(str)
new_df["subregion"] = ["Mother Earth" for i in range(df["region"].shape[0])]
new_df["key"] = df["name"].astype(str)
new_df["value"] = df[" sq km"].astype(int)

new_df.to_csv('landmasses_cleaned.csv', index=False, sep=";", quotechar='"', quoting=csv.QUOTE_NONNUMERIC)