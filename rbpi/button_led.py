'''
Created on Jun 30, 2023

@author: ctate
'''
from time import sleep
import RPi.GPIO as GPIO
delay=.1
inPin=21
outPin=20
lightActivated=False
GPIO.setmode(GPIO.BCM)
GPIO.setup(inPin,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(outPin,GPIO.OUT)
try:
    while True:
        readVal=GPIO.input(inPin)
        if readVal==0:
            while readVal==0:
                sleep(.1)
                readVal=GPIO.input(inPin)
            lightActivated=not lightActivated
            GPIO.output(outPin,lightActivated)
            print("The LED is %s. " % ("on" if lightActivated else "off"))
        sleep(delay)
except KeyboardInterrupt:
    GPIO.cleanup()
    print("\nTHATTT'SSSS AAAAAAAAAAAAAAAAAALLLLLLLLLLLLLLLLLLLLLLLLLLLL Fonks+")