import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.OUT)
while True:
	GPIO.output(4,1)
	time.sleep(5)
	GPIO.output(4,0)
	time.sleep(2)
