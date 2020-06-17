from tkinter import * 
from tkinter.ttk import *
from time import strftime 
import tkinter as tk

def easy_frame():
	board = Canvas(root)
	board.config(width=500,height=500)

	for ycoordinate in range(0,500,125):
		for xcoordinate in range(0,500,125):
			board.create_rectangle(xcoordinate,ycoordinate,xcoordinate+125,ycoordinate+125,outline='BLACK')


	board.pack()
	button1.destroy()
	button2.destroy()
	button3.destroy()
	frame.destroy()

def medium_frame():
	board = Canvas(root)
	board.config(width=500,height=500)

	for ycoordinate in range(0,500,83):
		for xcoordinate in range(0,500,83):
			board.create_rectangle(xcoordinate,ycoordinate,xcoordinate+83,ycoordinate+83,outline='BLACK')

	board.pack()
	button1.destroy()
	button2.destroy()
	button3.destroy()
	frame.destroy()

def hard_frame():
	board = Canvas(root)
	board.config(width=500,height=500)

	for ycoordinate in range(0,500,62):
		for xcoordinate in range(0,500,62):
			board.create_rectangle(xcoordinate,ycoordinate,xcoordinate+62,ycoordinate+62,outline='BLACK')

	board.pack()
	button1.destroy()
	button2.destroy()
	button3.destroy()
	frame.destroy()



def raise_frame():
	start_button.destroy()
	global frame
	frame = Label(root)
	frame.pack()
	global button1, button2, button3
	button1 = Button(frame, text = "Easy", command = easy_frame)
	button1.pack()
	button2 = Button(frame, text = "Medium", command = medium_frame)
	button2.pack()
	button3 = Button(frame, text = "Hard", command = hard_frame)
	button3.pack()


#simple window example 
root = Tk()
root.minsize(500,500) #minsize sets the size of the window 
root.config(bg = "#a4f6f9") #this sets a different color to the background

start_button = Button(root, text='Play Binary Dots', command = raise_frame)
start_button.pack()
start_button.place(relx=0.5, rely=0.5, anchor=CENTER)#places the intro button right in the center of the window






mainloop()