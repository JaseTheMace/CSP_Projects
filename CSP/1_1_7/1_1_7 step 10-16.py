#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

# create an empty list of turtles
my_turtles = []
trtl.speed(50)
# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic", "arrow", "turtle", "circle", "square", "triangle", "classic", "arrow", "turtle", "circle", "square", "triangle", "classic", "arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold", "red", "blue", "green", "orange", "purple", "gold", "red", "blue", "green", "orange", "purple", "gold", "red", "blue", "green", "orange", "purple", "gold"]

for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  t.penup()
  new_color = turtle_colors.pop()
  t.fillcolor(new_color)
  t.pencolor(new_color)
  my_turtles.append(t)

direction = 90

for_length = 50

length = 50

#  starting spot
startx = 0
starty = 0

#  length and angle
for t in my_turtles:
  t.setheading(direction)
  t.goto(startx, starty)
  t.pendown()
  t.right(45) 
  t.forward(length)
  direction = t.heading()
  for_length  += 3

  length = length + 3  
#	 start position
  startx = t.xcor()
  starty = t.ycor()

wn = trtl.Screen()
wn.mainloop()