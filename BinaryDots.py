from tkinter import * 
from tkinter.ttk import *
from time import strftime 
import tkinter as tk

def easy_frame():
	board = Canvas(root)
	board.config(width=500,height=500)
	board.create_rectangle(0, 0, 125, 125, outline = 'BLACK')
	board.create_rectangle(125, 0, 250, 125, outline = 'BLACK')
	board.create_rectangle(250, 0, 375, 125, outline = 'BLACK')
	board.create_rectangle(375, 0, 505, 125, outline = 'BLACK')

	board.create_rectangle(0,125,125,250, outline = 'BLACK')
	board.create_rectangle(125, 125, 250, 250, outline = 'BLACK')
	board.create_rectangle(250, 125, 375, 250, outline = 'BLACK')
	board.create_rectangle(375,125,505,250, outline = 'BLACK')

	board.create_rectangle(0, 250, 125, 375, outline = 'BLACK')
	board.create_rectangle(125, 250, 250, 375, outline = 'BLACK')
	board.create_rectangle(250, 250, 375, 375, outline = 'BLACK')
	board.create_rectangle(375, 250, 505, 375, outline = 'BLACK')

	board.create_rectangle(0,375, 125,500, outline = 'BLACK')
	board.create_rectangle(125,375, 250,505, outline = 'BLACK')
	board.create_rectangle(250,375, 375,505, outline = 'BLACK')
	board.create_rectangle(375,375, 505,505, outline = 'BLACK')

	board.pack()
	button1.destroy()
	button2.destroy()
	button3.destroy()
	frame.destroy()
'''
	

	'''

def medium_frame():
	board = Canvas(root)
	board.pack()

def hard_frame():
	board = Canvas(root)
	board.pack()

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