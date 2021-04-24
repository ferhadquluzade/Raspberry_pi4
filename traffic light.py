from gpiozero import LED
from time import sleep 
green=LED(4)
yellow=LED(17)
red=LED(27)
while 1:
	green.on()
	sleep(2)                                                                                                                                                                                                                                    
	green.off()
	yellow.on()
	sleep(2)     	
	yellow.off()
	red.on()
	sleep(2)                       
	red.off()
	sleep(2)                                                                                                                                                                                                                                                                                                                                                                                                                                                  


