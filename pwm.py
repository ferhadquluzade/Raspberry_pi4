from time import sleep 
import RPi.GPIO as gp
gp.setmode(gp.BCM)
gp.setup(21,0)
led=gp.PWM(21,110)#110 is f 
led.start(100)#when this line starts it will do at 100 
#and after for loop that will be again 100.
#that is sort of default value
for dc in range(0,101,5):
	led.ChangeDutyCycle(dc)
	sleep(2)
	print(dc)
	if(dc==100):
		break
