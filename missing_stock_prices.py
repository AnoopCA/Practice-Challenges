import sys
import numpy as np
import pandas as pd
from datetime import datetime

if __name__ == "__main__":
    in_data = sys.stdin.read().strip().split('\n')
    n = int(in_data[0])
    data = [i.split() for i in in_data[1:]]
    
    data = [[datetime.strptime(i[0].strip(),'%m/%d/%Y').strftime('%m-%d-%Y'),
             datetime.strptime(i[1],'%H:%M:%S').strftime('%H:%M:%S'),
             float(i[2]) if (i[2][:7])!='Missing' else np.nan] for i in data]
    
    data = pd.DataFrame(data, columns=['date', 'time', 'stock_price'])
    data_filled = data.copy()

    data_filled['stock_price'] = data_filled['stock_price'].interpolate(method='cubic', limit_direction='both')
    data_filled['stock_price'] = data_filled['stock_price'].round(3)

    for nan_row in range(len(data)):
        if pd.isna(data.at[nan_row, 'stock_price']):
            print(data_filled.at[nan_row, 'stock_price'])
