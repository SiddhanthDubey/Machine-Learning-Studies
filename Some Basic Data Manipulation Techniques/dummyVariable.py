import pandas as pd
df = pd.read_excel('carPrice.xlsx')

dummies = pd.get_dummies(df['Car Model'])

merged = pd.concat([df,dummies],axis='columns')

final = merged.drop(['Car Model','Mercedez Benz C class'],axis='columns')


X = final.drop('Sell Price($)',axis='columns')
Y = final['Sell Price($)']

from sklearn.linear_model import LinearRegression
model = LinearRegression()

model.fit(X.values, Y.values)

#print(model.score(X, Y))

print(model.predict([[45000,4,0,0]])) #Price of mercedez benz that is 4 yr old with mileage 45000