import math
import os
import random
import re
import sys

if __name__ == '__main__':
    #s = input()
    s = 'I came from the moon. He went to the other room. She went to the drawing room. '
    s = s.strip().split('.')
    s = [snt.strip().lower() for snt in s if snt!='']
    print(s)
    word_list = []
    for sentence in s:
        words = sentence.split()
        temp_list = []
        iter = 3
        for w in range(len(words)):
            if w < (w + iter):
                temp_list.append(words[w+(iter-3)])
                temp_list.append(words[w+(iter-2)])
                temp_list.append(words[w+(iter-1)])
                word_list.append(temp_list)
                print(word_list)
                temp_list = []
                iter += 3

    #print(word_list)
