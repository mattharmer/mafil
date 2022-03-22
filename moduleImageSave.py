# What sort of Camera? I should document the camera here

#!/usr/bin/env python

from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.start_preview()
sleep(5)
# This should save as name of Object Detected, with an increment value so no save over files.
camera.capture('/home/pi/mafil_ws/assets/picture.jpg')
camera.stop_preview()