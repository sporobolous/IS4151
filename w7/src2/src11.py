from picamera2 import Picamera2
from time import sleep

camera_list = Picamera2.global_camera_info()
print(camera_list)
camera = Picamera2()
camera.start_preview()
sleep(10)
camera.stop_preview()
