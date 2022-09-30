import pandas as pd
import numpy as np

# #1 Reading a CSV file 
# # Reading a CSV file
# file = 'file.csv'
# df = pd.read_csv(file)

# Changing Delimitter
# symbol = '|'
# df = pd.read_csv(file, sep = symbol)

###############################################################################

# #2 Saving a DataFrame to a CSV file
# # Saving CSV
# df.to_csv(file)

# Changing Delimitter while saving
# symbol = '|'
# df.to_csv(file, sep = symbol)

###############################################################################

# #3 Creating a DataFrame from a list of lists
data = [[1, 2, 3], [4, 5, 6]]
df = pd.DataFrame(data, columns = ['A', 'B', 'C'])

###############################################################################

# # 4 Creating a DataFrame from a dictionary
# data = {'A': [1, 2], 'B': [3, 4]}
# df = pd.DataFrame(data)

###############################################################################

# # 5 Merging DataFrames
# df1 = pd.DataFrame([[1, 'A'], [2, 'B']], columns = ['col1', 'col2'])
# df2 = pd.DataFrame([['A', 3], ['B', 4]], columns = ['col2', 'col3']) 
# df = pd.merge(df1, df2, on = 'col2', how = 'inner')

###############################################################################

# # 6 Sorting a DataFrame
# df = pd.DataFrame([[2, 'A'], [3, 'B'],[1, 'C']], columns = ['col1', 'col2'])
# df_sort = df.sort_values(by = 'col1')

###############################################################################

# # 7 Concatenating DataFrames
# df1 = pd.DataFrame([[1, 'A'], [2, 'B']], columns = ['col1', 'col2'])
# df2 = pd.DataFrame([['A', 3], ['B', 4]], columns = ['col3', 'col4'])
# df = pd.concat((df1, df2), axis = 1)

###############################################################################

# # 8 Rename column name
# df = pd.DataFrame([[1, 'A'], [2, 'B']], columns = ['col1', 'col2'])
# df_renamed = df.rename(columns  = {'col1': 'col3', 'col2': 'col4'})

###############################################################################

# # 9 Add New Column
# df = pd.DataFrame([[1, 'A'], [2, 'B']], columns = ['col1', 'col2'])
# df['col3'] = df['col1'] + 2

###############################################################################

# # 10 Filter DataFrame based on condition
# df = pd.DataFrame([[1, 'A'], [2, 'B'], [2, 'A'] , [3, 'C']], columns = ['col1', 'col2'])
# filter_1 = df[df.col1 > 1]

# filter from list
# filter_list = [1, 2]
# filter_2 = df[df.col1.isin(filter_list)]

###############################################################################

# # 11 Drop Column
# df = pd.DataFrame([[1, 'A'], [2, 'B']], columns = ['col1', 'col2'])
# df_new = df.drop(columns = ['col2'])

###############################################################################

# # 12 GroupBy
# df = pd.DataFrame([[1, 'A'], [2, 'B'], [3, 'C'], [4, 'C']], columns = ['col1', 'col2'])
# print(df.groupby('col2').col1.sum())

###############################################################################

# # 13 Unique Values in a column
# df = pd.DataFrame([[1, 'A'], [2, 'B'], [3, 'A'], [4, 'C']], columns = ['col1', 'col2'])

# # Print Unique Values
# print(df.col2.unique())

# # Number of unique values
# print(df.col2.nunique())

###############################################################################

# # 14 Fill NaN values
# df = pd.DataFrame([[1, 'A'], [2, np.nan], [3, np.nan]], columns = ['col1', 'col2'])
# df.col2.fillna('B', inplace = True)

###############################################################################

# # 15 Apply Function on a column

# def f(number):
#     return number + 2


# df = pd.DataFrame([[1, 'A'], [2, 'B']], columns = ['col1', 'col2'])
# df['col3'] = df.col1.apply(f)

###############################################################################

# # 16 Remove Duplicates

# df = pd.DataFrame([[1, 'A'], [2, 'B'], [1, 'A']], columns = ['col1', 'col2'])
# df_new= df.drop_duplicates()

###############################################################################

# # 17 Value Counts

# df = pd.DataFrame([[1, 'A'], [2, 'B'], [2, 'A'], [3, 'C']], columns = ['col1', 'col2'])
# print(df.col2.value_counts())

###############################################################################

# # 18 Size of a DataFrame
# df = pd.DataFrame([[1, 'A'], [2, 'B'], [2, 'A'], [3, 'C']], columns = ['col1', 'col2'])
# print(df.shape)

