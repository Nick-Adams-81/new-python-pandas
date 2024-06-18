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
#   print(df.sort_values(['Type 1', 'HP'], ascending=[1,0]))


# Changing data
#   df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']
#   print(df.head(3))
# Drop a column
#df = df.drop(columns=['Total'])
print(df.head(3))
# Move column in print out
cols = list(df.columns.values)
df = df[cols[0:4] + [cols[-1]] + cols[4:12]]
print(df.head(3))
