import sys
import numpy as np
from sklearn.linear_model import Linear_Regression

in_data = sys.stdin.read().strip().split('\n')

lst = []
for i in in_data:
    lst.append(list(map(float, i.split())))

data = []
for i in range(1, int(lst[0][1]) + 1):
    data.append(lst[i])
data = np.array(data)

x_train = data[:,:-1]
y_train = data[:,-1]

for i in range(int(lst[0][1])+2, int(lst[0][1])+2+


print(x, '\n', y)
