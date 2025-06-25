import sys
import pandas as pd
import numpy as np
from sklearn.metrics import root_mean_squared_error

if __name__ == "__main__":
    #data = sys.stdin.read().strip().split('\n')
    with open('temperature_predictions_in.txt', 'r') as f:
        data = f.readlines()
    yyyy = []
    month = []
    tmax = []
    tmin = []
    for i in data[2:]:
        y,m,tx,tn = i.split('\t')
        yyyy.append(int(y))
        month.append(m)
        if tx[0] == 'M':
            tmax.append(pd.NA)
        else:
            tmax.append(float(tx))
        if tn[0] == 'M':
            tmin.append(pd.NA)
        else:
            tmin.append(float(tn))
    
    temp = {'yyyy':yyyy, 'month':month, 'tmax':tmax, 'tmin':tmin}
    temp = pd.DataFrame(temp)
    
    ewma_list = []
    for i in range(2, len(temp['tmax'])-1):
        for col in ['tmax', 'tmin']:
            if pd.isna(temp.at[i+1, col]):
                w = min(i, 10)
                window_data = temp[col][:i]
                ewma = window_data.ewm(span=w, adjust=False).mean().iloc[-1]
                ewma = round(float(ewma),1)
                temp.at[i+1, col] = ewma
                print(ewma)
                ewma_list.append(ewma)

    #with open('temperature_predictions_out.txt', 'r') as f:
    #    out = [float(k.strip()) for k in f]
    #print(f'ewma: {root_mean_squared_error(out, ewma_list)}')
