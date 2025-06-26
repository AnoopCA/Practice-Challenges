import sys

data = sys.stdin.read().strip().split('\n')

pixels = [[int(k) for k in j.split(',')] for i in data for j in i.split()]
pixels_sum = [sum(i) for i in pixels]
pixels_count = [1 for i in pixels if sum(i) < 200]
percentage_dark = len(pixels_count) / len(pixels)

if percentage_dark > 0.40:
    print('night')
else:
    print('day')
