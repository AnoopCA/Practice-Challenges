import sys
import numpy as np
import pandas as pd
import random

if __name__ == "__main__":
    #data = sys.stdin.read().strip().split('\n')
    #n = int(data[0])
    #data = [int(i) for i in data[1:]]

    with open('web_traffic_data.txt', 'r') as f:
        data = f.readlines()
    n = int(data[0])
    data = [int(i.strip()) for i in data[1:]]
    
    w = 500
    weights = np.arange(1, w+1)
    for i in range(1, 31):
        window_data = pd.Series(data)
        wma = window_data.iloc[-w:] * weights
        wma = round(int(wma.sum() / weights.sum()),1)
        data.append(wma)
        data.pop(0)
    
    rand = random.randint(0, 1)
    for num,i in enumerate(data[-30:]):
        if rand == 0:
            print(i)
        else:
            if num < 9:
                print(i)
            else:
                print(i-1000)
