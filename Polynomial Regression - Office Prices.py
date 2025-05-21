import sys
import numpy as np
import pandas as pd

lst = []
for line in sys.stdin:
    lst.append(line.strip().split())

lst.pop(0)
test = np.array(lst[-4:], dtype=float)
train = np.array(lst[:-5], dtype=float)

train_df = pd.DataFrame(train, columns=['f1', 'f2', 'y'])
test_df = pd.DataFrame(test, columns=['f1', 'f2'])

m1 = (train_df['f1']*train_df['y']).sum() / (train_df['f1']**2).sum()
m2 = (train_df['f2']*train_df['y']).sum() / (train_df['f1']**2).sum()

print(m1, '\n', m2)