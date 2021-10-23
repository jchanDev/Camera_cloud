from picamera import PiCamera
from time import sleep
import time
camera = PiCamera()


#camera.shutter_speed = 17500
#camera.brightness = 60
#camera.exposure_mode = 'night'
#camera.rotation = 0
camera.brightness = 55
camera.shutter_speed = 6000000
camera.iso = 800

time.sleep(6.0)

camera.exposure_mode = 'off'
camera.start_preview(fullscreen=False, window = (30,30,640,480))

