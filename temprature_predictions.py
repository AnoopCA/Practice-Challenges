import sys
import pandas as pd


if __name__ == "__main__":
    data = sys.stdin.read().strip().split('\n')
    
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
    
    print(temp['tmax'].value_counts(dropna=False))
    print(temp['tmin'].value_counts(dropna=False))
    
    #print(temp[temp['yyyy'].isin([1929])]) - only October, November and December data available for the year 1929.
