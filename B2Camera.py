from picamera import PiCamera
from time import sleep

camera=PiCamera()

camera.rotation=180

camera.resolution=(1280,720)
camera.start_preview()
for i in range(5):
    sleep(5)
    camera.capture('/home/pi/Desktop/Image%s.jpg'%i)

camera.start_recording('/home/pi/Desktop/b2.h264')
sleep(10)
camera.stop_recording()

camera.stop_preview()
