import turtle

animation = turtle.Turtle()
animation.speed(0)
animation.hideturtle()
animation.getscreen().bgcolor("black")
animation.color("red")

for i in range(325):
	animation.circle(i)
	animation._rotate(7)
