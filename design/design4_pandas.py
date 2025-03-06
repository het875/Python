# Draw a Panda using Turtle Graphics
# Import turtle package
import turtle

# Creating a turtle object(pen)
pen = turtle.Turtle()

# Defining method to draw a colored circle
# with a dynamic radius
def ring(col, rad):

	# Set the fill
	pen.fillcolor(col)

	# Start filling the color
	pen.begin_fill()

	# Draw a circle
	pen.circle(rad)

	# Ending the filling of the color
	pen.end_fill()

##########################Main Section#############################

# pen.up			 --> move turtle to air
# pen.down		 --> move turtle to ground
# pen.setpos		 --> move turtle to given position
# ring(color, radius) --> draw a ring of specified color and radius
###################################################################

##### Draw ears #####
# Draw first ear
pen.up()
pen.setpos(-225, 160)
pen.down
ring('black', 80)

# Draw second ear
pen.up()
pen.setpos(225, 160)
pen.down()
ring('black', 80)

##### Draw face #####
pen.up()
pen.setpos(0, -160)
pen.down()
ring('white', 235)

# ##### Draw eyes black #####

# Draw first eye
pen.up()
pen.setpos(-115, 100)
pen.down
ring('black', 40)

# Draw second eye
pen.up()
pen.setpos(115, 100)
pen.down()
ring('black', 40)

##### Draw eyes white #####

# Draw first eye
pen.up()
pen.setpos(-115, 105)
pen.down()
ring('white', 22)

# Draw second eye
pen.up()
pen.setpos(115, 105)
pen.down()
ring('white', 22)

##### Draw nose #####
pen.up()
pen.setpos(0, -75)
pen.down
ring('black', 50)

##### Draw mouth #####
pen.up()
pen.setpos(0, -68)
pen.down()
pen.right(90)
pen.circle(42, 180)
pen.up()
pen.setpos(0, -68)
pen.down()
pen.left(360)
pen.circle(42, -180)
pen.hideturtle()


turtle.done()