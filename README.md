# VeinBioScan
Finger Vein Biometrical Scanner Project. 

Software: Python 3.7, utilizes PySide lib for GUI development, sqlite3 for database, sklearn lib for machine learning, PyCamera lib, skimage for image processing.

Hardware: Rapsberry Pi, PyCamera for night vision with fisheye lens, infrared led 2x8 grid, power supply.

Device of the project is a simple box with all hardware and a cylinder for finger to be placed and scanned. Inside a cylinder is pure dark for better results. Finger is being put in cylinder and photos are taken of a finger in preview video mode. After image processing that collected data is compared with stored data of 5 different people as a result of authentication of a person. 2 options are available: identification and authentication. 1st option is being processed as described before, 2nd option is adding authentication with password. 

Image processing: after image  were taken, it is being processed to binary image, croped, converted to numpy array, and compared to the existing data with KNN classifier.  
