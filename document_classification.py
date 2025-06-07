import sys
import pandas as pd

train = pd.read_csv('trainingdata.txt', header=None, names=['text'])
t = int(train.iloc[0][0])
train = train.iloc[1:]

train['labels'] = train['text'].apply(lambda x: int(x[0]))
train['text'] = train['text'].apply(lambda x: x[1:].strip())



print(train.tail())
