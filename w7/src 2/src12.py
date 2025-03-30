from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
sleep(5)
camera.capture('/home/pi/Documents/is4151-is5451/lecture07/image.jpg')
camera.stop_preview()
