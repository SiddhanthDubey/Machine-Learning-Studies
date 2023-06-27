from sklearn import linear_model
import matplotlib.pyplot as plt
import pandas as pd

ds = pd.read_csv('test.csv')
#X = np.array(ds.x)
#Y = np.array(ds.y)
#plt.scatter(X, Y)

reg = linear_model.LinearRegression()

reg.fit(ds[['area']].values, ds.peri.values)
# First argument has to be 2D array

# Now the machine will predict
test = [[12]]
print(reg.predict(test))
plt.plot(ds[['area']].values, reg.predict(ds[['area']].values))
plt.show()
