#Aiden Ramos
#Math 261
#Circles 
#This program will ask the user for the diamter of a circle and outputs the circumference and area of the circle
#Then draws a circle with that radius in the Turtle environment

import time as TI
#time is only here so all outputs do not all show up at once
import turtle as T
import math as M

#prompts the user for the diamter
diamter=float(input("Please enter a diamter between the numbers 20 and 150: "))

radius=diamter//2

pi=M.pi


#finds the circumference and area of the circle
circumference=pi*diamter

area=pi*(radius**2)

#displays the results to the user
print(f"The circumference of the circle {circumference:.2f}px\n")
TI.sleep(1)
print(f"The area of the circle is {area:.2f}px\n")

TI.sleep(1)

print("Creating your Turtle Circle...")

TI.sleep(3)

T.circle(radius)

T.done()
