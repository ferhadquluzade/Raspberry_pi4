import RPi.GPIO as gp
import signal
import subprocess
from time import sleep
def shutdown(parm):
	subprocess.Popen(['shutdown','now'])#shutdowns rpi
gp.setmode(gp.BOARD)
gp.setup(7,0)
gp.output(7,1)#while rpi is on the led is on
gp.setup(11,gp.IN,pull_up_down=gp.PUD_UP)#setting up button as an input
gp.add_event_detect(11,gp.FALLING,callback=shutdown)#when the button is pressed it activates shutdown function
signal.pause()#keeps alive the script
