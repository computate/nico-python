'''
Created on Jun 30, 2023

@author: ctate
'''
from time import sleep
import RPi.GPIO as GPIO
delay=.1
inPin=21
outPin=20
GPIO.setmode(GPIO.BCM)
GPIO.setup(inPin,GPIO.IN)
GPIO.setup(outPin,GPIO.OUT)
try:
    while True:
        readVal=GPIO.input(inPin)
        if readVal==1:
            GPIO.output(outPin,0)
            print("You are not pressing the button. The LED is off. ")
        elif readVal==0:
            GPIO.output(outPin,1)
            print("You are pressing the button. The LED is on. ")
        sleep(delay)
except KeyboardInterrupt:
    GPIO.cleanup()
    print("\nTHATTT'SSSS AAAAAAAAAAAAAAAAAALLLLLLLLLLLLLLLLLLLLLLLLLLLL Fonks+")