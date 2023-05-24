from skimage.feature import hog
from skimage.transform import resize, rescale
from skimage import io, exposure, color 
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.neighbors import DistanceMetric

import numpy as np
from PIL import Image as im

def imageProc():
    f = False
    for i in range(0,10):
        image = im.open('/home/pi/Desktop/New/FVR/Temp/temp'+str(i)+'.png')
        left = 400
        top = 340
        width = left + 1250
        height = top + 380
        image = image.crop((left, top, width, height))
    
        image = np.array(image)
        imgResized = resize(image, (152, 500))
        grayScale = color.rgb2gray(imgResized)
        # io.imsave('/home/pi/Desktop/New/Finger-Vein Recognizer/Temp/cropedd.png', grayScale)
        # imgCroped = crop(grayScale, (140, 140))
        # io.imsave('D:/PythonProgs/DIP/img.png',imgCroped)
        # if not open('Data/AcquiredData.txt'):
        # p2, p98 = np.percentile(imgCroped, (2, 98))
        # img_rescale = exposure.equalize_adapthist(imgCroped, clip_limit=0.015)
        
        if f == False:
        
            fd, hog_image = hog(grayScale, orientations=8, pixels_per_cell=(8, 8), cells_per_block=(1, 1), visualise=True)
            f = True     
            
        else:
            fdd, hog_image = hog(grayScale, orientations=8, pixels_per_cell=(8, 8), cells_per_block=(1, 1), visualise=True)
            fd = np.vstack((fd, fdd))
    
    #print(fd.shape,fd)
    fd = fd.mean(axis = 0) 
    fd = fd.reshape(1,-1)
    #d = euclidean_distances(fd, fd)
    #dist = DistanceMetric.get_metric('euclidean')
    #print(np.mean(dist.pairwise(fd)))
    print(fd.shape,fd)
    #print(d)
    return fd #, d

#imageProc()


def imageProcc():
    image = im.open('/home/pi/Desktop/New/FVR/Temp/temp.png')
    left = 400
    top = 340
    width = left + 1250
    height = top + 380
    image = image.crop((left, top, width, height))
    
    image = np.array(image)
    imgResized = resize(image, (152, 500))
    grayScale = color.rgb2gray(imgResized)
    # io.imsave('/home/pi/Desktop/New/Finger-Vein Recognizer/Temp/cropedd.png', grayScale)
    # imgCroped = crop(grayScale, (140, 140))
    # io.imsave('D:/PythonProgs/DIP/img.png',imgCroped)
    # if not open('Data/AcquiredData.txt'):
    # p2, p98 = np.percentile(imgCroped, (2, 98))
    # img_rescale = exposure.equalize_adapthist(imgCroped, clip_limit=0.015)
    fd, hog_image = hog(grayScale, orientations=8, pixels_per_cell=(8, 8), cells_per_block=(1, 1), visualise=True)
    fd = fd.reshape(1,-1)
    #d = euclidean_distances(fd, fd)
    print(fd.shape,fd) 
    return fd
#imageProcc()

