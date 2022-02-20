'''
Created on Feb 19, 2022

@author: ctate
'''
import random
from turtle import *
def  vshape(size):
    right(25)
    forward(size)
    backward(size)
    left(50)
    forward(size)
    backward(size)
    right(25)
def snowflakeArm(size):
    for x in range(0,4):
        forward(size)
        vshape(size)
    backward(size*4)
def snowflake(size):
    for x in range(0,6):
        color(random.choice(colors))
        snowflakeArm(size)
        right(60)
if __name__ == '__main__':
    shape("turtle")
    speed(10)
    colors = ["blue", "purple", "cyan", "yellow", "green", "orange", "red", "pink"]
    for i in range(0,999999999999999999999999):
        size = random.randint(5,30)
        x = random.randint(-400,400)
        y = random.randint(-400,400)
        penup()
        goto(x,y)
        pendown()
        snowflake(size)