#   a114_zero_iteration_and_infinite.py
#   Make a zero-iteration condition and follow it with an infinite loop.
#   Include some visual evidence that the second loop is infinite.
import turtle as trtl

painter = trtl.Turtle()
painter.speed(0)

# Add a loop with a zero-iteration condition
loop_letter = "a"

while (loop_letter == "c"):
  painter.right(90)
  painter.forward(100)
  painter.left(70)
  painter.forward(200)
  painter.circle(20)


# Add an infinite loop
loop_letter = "c"

painter.penup()
painter.goto(50,100)
painter.pendown()

while (loop_letter == "c"):
  painter.right(90)
  painter.forward(25)
  painter.left(70)
  painter.forward(75)
  painter.circle(20)

  
wn = trtl.Screen()
wn.mainloop()