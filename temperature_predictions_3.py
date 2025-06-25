import sys
import pandas as pd
import numpy as np

if __name__ == "__main__":
    data = sys.stdin.read().strip().split('\n')
    #with open('temperature_predictions_in.txt', 'r') as f:
    #    data = f.readlines()
    yyyy = []
    month = []
    tmax = []
    tmin = []
    for i in data[2:]:
        y,m,tx,tn = i.split('\t')
        yyyy.append(int(y))
        month.append(m)
        if tx[0] == 'M':
            tmax.append(np.nan)
        else:
            tmax.append(float(tx))
        if tn[0] == 'M':
            tmin.append(np.nan)
        else:
            tmin.append(float(tn))
    
    temp = {'yyyy':yyyy, 'month':month, 'tmax':tmax, 'tmin':tmin}
    temp = pd.DataFrame(temp)
    temp_filled = temp.copy()

    temp_filled[['tmax', 'tmin']] = temp_filled[['tmax', 'tmin']].interpolate(method='cubic', limit_direction='both')
    temp_filled[['tmax', 'tmin']] = temp_filled[['tmax', 'tmin']].round(1)

    val_list = []
    for i in range(len(temp)):
        for col in ['tmax', 'tmin']:
            if pd.isna(temp.at[i, col]):
                print(temp_filled.at[i, col])
    
