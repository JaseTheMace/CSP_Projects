#   a116_ladybug.py
import turtle as trtl
ladybug = trtl.Turtle()
ladybug.pensize(5)

num_legs = 6
length_legs = 55
angle = 210 / num_legs
counter = 0

while(counter < num_legs):
  if counter < 3:
    ladybug.penup()
    ladybug.goto(0,-30)
    ladybug.pendown()
    ladybug.setheading(angle * counter - 40)
    ladybug.forward(length_legs)
    counter = counter + 1
  else:
    ladybug.penup()
    ladybug.goto(0,-30)
    ladybug.pendown()
    ladybug.setheading(angle * counter + 40)
    ladybug.forward(length_legs)
    counter = counter + 1

# create ladybug head
ladybug = trtl.Turtle()
ladybug.pensize(40)
ladybug.circle(5)

# and body
ladybug.penup()
ladybug.goto(0, -55) 
ladybug.color("red")
ladybug.pendown()
ladybug.pensize(40)
ladybug.circle(20)
ladybug.setheading(270)
ladybug.color("black")
ladybug.penup()
ladybug.goto(0, 5)
ladybug.pensize(2)
ladybug.pendown()
ladybug.forward(75)

# config dots
num_dots = 0
xpos = -20
ypos = -55
ladybug.pensize(10)

# draw two sets of dots
while (num_dots < 2 ):
  ladybug.penup()
  ladybug.goto(xpos, ypos)
  ladybug.pendown()
  ladybug.circle(3)
  ladybug.penup()
  ladybug.goto(xpos + 30, ypos + 20)
  ladybug.pendown()
  ladybug.circle(2)

  # position next dots
  ypos = ypos + 25
  xpos = xpos + 5
  num_dots = num_dots + 1

ladybug.hideturtle()



wn = trtl.Screen()
wn.mainloop()

