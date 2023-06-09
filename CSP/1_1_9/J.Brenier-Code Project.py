import turtle as trtl

phone = trtl.Turtle()
phone.shape('turtle')

#Move to start position
phone.penup()
phone.goto(-200,200)
phone.pendown()

#Draw phone
phone.speed(0)
phone.forward(300)
phone.circle(-40,90)
phone.forward(400)
phone.circle(-40,90)
phone.forward(300)
phone.circle(-40,90)
phone.forward(400)
phone.circle(-40,90)

phone.penup()
phone.goto(-175,175)
phone.pendown()

phone.forward(250)
phone.circle(-40,90)
phone.forward(350)
phone.circle(-40,90)
phone.forward(250)
phone.circle(-40,90)
phone.forward(350)
phone.circle(-40,90)

#Draw apps 

#1-Spotify
phone.penup()
phone.goto(-185,155)
phone.pendown()
phone.forward(70)
phone.right(90)
phone.forward(70)
phone.right(90)
phone.forward(70)
phone.right(90)
phone.forward(70)
phone.right(90)

#2-Tik Tok
phone.penup()
phone.goto(-95,155)
phone.pendown()
phone.forward(70)
phone.right(90)
phone.forward(70)
phone.right(90)
phone.forward(70)
phone.right(90)
phone.forward(70)
phone.right(90)

#3-Youtube
phone.penup()
phone.goto(-5,155)
phone.pendown()
phone.forward(70)
phone.right(90)
phone.forward(70)
phone.right(90)
phone.forward(70)
phone.right(90)
phone.forward(70)
phone.right(90)

#4-Face Time
phone.penup()
phone.goto(-185,-5)
phone.pendown()
phone.forward(70)
phone.right(90)
phone.forward(70)
phone.right(90)
phone.forward(70)
phone.right(90)
phone.forward(70)
phone.right(90)

#5-Messages
phone.penup()
phone.goto(-95,-5)
phone.pendown()
phone.forward(70)
phone.right(90)
phone.forward(70)
phone.right(90)
phone.forward(70)
phone.right(90)
phone.forward(70)
phone.right(90)

#6-Telegram
phone.penup()
phone.goto(-5,-5)
phone.pendown()
phone.forward(70)
phone.right(90)
phone.forward(70)
phone.right(90)
phone.forward(70)
phone.right(90)
phone.forward(70)
phone.right(90)

#7-Call
phone.penup()
phone.goto(-185,-165)
phone.pendown()
phone.forward(70)
phone.right(90)
phone.forward(70)
phone.right(90)
phone.forward(70)
phone.right(90)
phone.forward(70)
phone.right(90)

#8-Widgetsmith
phone.penup()
phone.goto(-95,-165)
phone.pendown()
phone.forward(70)
phone.right(90)
phone.forward(70)
phone.right(90)
phone.forward(70)
phone.right(90)
phone.forward(70)
phone.right(90)

#9-Gmail
phone.penup()
phone.goto(-5,-165)
phone.pendown()
phone.forward(70)
phone.right(90)
phone.forward(70)
phone.right(90)
phone.forward(70)
phone.right(90)
phone.forward(70)
phone.right(90)


#Draw app pictures

#Spotify
phone.penup()
phone.goto(-150,95)
phone.pendown()
phone.circle(25)
phone.penup()
phone.left(90)
phone.forward(35)
phone.left(90)
phone.forward(10)
phone.right(180)
phone.pendown()
phone.forward(25)
phone.penup()
phone.right(90)
phone.forward(10)
phone.right(90)
phone.forward(5)
phone.pendown()
phone.forward(20)
phone.penup()
phone.left(90)
phone.forward(10)
phone.left(90)
phone.forward(5)
phone.pendown()
phone.forward(12.5)

#Tik Tok
phone.pensize(8)
phone.penup()
phone.goto(-65,125)
phone.pendown()
phone.circle(-15,-270)
phone.right(180)
phone.forward(30)
phone.circle(-15,-90)
phone.pensize(1)

#Youtube
phone.penup()
phone.goto(5,145)
phone.pendown()
phone.right(180)
phone.forward(50)
phone.right(90)
phone.forward(40)
phone.right(90)
phone.forward(50)
phone.right(90)
phone.forward(40)
phone.right(90)
phone.penup()
phone.forward(15)
phone.right(90)
phone.forward(10)
phone.pendown()
phone.forward(20)
phone.left(120)
phone.forward(20)
phone.left(120)
phone.forward(20)
phone.left(120)

#Face Time
phone.penup()
phone.goto(-175,-15)
phone.pendown()
for i in range(6):
  phone.forward(40)
  phone.left(90)
phone.forward(15)
phone.right(135)
phone.forward(20)
phone.left(135)
phone.forward(40)
phone.left(135)
phone.forward(20)
phone.left(45)

#Messages
phone.penup()
phone.goto(-85,-15)
phone.pendown()
phone.forward(40)
phone.left(90)
phone.forward(50)
phone.left(90)
phone.forward(40)
phone.left(90)
phone.forward(50)
phone.penup()
phone.left(90)
phone.forward(40)
phone.left(90)
phone.forward(10)
phone.pendown()
phone.right(90)
phone.forward(20)
phone.left(135)
phone.forward(25)

#Telegram
phone.penup()
phone.goto(55,-15)
phone.pendown()
phone.left(90)
phone.circle(30,360,3)
phone.left(90)
phone.penup()
phone.forward(30)
phone.pendown()
phone.forward(20)

#Call
phone.left(135)
phone.penup()
phone.goto(-155,-175)
phone.pendown()
phone.forward(5)
phone.right(90)
phone.forward(15)
phone.right(90)
phone.forward(5)
phone.left(90)
phone.forward(25)
phone.left(90)
phone.forward(5)
phone.right(90)
phone.forward(15)
phone.right(90)
phone.forward(15)
phone.right(90)
phone.forward(55)
phone.right(90)
phone.forward(10)

#Widgetsmith
phone.penup()
phone.goto(-85,-175)
phone.pendown()
phone.pensize(2)
for i in range(4):
  phone.forward(50)
  phone.right(90)
phone.pensize(8)

#Gmail
phone.penup()
phone.goto(10,-225)
phone.pendown()
phone.left(90)
phone.forward(40)
phone.right(135)
phone.forward(30)
phone.left(90)
phone.forward(30)
phone.right(135)
phone.forward(40)

wn = trtl.Screen()
wn.mainloop()