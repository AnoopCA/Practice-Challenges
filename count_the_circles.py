import sys
import numpy as np

#data = sys.stdin.read().strip().split('\n')
with open('count_the_circles_test_cases.txt', 'r') as f:
    data = f.readlines()

pixels = [[int(sum(int(k) for k in j.split(','))/3) for j in i.split()] for i in data[1:]]

idx_lst = []

for i in pixels:
    temp_list = []
    for j in i:
        if j < 200:
            temp_list.append(1)
        else:
            temp_list.append(0)
    idx_lst.append(temp_list)

for idx_1,row in enumerate(idx_lst):
    temp_lst = []
    for idx_2,elem in enumerate(row):
        if elem == 1:
            temp_lst.append(idx_2)
    if temp_lst:
        print(temp_lst[len(temp_lst)//2])
