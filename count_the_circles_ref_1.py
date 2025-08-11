import numpy as np
from scipy import ndimage
from sklearn.feature_extraction import image

# Get the sizing
a = input()

# ONLY WORKS TO READ AN IMAGE IN PYTHON 3
tmp_img = []
line = 'a'
while (len(line)>0):
    try:
        row = []
        a = input()
        pixels = a.split(' ')
        for pixel in pixels:
            row.append(list(map(int,pixel.split(','))))
        tmp_img.append(row)
    except:
        line = []
img = np.array(tmp_img)

clip_amount = int(18)
half_clip = int(clip_amount/2)
    
img1d = np.zeros( (img.shape[0]-clip_amount,img.shape[1]-clip_amount) )
for r in range(half_clip,img.shape[0]-half_clip):
    for c in range(half_clip,img.shape[1]-half_clip):
        img1d[r-half_clip][c-half_clip] = 1*np.abs(img[r][c][0]-img[half_clip][half_clip][0]) \
                                        + 1*np.abs(img[r][c][1]-img[half_clip][half_clip][1]) \
                                        + 1*np.abs(img[r][c][2]-img[half_clip][half_clip][2])
        if (img1d[r-half_clip][c-half_clip]==246):
            img1d[r-half_clip][c-half_clip] = 0

# TRY TO GENERATE AN ANSWER
maxv = np.max(img1d)
minv = np.min(img1d)
meanv = np.mean(img1d)
threshold = minv + (0.10*(meanv-minv))
    
temp_threshold_image = np.array(img1d>threshold)
es = [[0,1,0],[1,1,1],[0,1,0]]
threshold_image = ndimage.binary_erosion(temp_threshold_image,structure=es,iterations=20)
mask = threshold_image.astype(bool)

s = [[0, 1, 0], [1,1,1], [0,1,0]]
from scipy.ndimage import label
labeled_array1, num_features1 = label(temp_threshold_image,s)
labeled_array2, num_features2 = label(mask,s)
print( np.max([num_features1,num_features2]) )