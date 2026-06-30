#Jacob Needham
#06//2026
#P4LAB1
#Turtle graphic program that draws a triangle and a square
#
#


#add the turtle code library
import turtle

#create a window for the graphical display
win = turtle.Screen()
t = turtle.Turtle()

# Set the turtle options
t.pensize(7)
t.pencolor("violet")
t.shape("turtle")

#dirctions for turtle writing

#draw square
for side in range(4):
    t.forward(100)
    t.right(90)

#while loop for the triange
side = 3 

while side > 0:
    #print(side)
    t.pencolor("red")

    t.forward(100)
    t.left(120)

    side = side - 1



#Wait for user to close the window
win.mainloop()




