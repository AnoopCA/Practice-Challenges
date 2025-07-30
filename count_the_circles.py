import sys
import numpy as np

data = sys.stdin.read().strip().split('\n')

pixels = [[[int(k) for k in j.split(',')] for j in i.split()] for i in data[1:]]

print(pixels)
