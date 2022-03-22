# Imports
import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Define GPIO Pin Numbers
Ena = 13
In1 = 17
In2 = 27
Enb = 12
In3 = 22
In4 = 23
Lir = 16
Rir = 4

# Declare User Variables
encoderAmount = 189 * 3# * ticks by two to count all ticks, change later when using sway.
motorDirection = 1
motorSpeedLeft = 40
motorSpeedRight = 40

# Declare GPIO Pin Usage
GPIO.setup(Ena,GPIO.OUT)
GPIO.setup(In1,GPIO.OUT)
GPIO.setup(In2,GPIO.OUT)
GPIO.setup(Enb,GPIO.OUT)
GPIO.setup(In3,GPIO.OUT)
GPIO.setup(In4,GPIO.OUT)
GPIO.setup(Lir,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(Rir,GPIO.IN, pull_up_down=GPIO.PUD_UP)
# Declare Ena & Enb Pins as PWM and set Frequency
pwmEna = GPIO.PWM(Ena, 100)
pwmEnb = GPIO.PWM(Enb, 100)

# Start PWM
pwmEna.start(0)
pwmEnb.start(0)

# Change Duty Cycle
pwmEna.ChangeDutyCycle(motorSpeedLeft);
pwmEnb.ChangeDutyCycle(motorSpeedRight);

# Send Move Command to Motor Controller

#if motorDirection = 1
GPIO.output(In1,GPIO.HIGH)
GPIO.output(In2,GPIO.LOW)
GPIO.output(In3,GPIO.HIGH)
GPIO.output(In4,GPIO.LOW)

# Tick Count from event detects.
irLCount = 0
irRCount = 0

	# Event Detect Callback Counts.
def irLcallback(channel):
	global irLCount
	global irRCount

	#Set initial Motor Power
	global motorSpeedLeft
	global motorSpeedRight
	
	irLCount += 1
	print("Tick irL", irLCount)

	# Check if Tick Count Reached
	if irLCount >= encoderAmount:
		sleep(0.01)
		pwmEna.ChangeDutyCycle(0);
		pwmEnb.ChangeDutyCycle(0);
		print("Left IR reached Final Ticks", irLCount)
		print("Right IR reached Final Ticks", irRCount)
		print("CTRL-C to Kill")
		GPIO.cleanup()
	
	print("motorSpeedLeft", motorSpeedLeft)

	if irLCount > irRCount +4:
		motorSpeedLeft -= 0.2
		motorSpeedRight += 0.2

	if motorSpeedLeft > 99: motorSpeedLeft = 100
	if motorSpeedRight > 99: motorSpeedRight = 100
	if motorSpeedLeft < 1: motorSpeedLeft = 1
	if motorSpeedRight < 1: motorSpeedRight = 1

	pwmEna.ChangeDutyCycle(motorSpeedLeft);
	pwmEnb.ChangeDutyCycle(motorSpeedRight);

def irRcallback(channel):
	global irLCount
	global irRCount
	global motorSpeedLeft
	global motorSpeedRight
	irRCount += 1
	print("Tick irR", irRCount)

	# Check if Tick Count Reached
	if irRCount >= encoderAmount:
		sleep(0.01)
		pwmEna.ChangeDutyCycle(0);
		pwmEnb.ChangeDutyCycle(0);
		print("Right IR reached Final Ticks of", irRCount)
		print("CTRL-C to Kill")
		GPIO.cleanup()

	#Check if Motors Left is slower and Increase
	print("motorSpeedRight", motorSpeedRight)

	if irRCount > irLCount + 4:
		motorSpeedLeft += 0.2
		motorSpeedRight -= 0.2

	if motorSpeedLeft > 99: motorSpeedLeft = 100
	if motorSpeedRight > 99: motorSpeedRight = 100
	if motorSpeedLeft < 1: motorSpeedLeft = 1
	if motorSpeedRight < 1: motorSpeedRight = 1

	pwmEna.ChangeDutyCycle(motorSpeedLeft);
	pwmEnb.ChangeDutyCycle(motorSpeedRight);

# Listen for Event Detect
GPIO.add_event_detect(Lir, GPIO.BOTH, callback=irLcallback)
GPIO.add_event_detect(Rir, GPIO.BOTH, callback=irRcallback) # Only counting one detector ATM. Check again when introduce sway detect.

# Sleep until Key Press.
try:
	sleep(1000)
except KeyboardInterrupt:
	pwmEna.stop()
	pwmEnb.stop()
	GPIO.cleanup()