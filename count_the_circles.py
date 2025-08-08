import sys

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
    temp_lst_1 = []
    for idx_col,pxl in enumerate(row):
        if pxl == 1:
            temp_lst_1.append(idx_col)
    if temp_lst_1:
        temp_lst_2 = []
        # top_idx_lst contains the mid index of the topmost row of every circles, occurring one per row
        top_idx_lst = []
        while(temp_lst_1):
            if len(temp_lst_1) == 1:
                temp_lst_2.append(temp_lst_1.pop(0))
                top_idx_lst.append(temp_lst_2[len(temp_lst_2)//2])
            elif (temp_lst_1[0] + 1) == temp_lst_1[1]:
                temp_lst_2.append(temp_lst_1.pop(0))
            else:
                temp_lst_2.append(temp_lst_1.pop(0))
                top_idx_lst.append(temp_lst_2[len(temp_lst_2)//2])
                temp_lst_2 = []
        
        for top_idx in top_idx_lst:
            for crnt_rw in range(idx_row, len(pxl_lst)):
                if (pxl_lst[crnt_rw][top_idx] == 0) or (crnt_rw == len(pxl_lst)-1):
                    circle_list.append((crnt_rw, top_idx))
                    break

circle_list = sorted(list(set(circle_list)))

circles = []
for i in range(len(circle_list)):
    if i == 0:
        circles.append(circle_list[i])
    elif circle_list[i-1][0] == circle_list[i][0]:
        if abs(circle_list[i-1][1] - circle_list[i][1]) > 3:
            circles.append(circle_list[i])
    else:
        circles.append(circle_list[i])

print(len(circles))
