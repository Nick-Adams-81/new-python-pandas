import pandas as pd

# importing the csv file with the data
df = pd.read_csv('./poke.data.csv')

# Read headers
#   print(df.columns)

# Describe the data in dataframe
#   print(df.describe())

# Read each column
#   names = df[['Name', 'Type 1', 'HP']][0:3]
#   print(names)

# Read each row
#     print(df.iloc)

# Itterate through all rows and get index
#for index, row in df.iterrows():
    #print(index, row['Name'])

# Get item by field in dataset
#    print(df.loc[df['Type 1'] =='Fire'])

# Sorting by 1 field in data 
#   print(df.sort_values('Name'))
# Sorting by multiple fields in data
print(df.sort_values(['Type 1', 'HP'], ascending=[1,0]))