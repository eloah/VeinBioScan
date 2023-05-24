import time
from picamera import PiCamera


camera = PiCamera()
camera.resolution = (1920, 1080)
camera.saturation = -100
camera.contrast = 30
capture = True
time.sleep(0.1)
camera.start_preview(fullscreen=False, window = (500, 300, 480, 360))
time.sleep(10)
for i in range(0, 10):   
    time.sleep(0.5)
    camera.capture('/home/pi/Desktop/New/FVR/Temp/temp'+str(i)+'.png')

#camera.capture('/home/pi/Desktop/New/Finger-Vein Recognizer/Temp/temp.png')    
camera.stop_preview()
camera.close()
