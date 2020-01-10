from Mapping_for_Tkinter import Mapping_for_Tkinter
from tkinter import *
from math import *

#Formula input
formula = input("Enter math formula (using x variable, ie. sin(x)**2): ")

in_put = input("Enter xmin,xmax,ymin,ymax (return for default -5,5,-5,5): ")    #User input
if (in_put == ""):                                                              #Default input
    xmin, xmax, ymin, ymax = -5.0, 5.0, -5.0, 5.0
    m=Mapping_for_Tkinter(-5.0,5.0,-5.0,5.0,800)
else:                                                                           #Custom input
    xmin, xmax, ymin, ymax = in_put.split()
    xmin, xmax, ymin, ymax = float(xmin), float(xmax), float(ymin), float(ymax) 
    m=Mapping_for_Tkinter(xmin, xmax, ymin, ymax, 800)

    #Safeguards if input is invalid
    while xmax <= xmin:
        xmin, xmax = input("Your max is invalid (xmax<=xmin), Re-Enter correct [xmin,xmax]: ").split()
    while ymax <= ymin:
        ymin, ymax = input("Your max is invalid (ymax<=ymin), Re-Enter correct [ymin,ymax]: ").split()
    
window = Tk() # instantiate a tkinter window
canvas = Canvas(window, width=m.get_width(), height=m.get_height(),bg="white") # create a canvas width*height
canvas.pack()

#Creates axis if possible
if( xmin < 0 and xmax > 0):
    canvas.create_line(m.get_i(0),0,m.get_i(0),m.get_height())
        
if( ymin < 0 and ymax > 0):
    canvas.create_line(0,m.get_j(0),m.get_width(),m.get_j(0))

#Plots formula
for i in range(int(m.get_width())):
    x = m.get_x(i)
    y = eval(formula)
    canvas.create_rectangle((i,m.get_j(y))*2,outline="blue")


window.mainloop()  # wait until the window is closed
