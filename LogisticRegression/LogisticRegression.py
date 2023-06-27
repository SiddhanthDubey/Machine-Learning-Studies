import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split

df = pd.read_excel('insurance_data.xlsx')
print(df.head())

plt.scatter(df.age,df.bought_insurance, marker='*',color='black')
plt.show()

x_train, x_test, y_train, y_test =train_test_split(df[['age']],df.bought_insurance,test_size=0.1)

print(x_test)

model = LogisticRegression()
model.fit(x_train,y_train)

print(model.predict(x_test))

print(model.score(x_test,y_test))