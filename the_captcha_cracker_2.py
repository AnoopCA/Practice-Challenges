import os
import sys
import numpy as np

if __name__ == "__main__":
    #data = sys.stdin.read().split('\n')
    in_path = r"D:\ML_Projects\Practice-Challenges\sampleCaptchas\input"    # input00.txt
    out_path = r"D:\ML_Projects\Practice-Challenges\sampleCaptchas\output"  # output00.txt
    char_dict = {}
    char_map_num = 0
    for file_num in range(25):
        f_num = f"{file_num:02}"
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
                    temp_list.append(temp[5:50])
                    #print(temp[5:50])
            #print('-')
            for cap_row in temp_list:
                start = 0
                end = start + 9
                for i in range(5):
                    key = f"{char_map_num}_{i}"
                    if key not in char_dict:
                        char_dict[key] = []
                    char_dict[key].append(cap_row[start:end])
                    start = end
                    end += 9
            char_map_num += 1
            for key,value in char_dict.items():
                for ltr in value:
                    print(ltr)
                print('-')
        break

    captcha_list = []
    for file_num in range(25):
        f_num = f"{file_num:02}"
        file_path = os.path.join(out_path, 'output' + f_num + '.txt')
        if os.path.isfile(file_path):
            with open(file_path, 'r') as file:
                captcha_list.append(file.readline().strip())
    captcha_chars = []
    for word in captcha_list:
        for letter in list(word):
            captcha_chars.append(letter)
    char_list = sorted(list(set(captcha_chars)))
    #print(char_list)
