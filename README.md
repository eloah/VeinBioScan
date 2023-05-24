# VeinBioScan
Finger Vein Biometrical Scanner Project. 

Software: Python 3.5, utilizes PySide lib for GUI development, sqlite3 for database, sklearn lib for machine learning, PyCamera lib, skimage for image processing.

Hardware: Rapsberry Pi, PyCamera for night vision with fisheye lens, infrared led 2x8 grid, power supply. Please not that ambient light consists a bit noise for the image quality and data results.

Device of the project is a simple box with all hardware and a cylinder for finger to be placed and scanned. Inside a cylinder is pure dark for better results. Finger is being put in cylinder and photos are taken of a finger in preview video mode. After image processing that collected data is compared with stored data of 5 different people as a result of authentication of a person. 2 options are available: identification and authentication. 1st option is being processed as described before, 2nd option is adding authentication with password. 

Image processing: after image  were taken, it is being processed to binary image, croped, converted to numpy array, and compared to the existing data with KNN classifier.  

mGui.py if for all Desktop App widgets. It consists of all windows which are needed for app.
DBManager.py is for controlling a Database inserts and removes.
imageProcessing.py is for all image processes for collecting data. it is possible to addd any data fo any person.
KNNClassifier. Here where is all amgic begins, classifying the new data from existing data for authentication. Splitting for training and validating data KNN classifiers compares the result after training upon existing person data and predict the outcome of algorithm.
