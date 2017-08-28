from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
camera.resolution = (2592, 1944)

for i in range(5):
    sleep(60)
    camera.capture('/home/pi/Desktop/image%s.jpg' % i)
camera.stop_preview()
