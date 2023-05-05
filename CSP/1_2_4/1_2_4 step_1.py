import turtle as trtl
import random as rand

#--------Setup--------
wn = trtl.Screen()
maze = trtl.Turtle()
maze_runner = trtl.Turtle()

num_of_walls = 36
path_width = 20
maze.pensize(5)
maze.pencolor('pink')
maze.speed(0)
maze.penup()
maze.goto(40,-40)
maze.pendown()

maze_runner_shape = input("What shape do you want?: ")
maze_runner.shape(maze_runner_shape)
#--------functions--------

def draw_door(position):
  maze.forward(position)
  maze.penup()
  maze.forward(path_width*2)
  maze.pendown()

def draw_barrier(position):
  maze.forward(position)
  maze.left(90)
  maze.forward(path_width*2)
  maze.backward(path_width*2)
  maze.right(90)

maze_runner.fillcolor('blue')
maze_runner.penup()
maze_runner.goto(-path_width*2, path_width*2)
maze_runner.pendown()

wall_len = path_width
for i in range(num_of_walls):
  wall_len += path_width

  if (i > 4):
    maze.left(90)

    door = rand.randint(path_width*2, (wall_len - path_width*2))
    barrier = rand.randint(path_width*2, (wall_len - path_width*2))

    while abs(door - barrier) < path_width:
      door = rand.randint(path_width*2, (wall_len - path_width*2))

    if (door < barrier):
      draw_door(door)
      draw_barrier(barrier - door - path_width*2)
      maze.forward(wall_len - barrier)
    else:
      draw_barrier(barrier)
      draw_door(door - barrier)

      maze.forward(wall_len - door - path_width*2)

maze.hideturtle()
def Go_Up():
  maze_runner.setheading(90)

def Go_Right():
  maze_runner.setheading(0)

def Go_Left():
  maze_runner.setheading(180)

def Go_Down():
  maze_runner.setheading(270)

def Slow_Speed():
  maze_runner.forward(5)

def Med_Speed():
  maze_runner.forward(10)

def Fast_Speed():
  maze_runner.forward(20)

wn.onkeypress(Go_Up, 'Up')
wn.onkeypress(Go_Right, 'Right')
wn.onkeypress(Go_Left, 'Left')
wn.onkeypress(Go_Down, 'Down')
wn.onkeypress(Slow_Speed, 'q')
wn.onkeypress(Med_Speed, 'w')
wn.onkeypress(Fast_Speed, 'e')



wn.listen()
wn.mainloop()