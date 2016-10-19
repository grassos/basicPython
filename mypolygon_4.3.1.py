import Turtleworld

world = TurtleWorld()
bob = Turtle()
print (bob)

def square(t,n):

    for i in range(n):
        fd(t, 100)
        lt(t)

square (bob, 4)
