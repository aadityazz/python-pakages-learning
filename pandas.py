import pandas as pd

# It's better to use Jupyter Notebook

# Reading CSV File
iris = pd.read_csv("iris.data")

# Type of DataType of our DataSet
print(type(iris))

# Copying dataset to our variable
df = iris.copy()

# It will show the initial dataset (By Default it is 5)
df.head(3)

# Creating table header as a columns
df.columns = ['sl', 'sw', 'pl', 'pw', 'flower_type']

# Shows dimension of dataset (row X column)
print(df.shape)

# Showing datatype of each column
print(df.dtypes)

# Describing the data of dataset like mean, max, min, count, NaN etc etc...
df.describe()

# To get the specific column data from dataset
df["sl"]

# Get the datatype of that specific column
df.sl

# Check if there is any null entries or not
df.isnull()

# Check if that which column has how many entries
df.isnull().sum()

# To slice the dataset
df.iloc[1:4, 2:3]

# Manipulating Data from Dataset -->

# Copying tha dataset with removing specific element
a = df.drop(0)
a.head()

# If we want to remove that element in original database (The label 0 will also removed)
df.drop(0, inplace=True)
df.head()

# To look that the labels of dataset
df.index

# Label of 0th position
df.index(0)

# Checking if condition is true or false for a column
df.sl > 3

# It will only those row having value greater than 3
df[df.sl > 3]

# To get description of those rows having condition true
df[df.flower_type == 'Iris-section'].describe()

'''
Here is important thing to note is that iloc work based 
on data position on dataset and loc works based on label of the table
'''
df.loc[0]

# Add a row
df.loc[0] = {1, 2, 3, 4, "Iris-Section"}

# the row is added in the end is you want to verify we can simply do
df.tail()

'''
Here while add some data in the table the indexing is really bad 
to look so we need to rearrange them
'''
df.index

# To reset index we use
df.reset_index()

'''
This function will create a new column in the dataset named
index which is having value of really indexes
'''
# So to tackle above problem
df.reset_index(drop=True)

# A proper way to reset is
df.reset_index(drop=True, inplace=True)

# Deleting a column
df.drop('sl', axis=1)

# Another way to delete
del df["sw"]

# just getting original data back to df
df = iris.copy()
df.columns = ['sl', 'sw', 'pl', 'pw', 'flower-type']

# Adding column with some operations on existing column
df['diff_pl_pw'] = df["pl"] - df["pw"]

# Showing operation column only
df["pl"] - df["pw"]

# Handling NaN -->

# We can simply remove the NaN entry
df.dropna()

# The really doesn't change the df, to change it we can say
df.dropna(inplace=True)

# Now to make indexes in the correct order we can
df.reset_index(drop=True, inplace=True)

# If we want to fill NaN with other datas
df.sw.fillna(df.sw.mean(), inplace=True)

# A really nice way to fil data
df["Gender"] = "Female"
df.iloc[0:10, 6] = "Male"


def fun(s):
    if s == "Male":
        return 0
    else:
        return 1


df["sex"] = df.Gender.apply(fun)

del df["Gender"]
df.head()
