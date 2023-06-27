from sklearn.model_selection import train_test_split
from sklearn import linear_model
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
ds = pd.read_csv('test.csv')
X = np.array(ds.area)
Y = np.array(ds.peri)
plt.scatter(X, Y)


reg = linear_model.LinearRegression()

reg.fit([X], Y.values)
# First argument has to be 2D array
print(X_test)
plt.plot([X_train[:]], y_train.values)
# Now the machine will predict
#print(reg.predict([X_test]))
