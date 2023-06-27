import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
pageSpeeds = np.random.normal(3.0,1.0,1000)
purchaseAmount = np.random.normal(50.0,30.0,1000)/pageSpeeds
# plt.scatter(pageSpeeds,purchaseAmount)
# plt.show()

trainX = pageSpeeds[:800]
testX = pageSpeeds[800:]

trainY = purchaseAmount[:800]
testY = purchaseAmount[800:]

plt.scatter(trainX,trainY)

x = np.array(trainX)
y = np.array(trainY)

polyR = np.poly1d(np.polyfit(x,y,2))

xp = np.linspace(0,700,1000)
axes = plt.axes()
axes.set_xlim([0,7])
axes.set_ylim([0,200])

plt.scatter(testX,testY)
plt.plot(xp,polyR(xp),c='r')
plt.show()

r2 = r2_score(testY,polyR(testX))
print(r2)