import numpy as np
from scipy.signal import convolve2d

image = np.array([
    [10, 10, 10],
    [10, 50, 10],
    [10, 10, 10]
])

# Simple edge detection kernel
kernel = np.array([
    [-1, -1, -1],
    [-1,  8, -1],
    [-1, -1, -1]
])

result = convolve2d(image, kernel, mode='same', boundary='symm')
print(result)