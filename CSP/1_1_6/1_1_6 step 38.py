#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
spider = trtl.Turtle()
length = 70
num_of_legs = 8
angle_of_legs = 240 / num_of_legs
spider.pensize(5)
place_of_leg = 0

while (place_of_leg < num_of_legs / 2):
  spider.penup()
  spider.goto(0,20)
  spider.setheading(angle_of_legs * place_of_leg - 60 + 240)
  #Draw legs
  spider.pendown()
  spider.circle(50,-120)
  spider.penup()
  place_of_leg = place_of_leg + 1
place_of_leg = 0
while (place_of_leg < num_of_legs / 2):
  spider.penup()
  spider.goto(0,20)
  spider.setheading(angle_of_legs * place_of_leg - 45 + 150)
  #Draw legs
  spider.pendown()
  spider.circle(50,120)
  spider.penup()
  place_of_leg = place_of_leg + 1
place_of_leg = 0 


spider.speed(0)
#Create a spider body
#Configure spider legs
spider.fillcolor("black")
spider.pensize(20)
spider.penup()
spider.goto(-20,0)
spider.pendown()
spider.begin_fill()
spider.circle(30)
spider.end_fill()

spider.penup()
spider.goto(-5,-40)
spider.pendown()
spider.begin_fill()
spider.circle(20)
spider.end_fill()



#Draw eye 1
spider.pensize(5)
spider.penup()
spider.color("red")
spider.fillcolor("red")
spider.goto(-10,-40)
spider.pendown()
spider.begin_fill()
spider.circle(5)
spider.end_fill()
#Draw eye 2
spider.penup()
spider.goto(10,-35)
spider.pendown()
spider.begin_fill()
spider.circle(5)
spider.end_fill()

spider.hideturtle()

wn = trtl.Screen()
wn.mainloop()