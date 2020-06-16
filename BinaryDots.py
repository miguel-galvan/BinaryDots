from tkinter import * 
from tkinter.ttk import *
from time import strftime 
import tkinter as tk

#simple window example 
root = Tk()
root.minsize(500,500) #minsize sets the size of the window 
root.config(bg = "#a4f6f9") #this sets a different color to the background

start_button = Button(root, text='Play Binary Dots')
start_button.pack()
start_button.place(relx=0.5, rely=0.5, anchor=CENTER)#places the intro button right in the center of the window


mainloop()