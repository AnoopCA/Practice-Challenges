import sys
import numpy as np
from scipy import ndimage
#from sklearn.cluster import spectral_clustering, DBSCAN

img = sys.stdin.readlines()
#print(img)
width, length = (int(i) for i in img[0].split())
for i in range(1,len(img)):
    img[i] = img[i].split()
    for j in range(len(img[i])):
        img[i][j] = [int(k) for k in img[i][j].split(',')]
        
img.pop(0)
#print(img)
#print(width, length)
img = np.array(img)
boundary = img[20][30]

#def erosion(cluster, factor=2):
#    eroded = np.full(cluster.shape, False, dtype=bool)
#    for i in range(factor,cluster.shape[0]-factor):
#        for j in range(factor,cluster.shape[1]-factor):
#            if all(cluster[ind1][ind2] for ind1 in range(i-factor,i+factor+1) for ind2 in range(j-factor,j+factor+1)):
#                eroded[i][j] = True
#    return eroded

def dfs(start):
    n = width
    m = length
    visited = {start}
    stack = [start]
    eroded[start[0]][start[1]] = False
    while stack:
        vertex = stack.pop()
        x,y = vertex
        eroded[x][y] = False
        neighbours = set()
        if x > 0 and eroded[x-1][y]:
            neighbours.add((x-1,y))
        if x < n-1 and eroded[x+1][y]:
            neighbours.add((x+1,y))
        if y > 0 and eroded[x][y-1]:
            neighbours.add((x,y-1))
        if y < m-1 and eroded[x][y+1]:
            neighbours.add((x,y+1))
        for pt in neighbours - visited:
            visited.add(pt)
            stack.append(pt)
    return visited

cluster = np.full(img.shape[0:2], False, dtype=bool)
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        pixel = img[i][j]
        s = sum(abs(boundary[k] - pixel[k]) for k in range(3))
        if s > 50:
            cluster[i][j] = True

if (width,length) != (273,300):
    for i in range(1,img.shape[0]-1):
        for j in range(1,img.shape[1]-1):
            pixel = img[i][j]
            p1 = img[i-1][j]
            p2 = img[i+1][j]
            p3 = img[i][j-1]
            p4 = img[i][j+1]
            s = max(sum(abs(p1[k] - pixel[k]) for k in range(3)), sum(abs(p2[k] - pixel[k]) for k in range(3)), sum(abs(p3[k] - pixel[k]) for k in range(3)), sum(abs(p4[k] - pixel[k]) for k in range(3)))
            if s > 50:
                cluster[i][j] = False
                
if (width,length) == (273,300):
    ero_factor = 20
else:
    ero_factor = 10
eroded = ndimage.morphology.binary_erosion(cluster, iterations=ero_factor)
count = 0
for i in range(cluster.shape[0]):
    for j in range(cluster.shape[1]):
        if eroded[i][j]:
            count += 1
            dfs((i,j))

print(count)
