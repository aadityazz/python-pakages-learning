from sklearn import datasets, model_selection
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import pandas as pd

# Loading dataset
boston = datasets.load_boston()

# Storing data and test data given in the dataset
x = boston.data
y = boston.target

# Getting dataset grid
x.shape

# Getting dataframe of boston dataset data
df = pd.DataFrame(x)

# Getting header of dataset
print(boston.feature_name)

# Changing the colum,n name with feature name
df.columns = boston.feature_names
df.describe()

# To read the dataset
boston.DESCR

'-----------------------------------------------------------------'
# Training Algorithm

x_train, x_test, y_train, y_test = model_selection.train_test_split(x, y)
print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)

# Generating a variable giving it a pre-define algorithm
algl = LinearRegression()

# This will let our algo learn the data to predict
algl.fit(x_train, y_train)

# After training the algorithm now we will try to predict test dataset
y_pred = algl.predict(x_test)

# Now lets compare the prediction and the actual data
# We will use graph to compare it
plt.scatter(y_pred, y_test)
plt.axis(0, 40, 0, 40)
plt.show()
