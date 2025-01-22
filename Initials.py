#Aiden Ramos
#Math 261
#Initials
# This program will use Turtle to draw my Initials

import turtle as T
T.penup()
T.pensize(10)


def draw_a(): #function to draw A
    
    T.goto(-70,-50)
    T.pendown()
    
    T.left(70)
    T.forward(100)
    T.right(140)
    T.forward(100)
    T.backward(50)
    T.right(110)
    T.forward(35)
    T.penup()


def draw_r(): #function to draw R
    T.penup()
    T.goto(20,-50)
    T.setheading(90) # sets to facing up
    T.pendown()
    
    T.forward(100)
    T.right(90)
    T.circle(-30,180) #makes semi-circle of the R
    
    T.setheading(315) #points at the proper angle to draw the final line of the R
    T.forward(60)
    T.penup()


#calls both functions to draw the letters
draw_a()
draw_r()