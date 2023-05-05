#--import statements-----

import turtle as trtl

import random as rand

#-----game configuration----

block_color = "blue"
block_shape = "square"
block_size = 5
score = 0

font_setup = ("Arial", 20, "normal")
timer = 30
counter_interval = 1000   #1000 represents 1 second
timer_up = False 
time_left = 20

#-----initialize turtle-----

block = trtl.Turtle()
block.shapesize(block_size)
block.fillcolor(block_color)
block.shape("square")

score_writer = trtl.Turtle()
score_writer.shape("turtle")
score_writer.fillcolor("white")
score_writer.color('white')

counter =  trtl.Turtle()
counter.shape("arrow")
counter.fillcolor('white')
counter.color('white')

counter.penup()
counter.goto(150,200)
counter.pendown()

#-----game functions--------
block.penup()
rand.randint(-400,400)

def spot_clicked(x,y):

  change_position()

def change_position():
  new_xpos = rand
  new_ypos = rand
  block.goto(rand.randint(-400,400),rand.randint(-400,400))
  update_score(0,0)

def update_score(x,y):
  global score
  score = score + 1
  score_writer.clear()
  score_writer.write(score, font=font_setup)

score_writer.penup()
score_writer.goto(100,200)
score_writer.pendown()

def update_timer():
  global time_left, game_over
  if time_left > 0:
    time_left -= 1
    block.screen.ontimer(update_timer,1000)
    block.screen.title("TURTLE GAME - Score: {} - THE TIME: {}".format(score,time_left))
  else:
    game_over = True
    block.hideturtle()
    block.screen.title("Turtle Game -Score {} - NO MO TIME".format(score))
#-----events----------------

wn = trtl.Screen()
change_position()
block.onclick(spot_clicked)
update_timer()
wn.mainloop()