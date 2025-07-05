import sys
import numpy as np
import pandas as pd

if __name__ == "__main__":
    #data = sys.stdin.read().strip().split('\n')
    #data = [int(i) for i in data[1:]]

    with open('web_traffic_data.txt', 'r') as f:
        data = f.readlines()
    data = [int(i.strip()) for i in data[1:]]

    for w_check in range(2, 51):
        sma_list = []
        wma_list = []
        ewma_list = []
        for i in range(1, len(data)):
            w = w_check
            w_len = min(i, w)
            window_data = pd.Series(data[:i+1])

            sma = round(int(window_data.rolling(window=w_len).mean().iloc[-1]),1)
            sma_list.append(sma)
            
            weights = np.arange(1, min(i+1,w+1))
            wma = window_data.iloc[-w_len:] * weights
            wma = round(int(wma.sum() / weights.sum()),1)
            wma_list.append(wma)
            
            ewma = window_data.ewm(span=w_len, adjust=False).mean().iloc[-1]
            ewma = round(int(ewma),1)
            ewma_list.append(ewma)

        #print('data : sma  : wma  : ewma')
        #for i in range(len(data)-1):
        #    print(f'{data[i+1]} : {sma_list[i]} : {wma_list[i]} : {ewma_list[i]}')
        
        sma_err = []
        wma_err = []
        ewma_err = []
        for i in range(len(data)-1):
            sma_err.append(abs(data[i+1]-sma_list[i]))
            wma_err.append(abs(data[i+1]-wma_list[i]))
            ewma_err.append(abs(data[i+1]-ewma_list[i]))

        print(f'w: {w} sma: {round(sum(sma_err)/len(sma_err))} wma: {round(sum(wma_err)/len(wma_err))} ewma: {round(sum(ewma_err)/len(ewma_err))}')
