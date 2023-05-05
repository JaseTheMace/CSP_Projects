import turtle as trtl
#   a114_divisible.py

# get two numbers from user
number_1 = int(input("Enter a number: "))

number_2 = int(input("Enter a number: "))
# loop while the numbers are not divisible (the remainder is 0)
while (number_1 % number_2 != 0):
  print("Those numbers are not divisible.")
  break
else:
  print(number_1 % number_2)

# inform user of result 

# gather user input again
while number_1 % number_2 != 0:
  number_1 = int(input("Enter a number: "))

  number_2 = int(input("Enter a number: "))

  if number_1 % number_2 != 0:
    print("Those numbers are not divisible.")
# inform user of result 

wn = trtl.Screen()
wn.mainloop()