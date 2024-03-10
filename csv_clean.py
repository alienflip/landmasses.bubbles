# import pandas with shortcut 'pd'
import pandas as pd
import csv

# read_csv function which is used to read the required CSV file
# source: https://www.cia.gov/the-world-factbook/field/area/country-comparison/
data = pd.read_csv('landmass.csv')

# drop function which is used in removing or deleting rows or columns from the CSV files
data.drop('slug', inplace=True, axis=1)
data.drop('region', inplace=True, axis=1)
data.drop('ranking', inplace=True, axis=1)
data.drop('date_of_information', inplace=True, axis=1)

col_0 = data["name"]
col_1 = ["Origin" for i in range(col_0.shape[0])]
col_2 = data[" sq km"]

new_df = pd.DataFrame(col_0)
new_df["parent"] = col_1
new_df["value"] = col_2

new_df.loc[0] = "Origin", "", ""
new_df = new_df.sort_index().reset_index(drop=True)

new_df.to_csv('landmass_cleaned_0.csv')

# save cleaning step 1
with open('landmass_cleaned_0.csv', newline='\n') as csvfile:
    spamreader = csv.reader(csvfile)
    with open("landmass_cleaned_1.csv", "w") as file:
        writer = csv.writer(file, delimiter=',', quotechar='"')
        for row in spamreader:
            writer.writerow([row[1], row[2], row[3].replace(",",'')])