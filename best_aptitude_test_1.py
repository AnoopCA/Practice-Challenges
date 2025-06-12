import sys
import numpy as np
from scipy.stats import linregress

data = sys.stdin.read().strip().split('\n')
#data = ['1', '5', '7.5 7.7 7.9 8.1 8.3', '10 30 20 40 50', '11 9 5 19 29', '21 9 15 19 39', '91 9 75 19 89', '81 99 55 59 89']
t = int(data[0])

l = 0
for i in range(t):
    n = int(data[i+1+l])
    scores = []
    gpa = [float(j) for j in data[i+2+l].split()]
    gpa = np.array(gpa)
    for k in range(i+3+l, i+3+l+n):
        scores.append([float(m) for m in data[k].split()])
    scores = np.array(scores)
    l += 7

    sorted_indices = np.argsort(gpa)
    gpa = gpa[sorted_indices]
    slopes = []
    scores = scores[:, sorted_indices]
    
    for col in scores:
        slope,_,_,_,_ = linregress(range(len(col)), col)
        slopes.append(slope)
    print(slopes.index(max(slopes))+1)
