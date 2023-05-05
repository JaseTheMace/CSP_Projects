from turtle import Turtle, Screen
import turtle as trtl
from random import random
import tkinter
import leaderboard as lb

#TIMER
import time
import datetime
 
# Create function that acts as a countdown
def countdown(seconds):
 
    # Number of seconds
    seconds = 20
    font_setup = ("Arial", 20, "normal")
    score = 0

    # While loop that checks if seconds reaches zero
    # If not zero, subtract time by one second
    while seconds > 0:
 
        # Timer represents time left on countdown
        timer = datetime.timedelta(seconds = seconds)
        
        # Prints the time left on the timer
        print(timer, end="\r")
 
        # Delays the program one second
        time.sleep(1)
 
        # Reduces the time by one second
        seconds -= 1
 
    print("Bzzzt! The countdown is at zero seconds!")


game = trtl.Turtle()

#DRAG TO DRAW
def drawColor(x, y):
    draw.color('blue')

def drag_draw(x, y):
    draw.ondrag(None)
    draw.goto(x, y)
    draw.ondrag(drag_draw)

#BUTTONS & PENSIZE
button = Turtle('circle', visible=False)
button.speed('fastest')
button.hideturtle()
button.up()

button.goto(350, 230)
button.shapesize(50 / 20)
button.showturtle()

#BLUE BUTTON

draw = Turtle('turtle')
draw.speed(0)
draw.pensize(4)
button.color('blue')
button.onclick(drawColor)
draw.ondrag(drag_draw)

#BLACK BUTTON

def drawColor(x, y):
    draw.color('black')

circle = Turtle('circle', visible=False)
circle.speed('fastest')
circle.hideturtle()
circle.up()
circle.goto(350, 170)
circle.shapesize(50 / 20)
circle.showturtle()
circle.color('black')
circle.onclick(drawColor)

countdown(20)

wn = trtl.Screen()
wn.listen()
window = Screen()
window.mainloop()
#update_timer()
wn.mainloop()