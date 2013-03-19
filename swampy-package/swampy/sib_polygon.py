# Polygon excercise from Week 0

# Name: Kelly Chiang


from TurtleWorld import * 
from math import pi		
world = TurtleWorld()			
bob = Turtle()				



# This is where you put code to move bob

#square function

def square(t):
    for i in range(4):
        fd(t, 100)
        lt(t)
#print square(bob) #keeps it form looping?

#small square
def square2(t, length):
    for i in range(4):
        fd(t, length)
        lt(t)
#square2(bob, 25) 

def polygon(t, n, length):
    for i in range(n):
    	angle = 360/n
        fd(t, length)
        rt(t, angle)
#polygon(bob, 8, 70)


# circle function
#def circle(t, r):
    #circumference = 2 * pi * r
    #n = 50
    #length = circumference / n
    #polygon(t, n, length)
#circle(bob, 20)

#refactored code arc()
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

arc(bob, 20, 180) #can draw an arc of any angle! :D   


#def circle(t, r):
 #   arc (t, r, 360)
#circle(bob, 20)

wait_for_user()					
