import sys
import numpy as np
import pandas as pd

if __name__ == "__main__":
    #data = sys.stdin.read().strip().split('\n')
    #n = int(data[0])
    #data = [int(i) for i in data[1:]]

    with open('web_traffic_data.txt', 'r') as f:
        data = f.readlines()
    n = int(data[0])
    data = [int(i.strip()) for i in data[1:]]

    sma_list = []
    wma_list = []
    ewma_list = []
    for i in range(1, 31): #len(data)):
        w = 90
        w_len = min(i, w)
        window_data = pd.Series(data[n-w:n-w+i+1])
        print(len(window_data))
        weights = np.arange(1, min(i+1,w+1))
        wma = window_data.iloc[-w_len:] * weights
        wma = round(int(wma.sum() / weights.sum()),1)
        #wma_list.append(wma)
        data.append(wma)
        data.pop(0)
        #print(data[-1])