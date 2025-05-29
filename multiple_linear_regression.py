import sys
import numpy as np
from sklearn.linear_model import LinearRegression

in_data = sys.stdin.read().strip().split('\n')

lst = []
for i in in_data:
    lst.append(list(map(float, i.split())))

data = []
n = int(lst[0][1])
for i in range(1, n + 1):
    data.append(lst[i])
data = np.array(data)

x_train = data[:,:-1]
y_train = data[:,-1]

t = int(lst[n+1][0])
x_test = []
for i in range(n+2, n+2+t):
    x_test.append(lst[i])

x_test = np.array(x_test)

lr = LinearRegression()
lr.fit(x_train, y_train)
pred = lr.predict(x_test)

for i in pred:
    print(round(i,2))
