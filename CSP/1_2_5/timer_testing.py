import turtle as trtl

import random as rand

import leaderboard as lb


#TIMER

leaderboard_file_name = "a122_leaderboard.txt"
player_name = input("Please enter your name: ")


font_setup = ("Arial", 20, "normal")
timer = 30
counter_interval = 1000   #1000 represents 1 second
timer_up = False 
time_left = 20

block_color = "white"
block_shape = "square"
block_size = 5
score = 0

block = trtl.Turtle()
block.shapesize(block_size)
block.fillcolor(block_color)
block.shape("square")

def update_timer():
  global time_left, game_over
  if time_left > 0:
    time_left -= 1
    block.screen.ontimer(update_timer,1000)
    block.screen.title("TURTLE GAME - Score: {} - THE TIME: {}".format(score,time_left))
  else:
    game_over = True
    manage_leaderboard()
    block.hideturtle()
    block.screen.title("Turtle Game -Score {} - NO MO TIME".format(score))

def manage_leaderboard():

  global score
  global block

  # get the names and scores from the leaderboard file
  leader_names_list = lb.get_names(leaderboard_file_name)
  leader_scores_list = lb.get_scores(leaderboard_file_name)

  # show the leaderboard with or without the current player
  if (len(leader_scores_list) < 5 or score >= leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(True, leader_names_list, leader_scores_list, block, score)

  else:
    lb.draw_leaderboard(False, leader_names_list, leader_scores_list, block, score)

#-----events----------------

wn = trtl.Screen()
update_timer()
wn.mainloop()