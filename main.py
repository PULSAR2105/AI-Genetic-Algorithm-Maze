# -*- coding: utf-8 -*-
from tkinter import *
import random
import os

# Craation of the main window
window = Tk()
window.title("AI Genetic Algorithm Maze")

id_num = ()

def RightClick(event) :
    """ Event management Left-click on the graphic area"""
    # mouse pointer position
    X = event.x
    Y = event.y
    # on dessine un carré
    r = 20
    color = "%06x" % random.randint(0, 0xFFFFFF)
    color = "#" + color
    Canevas.create_rectangle(X-r, Y-r, X+r, Y+r, outline = 'black', fill = color, tags = "obstacle")

def LeftClick(event) :
    global id_num

    # Event management Left-click on the graphic area
    # mouse pointer position
    X = event.x
    Y = event.y

    id_num = Canevas.find_closest(X, Y, halo = None, start = None)
    print(id_num)

    r = 20
    Canevas.coords(id_num, X-r, Y-r, X+r, Y+r)   

def Drag(event) :
    global id_num

    # Event management Left-click on the graphic area
    # mouse pointer position
    X = event.x
    Y = event.y

    if id_num != () :
        # limite de l'objet dans la zone graphique
        if X < 0 : 
        	X = 0

        if X > width : 
        	X = width

        if Y < 0 : 
        	Y = 0

        if Y > height : 
        	Y = height

        #print(X, Y)

        # mise à jour de la position de l'objet (drag)
        r = 20
        Canevas.coords(id_num, X-r, Y-r, X+r, Y+r)   

def Erase():
    # Eraseing of the space of the canvas
    Canevas.delete("obstacle")

# Création of a widget Canevas
width = 500
height = 500
Canevas = Canvas(window, width = width, height = height, bg ='white')

# The bind() method allows you to link an event with a function:
# A left click on the graphic area will cause the user function to be called Click()
Canevas.bind('<Button-3>', RightClick)

Canevas.bind('<Button-1>', LeftClick)

Canevas.bind('<B1-Motion>',Drag)

Canevas.pack(padx =5, pady =5)

# Craation of a widget Button (erase button)
Button1 = Button(window, text ='Erase', command = Erase)
Button1.pack(side=LEFT, padx = 5,pady = 5)

# Craation of a widget Button (quit button)
Button2 = Button(window, text = 'Quit', command = window.destroy)
Button2.pack(side=LEFT, padx = 5,pady = 5)

# Lauching the event manager
window.mainloop() 

os.system("pause")
