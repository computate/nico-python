'''
Created on Feb 19, 2022

@author: ctate

# Prerequisites

```bash
pkcon install -y python3-tkinter
```
'''
def myFourPixels():
    forward(25)
    left(90)
    forward(25)
    left(90)
    forward(25)
    left(90)
    forward(25)
    right(90)
    forward(25)
    right(90)
    forward(25)
    right(90)
    forward(50)
    left(90)
    forward(25)
    left(90)
    forward(25)
    left(90)
    forward(25)
    right(90)
    forward(25)
    right(90)
    forward(25)
    right(90)
    forward(25)
def mySquare(size):
    forward (size)
    right(90)
    forward (size)
    right(90)
    forward (size)
    right(90)
    forward(size)

from turtle import *
if __name__ == '__main__':
    hideturtle()
    color("white")
    shape("square")
    speed(1)
    pensize(4)
    Screen().bgcolor("red")
    mySquare(400)
    done()