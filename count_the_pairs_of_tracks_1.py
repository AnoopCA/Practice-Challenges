import sys

#data = sys.stdin.read().strip().split('\n')
with open('pair_of_tracks_samples/sampleTest1.txt', 'r') as f:
    data = f.readlines()

r,c = data[0].split()
r,c = int(r), int(c)

pixels = []
for i in range(r):
    temp_px = data[i+1].strip().split()
    temp_px = [sum(int(q) for q in p.split(',')) for p in temp_px]
    pixels.append(temp_px)
    
for i in pixels:
    temp = ''
    for j in i:
        if j < 150:
            temp += '.'
        else:
            temp += '*'
    print(temp)
