# import turtle
import turtle

# defining colors
colors = ['red', 'yellow', 'green', 'purple', 'blue', 'orange', 'pink','cyan']

# setup turtle pen
t= turtle.Pen()

# changes the speed of the turtle
t.speed(100)

# changes the background color
turtle.bgcolor("black")

# make spiral_web
for x in range(325):
	t.pencolor(colors[x%8]) # setting color
	t.width(x/100 + 1) # setting width
	t.forward(x) # moving forward
	t.left(44) # moving left
	

turtle.done()
t.speed(100)

turtle.bgcolor("black") # changes the background color

 # make spiral_web
for x in range(325):
	t.pencolor(colors[x%1]) # setting color
	t.width(x/100 + 1) # setting width
	t.forward(x) # moving forward
	t.left(44) # moving left
	
	

turtle.done()

# print("hello dosto welcome to Mr.unary Code")