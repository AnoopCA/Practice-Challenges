import numpy as np
from scipy.stats import mode

def floodFill4(image, sr, sc, newColor):
    dxs = [1, 0, -1, 0]
    dys = [0, 1, 0, -1]
    queue = [(sr, sc)]
    oldColor = image[sr][sc]
    image[sr][sc] = newColor
    while queue:
        x, y = queue.pop(0)
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(image) and 0 <= ny < len(image[0]):
                if image[nx][ny] != newColor and image[nx][ny] == oldColor:
                    image[nx][ny] = newColor
                    queue.append((nx, ny))
    #return image
    return ''

def drawcircle(myGrid, x0, y0, radius, myVal, R, C):
    x = radius-1
    y = 0
    dx = 1
    dy = 1
    err = dx - (radius *2 )
    while (x >= y):
        if x0 + x < R and y0 + y < C: myGrid[x0 + x, y0 + y] = myVal
        if x0 + y < R and y0 + x < C: myGrid[x0 + y, y0 + x] = myVal
        if x0 - y >0 and y0 + x < C: myGrid[x0 - y, y0 + x] = myVal
        if x0 - x >0 and y0 + y < C: myGrid[x0 - x, y0 + y] = myVal
        if x0 - x >0 and y0 - y >0: myGrid[x0 - x, y0 - y] = myVal
        if x0 - y >0 and y0 - x >0: myGrid[x0 - y, y0 - x] = myVal
        if x0 + y < R and y0 - x >0: myGrid[x0 + y, y0 - x] = myVal
        if x0 + x < R and y0 - y >0: myGrid[x0 + x, y0 - y] = myVal
        if (err <= 0):
            y += 1
            err += dy
            dy += 2
        if (err > 0):
            x -= 1
            dx += 2
            err += dx - (radius * 2)
    return ''

def getCircleCoords(myGrid, x0, y0, radius):
    x = radius-1
    y = 0
    dx = 1
    dy = 1
    err = dx - (radius *2 )
    myCoords = []
    while (x >= y):
        myCoords.extend([ [x0 + x, y0 + y], [x0 + y, y0 + x], [x0 - y, y0 + x], [x0 - x, y0 + y], [x0 - x, y0 - y], [x0 - y, y0 - x], [x0 + y, y0 - x], [x0 + x, y0 - y] ])
        if (err <= 0):
            y += 1
            err += dy
            dy += 2
        if (err > 0):
            x -= 1
            dx += 2
            err += dx - (radius * 2)
    return myCoords

tmp = input()
C, R = [int(x) for x in tmp.split()]
tmp = input()
y = 0
grid = np.zeros((C, R), dtype=np.int16)
n =0
allColors = []
while True:
    tmp2 = tmp.replace(' \n','')
    tmp2 = tmp.replace('\n','')
    tmp3 = tmp2.split(' ')
    rowData = [ x[0] +'-'+x[1]+'-'+ x[2] for x in [c.split(',') for c in tmp3]]
    for x, c in enumerate(rowData):
        if not(c in allColors):
            allColors.append(c)
        grid[y,x] = allColors.index(c)
    y += 1
    try:
        tmp = input()
        if not tmp: break
    except EOFError:
        break

modesG = []
for i in range(10): # 10 lines should be enough
    for j in range(4): # 4 sides
        if j == 0: modeGrid = mode(grid[i,:])
        elif j == 1: modeGrid = mode(grid[C-i-1,:])
        elif j == 2: modeGrid = mode(grid[:, i])
        else: modeGrid = mode(grid[:, R-i-1])
        lenMode = modeGrid[1][0]
        valMode = modeGrid[0][0]
        if lenMode/C > 0.75 and not (valMode in modesG):
            if len(modesG)==0: modesG = [[valMode]]
            else: modesG.append([valMode])

board = np.ones((C, R)) * 255
for i in modesG:
    board[np.where(grid == i)] = 0

nCircles = 0
i = 0
while i < C:
    a, b = (0, 0)
    while a < R:
        if board[i, a] == 0:
            a += 1
        else:
            b = a
            while b < R and board[i, b] > 0:
                b += 1
            if b - a >= 10: # found a line of pixels >= 25
                lenAB = b - a
                y0, y1 = (i, i)
                while y0 < C and np.sum(board[y0, a:b]>0) == lenAB: # find a rectangle under the line
                    y0 += 1
                if y0 == y1:
                    board[y0, a:b] = 0
                    break
                x = lenAB // 2 + a
                y = (y0 - y1) // 2 + i

                diamCir = (y0 - y1) // 2 - 1 # estimate diameter
                if x + diamCir//2 +1 > R: diamCir -= 1
                if y + diamCir//2 +1 > C: diamCir -= 1
                if (diamCir >= 15):
                    mCoord = getCircleCoords(board, y, x, diamCir) # get coords of a circle of that diameter

                    drawcircle(board, y, x, diamCir, 0, C,R)
                    floodFill4(board, y, x, 0)
                    nCircles += 1
                else:
                    board[y1:y0, a:b] = 0
            else:
                a = b+1
    i += 1

print(nCircles)
