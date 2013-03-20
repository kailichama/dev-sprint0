# Flower excercise (4.2) from Week 0

# Name:


from TurtleWorld import * 
from math import *		
world = TurtleWorld()			
bob = Turtle()				



# This is where you put code to move bob
#Write an appropriately general set of functions that can draw flowers as in Figure 4.1.

def polyline(t, n, length, angle):
    for i in range(n):
        fd(t, length)
        lt(t, angle)

def arc(t, r, angle):
    arc_length = 2 * pi * r * abs(angle)/360
    n = int(arc_length / 4) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n #float values have decimals 

    lt(t, step_angle/2)
    polyline(t, n, step_length, step_angle)
    rt(t, step_angle/2)

def petal(t, r, angle):
    for i in range(2):
        arc(t, r, angle)
        lt(t, 180-angle)

def flower(t, r, n, angle):
    for i in range(n):
        petal(t, r, angle)
        lt(t, 360.0/n)
flower(bob, 20, 5, 100)


wait_for_user()					

