import sys
import pandas as pd
import numpy as np
from sklearn.metrics import root_mean_squared_error
import random

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
    
    val_list = []
    for i in range(len(temp)):
        for col in ['tmax', 'tmin']:
            if pd.isna(temp.at[i, col]):
                if (i != 0) and (i != (len(temp)-1)):
                    j = 0
                    while pd.isna(temp.at[i+j, col]):
                        j += 1
                    val = round((temp.at[i-1, col] + temp.at[i+j, col]) / 2, 1)
                    temp.at[i, col] = val
                    print(val)
                    val_list.append(val)
                else:
                    if i == 0:
                        monthly_avg = temp.groupby('month')[col].mean()
                        val = round(monthly_avg[temp.at[i, 'month']], 1)
                        temp.at[i, col] = val
                        print(val)
                        val_list.append(val)
                    else:
                        val = round(temp.at[i-1, col], 1)
                        temp.at[i, col] = val
                        print(val)
                        val_list.append(val)
    