#2019-20 Fall Computer Science Principles Final Exam

#Ms. Haubold


#Name
# Juel Wiseman  
#Date
# December 19, 2019


#### INSTRUCTIONS ####
#Create an etch a sketch turtle game
#The turtle should move with the arrow keys (up, down, left and right), and draw
#Space should clear the screen
#o and p should make the pen size bigger and smaller
#u should pick the pen up or put the pen down
#All code must be commented
#BONUS
#Add a feature to change colors
#


#import required libraries
import turtle as trtl
import random as rand
#create turtle
drawer = trtl.Turtle()

#setting variables
pensize = 5
pen = 6
color = 6
#movement functions
def up():
    drawer.seth(90)
    drawer.forward(10)

def right():
    drawer.seth(0)
    drawer.forward(10)

def left():
    drawer.seth(180)
    drawer.forward(10)

def down():
    drawer.seth(270)
    drawer.forward(10)

# increasing and decreasing pensize

def big_pen():
    drawer.pensize(pensize +1)

def small_pen():
    drawer.pensize(pensize -1)

# picking up and putting down the pen
def upsy_downsy_daisy():
    if(pen < 1):
        drawer.penup()

    else:
        drawer.pendown()

#clearing screen
def screen_clear():
    drawer.reset()

#color/drawing functions
def change_color():
    if (color < 1):
        drawer.color("red")

#create screen

#bind to keypresses
wn = trtl.Screen()

wn.onkeypress(up, "Up")
wn.onkeypress(right, "Right")
wn.onkeypress(left, "Left")
wn.onkeypress(down, "Down")
wn.onkeypress(big_pen, "o")
wn.onkeypress(small_pen, "p")
wn.onkeypress(screen_clear, "space")
wn.onkeypress(change_color, "c")
wn.onkeypress(upsy_downsy_daisy, "u")

#listen
wn.listen()

#mainloop
wn.mainloop()