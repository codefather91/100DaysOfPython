
from turtle import Turtle, Screen
import random
import numpy as np


screen = Screen()
sides = 4
angle = 360/sides
screen.colormode(cmode=255)
t = Turtle()
color_list = []
t.speed(speed=10)

while 360/sides >= 1:
    for _ in range(sides):
        t.forward(50)
        t.right(360/sides)
        color_list = []
        color_list.append(random.randint(0,255))
        color_list.append(random.randint(0,255))
        color_list.append(random.randint(0,255))
        t.color(tuple(color_list))
    t.right(1)
    sides+=1
