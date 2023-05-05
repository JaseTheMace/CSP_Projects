import turtle as trtl
import random as rand

#--------Setup--------
wn = trtl.Screen()
maze = trtl.Turtle()
distance = 10

def move():
  maze.forward(distance)

def penup():
  maze.penup()

def pendown():
  maze.pendown()

wn.onkeypress(penup,'q')

wn.onkeypress(pendown,'w')

wn.onkeypress(move,'e')










wn.listen()
wn.mainloop()