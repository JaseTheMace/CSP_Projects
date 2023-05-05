#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
spider = trtl.Turtle()
#Create a spider body
spider.pensize(40)
spider.circle(20)
#Configure spider legs
num_of_legs = 8
length_of_leg = 70
angle_of_legs = 180 / num_of_legs
spider.pensize(5)
place_of_leg = 0
while (place_of_leg < num_of_legs):
  if place_of_leg < 4:
    spider.goto(0,20)
    spider.setheading(angle_of_legs * place_of_leg - 45)
    #Draw legs
    spider.forward(length_of_leg)
    place_of_leg = place_of_leg + 1
  else:
    spider.goto(0,20)
    spider.setheading(angle_of_legs * place_of_leg + 45)
    #Draw legs
    spider.forward(length_of_leg)
    place_of_leg = place_of_leg + 1
spider.hideturtle()
#Draw eye 1
spider.penup()
spider.color("red")
spider.fillcolor("red")
spider.goto(5,1)
spider.pendown()
spider.begin_fill()
spider.circle(5)
spider.end_fill()
#Draw eye 2
spider.penup()
spider.goto(-15,3)
spider.pendown()
spider.begin_fill()
spider.circle(5)
spider.end_fill()



wn = trtl.Screen()
wn.mainloop()