from DBManager import *
from imageProcessing import imageProc, imageProcc
from sklearn import preprocessing, neighbors, metrics 
from sklearn.metrics.pairwise import euclidean_distances, paired_distances
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor, DistanceMetric
import numpy as np


from skimage.feature import hog
from skimage.transform import resize, rescale
from skimage import io, exposure, color 
from PIL import Image as im

name = 'Χιονίδης Ρωμάν'
class knnClassifier():
    def __init__(self): 
        super(knnClassifier, self).__init__()

    def trainKnn(self):
        self.X = dbReadData()
        self.y = dbReadLabels()
        self.knn = KNeighborsClassifier(n_neighbors=1)
        self.knn.fit(self.X,self.y)
        return 

    def classify(self):
        sample = imageProcc()
        prediction = self.knn.predict(sample)
        #print(prediction)
        #accuracy =  self.knn.score(self.y, prediction) 
        #print(accuracy)
        prediction = tuple(prediction)
        prediction = prediction[0]
        
        X1 = dbReadData1(prediction)
        print(X1, X1.shape)
        d = euclidean_distances(sample, X1)
        d = tuple(d)
        d = d[0]
        print(d, d.shape)
        
        return prediction, d


def knnNoSplitData():
    
    X = dbReadData()
    #print(X,X.shape)
    y = dbReadLabels()
    sample = imageProcc()
    #dist = 
    knn = KNeighborsClassifier(n_neighbors=1)
    knn.fit(X,y)
    prediction = knn.predict(sample)
    print(prediction)
    #accuracy =  knn.score(X, y)
    #print(dis)
    d = euclidean_distances(sample, X)
    #d = d.reshape(1,-1)
    print(d,d.shape)
    #print(d,np.mean(d))
    #print(d,sum)
    #dist = DistanceMetric.get_metric('euclidean')
    #print(np.mean(dist.pairwise(X)))
    #print(np.mean)
      
    return  d #prediction,


def knnNoSplitData1():
    
    X = imageProc()#dbReadData1(name)
    #print(X,X.shape)
    y = dbReadLabels()
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
        fd, hog_image = hog(grayScale, orientations=8, pixels_per_cell=(8, 8), cells_per_block=(1, 1), visualise=True)
        d = euclidean_distances(fd, X)
        print(d,d.shape)
    #sample = imageProcc()
    #dist = 
    #knn = KNeighborsClassifier(n_neighbors=1)
    #knn.fit(X,y)
    #prediction = knn.predict(sample)
    #print(prediction)
    #accuracy =  knn.score(X, y)
    #print(dis) 
    #d = euclidean_distances(sample, X)
    #d = d.reshape(1,-1)
    #print(d,d.shape)
    #print(d,np.mean(d))
    #print(d,sum)
    #dist = DistanceMetric.get_metric('euclidean')
    #print(np.mean(dist.pairwise(X)))
    #print(np.mean)
      
    return  d #prediction,
    
def passVerify(name):
    X = dbReadData1(name)
    sample = imageProcc()
    d = euclidean_distances(sample, X)
    return d
"""class knnClassifier1():
    def __init__(self):
        super(knnClassifier1, self).__init__()

    def trainKnn(self):
        self.X = dbReadData()
        self.y = dbReadLabels()
        #self.X_train, self.X_test, self.y_train, self.y_test = cross_validation.train_test_split(self.X, self.y, test_size=0.2)
        self.knn = KNeighborsClassifier(n_neighbors=1)
        self.knn.fit(self.X_train, self.y_train)
        return

    def classify(self):
        sample = imageProc()
        prediction = self.knn.predict(sample)
        print(prediction)
        accuracy =  self.knn.score(self.X_test, self.y_test) 
        print(accuracy)
        return prediction

def knnSplitData():
    X = dbReadData()
    y = dbReadLabels()
    #X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.2)
    sample = imageProc()


    knn = KNeighborsClassifier(n_neighbors=3)
    knn.fit(X_train, y_train)
    prediction = knn.predict(sample)
    print(prediction)

    accuracy =  knn.score(X_test, y_test)
    print(accuracy)

    return prediction, accuracy
    

def knnMultipleKTestSplitData():
    k = range(1, 26)
    scores = []

    X = dbReadData()
    y = dbReadLabels()
    #X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.2)

    for i in k:
        knn = KNeighborsClassifier(n_neighbors=i)
        knn.fit(X_train, y_train)
        prediction = knn.predict(X_test)
        scores.append(knn.score(X_test, y_test))
        plt.plot(k, scores)
        plt.xlabel('Value of K for Knn')
        plt.ylabel('Testing Accuracy')
    return

def knnMultipleKTestNoSplitData():
    k = range(1, 26)
    scores = []

    X = dbReadData()
    y = dbReadLabels()
    for i in k:
        knn = KNeighborsClassifier(n_neighbors=i)
        knn.fit(X, y)
        prediction = knn.predict(X)
        scores.append(knn.score(X, y))
        plt.plot(k, scores)
        plt.xlabel('Value of K for Knn')
        plt.ylabel('Testing Accuracy')
    return"""



#knnNoSplitData1()
#knnNoSplitData()
#knnSplitData()
# knnMultipleKTestSplitData()
# knnMultipleKTestNoSplitData()


#knnnn = knnClassifier()
#knnnn.trainKnn()
#knnnn.classify()
