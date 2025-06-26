import os
import sys
import numpy as np


if __name__ == "__main__":
    #data = sys.stdin.read().split('\n')
    in_path = r"D:\ML_Projects\Practice-Challenges\sampleCaptchas\input"    # input00.txt
    out_path = r"D:\ML_Projects\Practice-Challenges\sampleCaptchas\output"  # output00.txt
    for num in range(25):
        f_num = f"{num:02}"
        for file_name in os.listdir(in_path):
            file_path = os.path.join(in_path, "input" + f_num + ".txt")
            if os.path.isfile(file_path):
                with open(file_path, 'r') as f:
                    data = f.readlines()                
                r,c = data[0].split()
                r,c = int(r),int(c)
                pixels = [[sum([int(k) for k in j.split(',')]) for j in i.split()] for i in data[1:r+1]]
                pixels = np.array(pixels)
                temp_list = []
                for row in pixels:
                    temp = ''
                    for col in row:
                        if col > 400:
                            temp += str('*')
                        else:
                            temp += str('.')
                    if set(temp) != {"*"}:
                        temp_list.append(temp)
                        print(temp)
                print('-')
                char_dict = {1:[], 2:[], 3:[], 4:[], 5:[]}
                for cap_row in temp_list:
                    start = 5
                    end = start + 9
                    for i in char_dict:
                        char_dict[i].append(cap_row[start:end])
                        start = end
                        end += 9
                #print(char_dict)
                break
        break
