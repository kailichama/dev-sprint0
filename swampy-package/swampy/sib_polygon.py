# Polygon excercise from Week 0

# Name: Kelly Chiang


from TurtleWorld import * 		
world = TurtleWorld()			
bob = Turtle()				



# This is where you put code to move bob

#square function

def square(t):
    for i in range(4):
        fd(t, 100)
        lt(t)
print square(bob) #keeps it form looping?

#small square
def square2(t, length):
    for i in range(4):
        fd(t, length)
        lt(t)
square2(bob, 25) 

def polygon(t, n, length):
    for i in range(n):
    	angle = 360/n
        fd(t, length)
        rt(t, angle)
        lt(t)
polygon(bob, 8, 70)


# circle function

def circle(t, r):
    length = 1
    circumference = n
circle(bob, 2)

wait_for_user()					
