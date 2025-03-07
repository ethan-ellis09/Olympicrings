import turtle

screen = turtle.Screen()
screen.screensize(canvwidth=500,canvheight=500)
screen.bgcolor("Tan")

t= turtle.Turtle()

t.pencolor("blue")
t.penup()
t.goto(-80,15)
t.pendown()
t.circle(35)

t.pencolor("Black")
t.penup()
t.goto(0,15)
t.pendown()
t.circle(35)

t.pencolor("red")
t.penup()
t.goto(80,15)
t.pendown()
t.circle(35)

t.pencolor("yellow")
t.penup()
t.goto(-40,-15)
t.pendown()
t.circle(35)

t.pencolor("green")
t.penup()
t.goto(40,-15)
t.pendown()
t.circle(35)


t.penup()
t.goto(0,100)
t.pencolor("purple")
t.pendown()
t.write("Winter Olympics",font=("Arial",30,"normal"),align="center")

t.penup()
t.goto(0,-100)
t.pencolor("purple")
t.pendown()
t.write("2026",font=("Arial",30,"normal"),align="center")

t.hideturtle()
turtle.done()