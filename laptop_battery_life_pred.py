import pandas as pd
import numpy as np

if __name__ == '__main__':
    timeCharged = float(input().strip())
    data = pd.read_csv('trainingdata.txt', header=None, names=["TimeCharged", "TimeLasted"])
    data = data[data['TimeCharged']<=4.01]

    A = np.array(data['TimeCharged']).reshape(-1,1)
    Y = np.array(data['TimeLasted']).reshape(-1,1) 
    beta_params = np.linalg.inv(A.T @ A) @ A.T @ Y

    if timeCharged > 4.01:
        print(8)  
    else:
        predicted_time = timeCharged *  beta_params[0][0]
        print(predicted_time)
