#   a123_apple_1.py
import turtle as trtl
import random as rand

#-----setup-----

apple_image = "apple.gif" # Store the file name of your shape
ground_height = -200
apple_letter_x_offset = -25
apple_letter_y_offset = -50
screen_width = 400
screen_height = 400
letters = ["A","B","C","D","E","F","G","H","I","J","K","L",
"M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file

apple = trtl.Turtle()
letter = trtl.Turtle()

apple.penup()
letter.penup()
letter.hideturtle()

wn.bgpic("background.gif")

current_letter = "A"
wn.tracer(False)

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file

def reset_apple(active_apple):
  global current_letter
  length_of_list = len(letters)
  if (length_of_list != 0):
    index = rand.randint(0,length_of_list)
    active_apple.goto(rand.randint(-(screen_width)/2, (screen_width)/2), rand.randint(-(screen_height)/2, (screen_height)/2))
    current_letter = letters.pop(index)
    draw_apple(active_apple, current_letter)

def draw_apple(active_apple, letter):
  active_apple.shape(apple_image)
  active_apple.showturtle()
  draw_letter(active_apple, letter)
  wn.update()

def drop_apple():
  wn.tracer(True)
  apple.goto(apple.xcor(), ground_height)
  apple.clear()
  apple.hideturtle()
  wn.tracer(False)
  reset_apple(apple)

def draw_letter(active_apple, letter):
  active_apple.color("white")
  remember_position = active_apple.position()
  active_apple.setpos(active_apple.xcor() + apple_letter_x_offset,active_apple.ycor() + apple_letter_y_offset)
  active_apple.write(letter, font=("Arial", 44, "bold"))
  active_apple.setpos(remember_position)

#-----function calls-----
draw_apple(apple, current_letter)

def check_apple_a():
  if (current_letter == "a"):
    drop_apple()

def check_apple_b():
  if (current_letter == "b"):
    drop_apple()

def check_apple_c():
  if (current_letter == "c"):
    drop_apple()

def check_apple_d():
  if (current_letter == "d"):
    drop_apple()

def check_apple_e():
  if (current_letter == "e"):
    drop_apple()

def check_apple_f():
  if (current_letter == "f"):
    drop_apple()

def check_apple_g():
  if (current_letter == "g"):
    drop_apple()

def check_apple_h():
  if (current_letter == "h"):
    drop_apple()

def check_apple_i():
  if (current_letter == "i"):
    drop_apple()

def check_apple_j():
  if (current_letter == "j"):
    drop_apple()

def check_apple_k():
  if (current_letter == "k"):
    drop_apple()

def check_apple_l():
  if (current_letter == "l"):
    drop_apple()

def check_apple_m():
  if (current_letter == "m"):
    drop_apple()

def check_apple_n():
  if (current_letter == "n"):
    drop_apple()

def check_apple_o():
  if (current_letter == "o"):
    drop_apple()

def check_apple_p():
  if (current_letter == "p"):
    drop_apple()

def check_apple_q():
  if (current_letter == "q"):
    drop_apple()

def check_apple_r():
  if (current_letter == "r"):
    drop_apple()

def check_apple_s():
  if (current_letter == "s"):
    drop_apple()

def check_apple_t():
  if (current_letter == "t"):
    drop_apple()

def check_apple_u():
  if (current_letter == "u"):
    drop_apple()

def check_apple_v():
  if (current_letter == "v"):
    drop_apple()

def check_apple_w():
  if (current_letter == "w"):
    drop_apple()

def check_apple_x():
  if (current_letter == "x"):
    drop_apple()

def check_apple_y():
  if (current_letter == "y"):
    drop_apple()

def check_apple_z():
  if (current_letter == "z"):
    drop_apple()

wn.onkeypress(check_apple_a, "a")
wn.onkeypress(check_apple_b, "b")
wn.onkeypress(check_apple_c, "c")
wn.onkeypress(check_apple_d, "d")
wn.onkeypress(check_apple_e, "e")
wn.onkeypress(check_apple_f, "f")
wn.onkeypress(check_apple_g, "g")
wn.onkeypress(check_apple_h, "h")
wn.onkeypress(check_apple_i, "i")
wn.onkeypress(check_apple_j, "j")
wn.onkeypress(check_apple_k, "k")
wn.onkeypress(check_apple_l, "l")
wn.onkeypress(check_apple_m, "m")
wn.onkeypress(check_apple_n, "n")
wn.onkeypress(check_apple_o, "o")
wn.onkeypress(check_apple_p, "p")
wn.onkeypress(check_apple_q, "q")
wn.onkeypress(check_apple_r, "r")
wn.onkeypress(check_apple_s, "s")
wn.onkeypress(check_apple_t, "t")
wn.onkeypress(check_apple_u, "u")
wn.onkeypress(check_apple_v, "v")
wn.onkeypress(check_apple_w, "w")
wn.onkeypress(check_apple_x, "x")
wn.onkeypress(check_apple_y, "y")
wn.onkeypress(check_apple_z, "z")

wn.listen()
wn.mainloop()