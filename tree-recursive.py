# Written by Ralph Louis Gopez
import turtle

# parameters here easily tweak it and change it for experimental purposes
depth = 10
starting_length = 150
angle = 25
length_rate = 0.6
has_animation = True

# this is the recursive branch function
# which basically draws the tree's branches recursively
# mind boggling to think about but yeah it works
def branch(n, angle, length):
    if n == 0:
        return

    # so yeah we start somewhere that totally depends on how you setup the turtle first

    # left branch first, simply rotate to angle then forward
    turtle.left(angle)
    turtle.forward(length)
    # yeah we call itself here when the 
    # turtle is basically at one of the branch ends (the left one) 
    # and it starts the whole same recursive function but n-1 to eventually reach base case
    branch(n-1, angle, length * length_rate)

    # Moves the turtle back to its original current position for 
    # us to be able to draw the second branch
    turtle.backward(length)
    turtle.right(angle)

    # right branch, second, same routine but right instead of left or we can use left but -angle
    turtle.right(angle)
    turtle.forward(length)
    # this one calls the function again for this right branch
    branch(n-1, angle, length * length_rate)

    # remember to always put the turtle back on its current original place
    turtle.backward(length)
    turtle.left(angle)

if __name__ == "__main__":
    turtle.setup(width=600, height=600, startx=None)
   
    turtle.tracer(has_animation)
    turtle.speed("fastest")
    turtle.color("black")
    
    turtle.left(90)

    # for some reason setting starty on setup doesn't work hence this
    turtle.up()
    turtle.backward(300)
    turtle.down()

    turtle.forward(starting_length)
    branch(depth, angle, starting_length)
    turtle.done()
