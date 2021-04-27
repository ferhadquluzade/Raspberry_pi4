from time import sleep 
import RPi.GPIO as gp
def turnOnLight(lights):
    ind=0
    while (ind<3):
        lights[ind].start(100)
        sleep(3.5)
        for x in range(5):
            lights[ind].ChangeDutyCycle(0)
            sleep(0.5)
            lights[ind].ChangeDutyCycle(100)
            sleep(0.5)
        lights[ind].stop()
        if(ind==2):
            ind=0
            continue
        ind+=1
gp.setmode(gp.BCM)
greenPin=4
yellowPin=17
redPin=27
gp.setup(greenPin,0)
gp.setup(yellowPin,0)
gp.setup(redPin,0)
green=gp.PWM(greenPin,50)
yellow=gp.PWM(yellowPin,50)
red=gp.PWM(redPin,50)
lights=[green,yellow,red]
turnOnLight(lights)
