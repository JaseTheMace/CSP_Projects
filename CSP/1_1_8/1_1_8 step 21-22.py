#   a118_turtles_in_traffic.py
#   Move turtles horizontally and vertically across screen.
#   Stopping turtles when they collide.
import turtle as trtl

# create two empty lists of turtles, adding to them later
horiz_turtles = []
vert_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
horiz_colors = ["red", "blue", "green", "orange", "purple", "gold"]
new_horiz_colors = ["red", "blue", "green", "orange", "purple", "gold"]
vert_colors = ["darkred", "darkblue", "lime", "salmon", "indigo", "brown"]
new_vert_colors = ["darkred", "darkblue", "lime", "salmon", "indigo", "brown"]

tloc = 50
for s in turtle_shapes:

  ht = trtl.Turtle(shape=s)
  horiz_turtles.append(ht)
  ht.penup()
  ht.speed(0)
  new_color = horiz_colors.pop()
  ht.fillcolor(new_color)
  ht.goto(-350, tloc)
  ht.setheading(0)

  vt = trtl.Turtle(shape=s)
  vert_turtles.append(vt)
  vt.penup()
  vt.speed(0)
  new_color = vert_colors.pop()
  vt.fillcolor(new_color)
  vt.goto( -tloc, 350)
  vt.setheading(270)
  
  tloc += 50
#speed of the turtles
s_ht = 3
s_vt = 3

# TODO: move turtles across and down screen, stopping for collisions

steps = 0
iter = 5
iter2 = 0
for steps in range(50):
  for ht in horiz_turtles:
    for vt in vert_turtles:
      if len(horiz_turtles) == 6:
        ht.forward(3)
        vt.forward(3)
      if len(horiz_turtles) == 5:
        ht.forward(2.5)
        vt.forward(2.5)
      if len(horiz_turtles) == 4:
        ht.forward(2)
        vt.forward(2)
      if len(horiz_turtles) == 3:
        ht.forward(1.5)
        vt.forward(1.5)
      if len(horiz_turtles) == 2:
        ht.forward(1)
        vt.forward(1)
      if len(horiz_turtles) == 1:
        ht.forward(0.5)
        vt.forward(0.5)
  if (abs(ht.xcor() - vt.xcor()) < 10):
    ht.shape("arrow")
    ht.color("blue")
    ht.back(50)
    ht.shape(turtle_shapes[iter])
    ht.color(new_horiz_colors[iter2])
  if (abs(ht.ycor() - vt.ycor()) < 10):
    vt.shape("turtle")
    vt.color("grey")
    vt.back(50)
    vt.shape(turtle_shapes[iter])
    vt.color(new_vert_colors[iter2])
    iter -= 1
    iter2 += 1
    horiz_turtles.remove(ht)
    vert_turtles.remove(vt)
steps = steps + 1





wn = trtl.Screen()
wn.mainloop()