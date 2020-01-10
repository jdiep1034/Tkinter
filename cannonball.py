from Mapping_for_Tkinter import Mapping_for_Tkinter
from tkinter import *
import math
import time


m = Mapping_for_Tkinter(0.0 ,1200.0 ,0.0 ,400.0 ,1200)
user1 = input("Enter velocity,theta(0,90),strength (Leave space between each value)(return for default 70,60,0.75): ")

#Default Condition
if user1 == "":
    v, theta, strength = 70, 60, 0.75

#Custom Condition
else:
    v, theta, strength = user1.split()
    v, theta, strength = float(v), float(theta), float(strength)

#Theta to radians
theta = math.radians(theta)

window = Tk() # instantiate a tkinter window
canvas = Canvas(window, width=m.get_width(),height=m.get_height(),bg="white") # create a canvas width*height
canvas.pack()

#Creates ball
ball = canvas.create_oval(m.get_i(-4), m.get_j(-4), m.get_i(4), m.get_j(4), fill = "blue")

#Set variables
x = 0
y = 0
rebound = 0
tTime = 0
bTime = 0

#Continue until velocity is very small
while v > 0.01:
    xo = x
    yo = y

    #Change in motion based on time
    changeX = v * math.cos(theta) * 0.1
    changeY = (v * math.sin(theta) * bTime) - (4.9 * bTime**2)
    x += changeX
    y = changeY

    #Condition for when ball rebounds
    if y < 0:
        v *= strength
        y = 0
        rebound += 1
        bTime = 0

    #Dotted line following ball
    canvas.create_rectangle(((m.get_i(x)), m.get_j(y))*2,outline = "black")

    #Move the ball based on change in motion
    canvas.move(ball, m.get_i(x) - m.get_i(xo), m.get_j(y) - m.get_j(yo))

    tTime += 0.1
    bTime += 0.1
    
    time.sleep(0.01)
    window.update()

    #Condition for when ball reaches right side of the screen
    if x > m.get_xmax():
        break

#Print information
print("Total number of rebounds is: " + str(rebound))
print("Total time is: " + str(tTime) + "s")

#Turns ball red when finished
canvas.itemconfig(ball,fill="red")


window.mainloop()
