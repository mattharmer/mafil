#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Variables
delay = 0.0208
steps = 1

# Enable pins
enable_a = 1 #Purple
enable_b = 12 #Blue
coil_A_1_pin = 6 #White
coil_A_2_pin = 5 #Red
coil_B_1_pin = 26 #Orange
coil_B_2_pin = 13 #Yellow

# Set pin states

GPIO.setup(enable_a, GPIO.OUT)
GPIO.setup(enable_b, GPIO.OUT)
GPIO.setup(coil_A_1_pin, GPIO.OUT)
GPIO.setup(coil_A_2_pin, GPIO.OUT)
GPIO.setup(coil_B_1_pin, GPIO.OUT)
GPIO.setup(coil_B_2_pin, GPIO.OUT)


# Set ENA and ENB to high to enable stepper

GPIO.output(enable_a, True)
GPIO.output(enable_b, True)

# Function for step sequence

def setStep(w1, w2, w3, w4):
  GPIO.output(coil_A_1_pin, w1)
  GPIO.output(coil_A_2_pin, w2)
  GPIO.output(coil_B_1_pin, w3)
  GPIO.output(coil_B_2_pin, w4)

for i in range(0, steps):
    time.sleep(1)

    #Position 1 In front
    setStep(0,1,1,0)
    time.sleep(delay)

    #Position2 Normal
    setStep(0,1,0,1)
    time.sleep(delay)


    #setStep(1,0,0,1)
    #time.sleep(delay)
    #setStep(1,0,1,0)
    #time.sleep(delay)
    #setStep(1,0,1,0)
    #time.sleep(delay)
    #setStep(1,0,0,1)
    #time.sleep(delay)
    #setStep(0,1,0,1)
    #time.sleep(delay)
    #setStep(0,1,1,0)
    #time.sleep(delay)

#Disable Stepper
GPIO.output(enable_a, False)
GPIO.output(enable_b, False)