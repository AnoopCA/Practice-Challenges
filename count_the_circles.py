import sys
import numpy as np

#data = sys.stdin.read().strip().split('\n')
with open('count_the_circles_test_cases.txt', 'r') as f:
    data = f.readlines()

pixels = [[int(sum(int(k) for k in j.split(','))/3) for j in i.split()] for i in data[1:]]

pxl_lst = []

for i in pixels:
    temp_list = []
    for j in i:
        if j < 200:
            temp_list.append(1)
        else:
            temp_list.append(0)
    pxl_lst.append(temp_list)

#with open('text_out.txt', 'w') as f:
#    for l in idx_lst:
#        line = ''.join(str(i) for i in l)
#        f.write(line + '\n')

circle_list = []
for idx_row,row in enumerate(pxl_lst):
    temp_lst = []
    for idx_col,pxl in enumerate(row):
        if pxl == 1:
            temp_lst.append(idx_col)
    if temp_lst:
        top_idx = temp_lst[len(temp_lst)//2]
        for temp_col in range(idx_row, len(pxl_lst)):
            if circle_list:
                for rw,cl in circle_list:
                    if (rw == top_idx) and (cl < temp_col):
                        break
            if pxl_lst[temp_col][top_idx] == 0:
                circle_list.append((top_idx, temp_col))
                break
circle_list = list(set(circle_list))

for i in circle_list:
    print(i)
