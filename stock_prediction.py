import sys
import math

data = sys.stdin.read().strip().split('\n')

lst = []
for i in data:
    lst.append(i.split())

m = lst[0][0]
k = int(lst[0][1])
d = lst[0][2]

for i in range(1, k+1):
    stocks = lst[i][0]
    buy_sell = int(lst[i][1])
    prices = list(map(float, lst[i][2:]))
    
