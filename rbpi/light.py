'''
Created on Jun 29, 2023

@author: ctate
'''
import RPi.GPIO as GPIO
from time import sleep
num_blinks = int(input("How many times should I blink the LED light? "))
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
num_seconds = 3
sleep_seconds = 1
print("turning off in %s blinks" % num_blinks)
for i in reversed(range(num_blinks)):
    print("%s" % (i + 1))
    print("on")
    GPIO.output(11,1)
    sleep(sleep_seconds)
    print("off")
    GPIO.output(11,0)
    sleep(sleep_seconds)
GPIO.cleanup()
