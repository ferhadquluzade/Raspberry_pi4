import RPi.GPIO as GPIO
from time import sleep 
GPIO.setmode(GPIO.BCM)
GPIO.setup(4,0)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,0)
while 1:
	GPIO.output(4,1)
	sleep(2)
	GPIO.output(17,1)
	sleep(2)                                                                                                                                                                                                                                                                         
	GPIO.output(27,1)
	sleep(2)                                                                                                                                                                                                                                                     
	GPIO.output(4,0)                                                                                                                                                                                                                                                                
	GPIO.output(17,0)                                                                                                                                                                                                                                                                
	GPIO.output(27,0)     
	sleep(2)                                                                                                                                                                                                                                                     
	                                                                                                                                                                                                                                                           
	
