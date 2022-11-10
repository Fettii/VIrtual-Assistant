from tkinter import * 
from tkinter.ttk import *
import os
import random


def process():
    user_input = statement.get().lower()
    '''''

    all functions will be called within this one !

    '''''
    if "joke" in user_input:
      joke()

    if "reminder" in user_input:
      print("this feature hasn't been implemented yet")

    if "forecast" in user_input:
      pass

    if "date" in user_input:
      pass

    if "email" in user_input:
      pass
      




def joke():
  # opens list of jokes
  file = open("jokes.txt")
  content = file.readlines()
  # randomly selects a number from 1 to 100
  number=(random.randrange(1, 100))
  selected_joke = content[number]
  updateconsole(selected_joke)















  

def updateconsole(message):
  console.config(text = message, font = ("Times", 10),wraplength=console.winfo_width())













def homescreen():
    global master
    master = Tk()
    master.geometry("400x400")
    master.columnconfigure(0, weight=1)
    master.columnconfigure(1, weight=3)
    master.columnconfigure(2, weight=1)
    
    global statement
    global console
    title = Label(master, text = "Tualy", font= ("Times",15))
    title.grid(row = 0, column = 1, padx = 5)
    x = StringVar()
    statement = Entry(master, textvariable = x)
    labelframe = Labelframe(master, text = "this is a frame").grid( row = 1, column= 0)
    console= Label(labelframe, text = 'Welcome to your Virtual Assistant\n Would you like to: \n Send an Email ~ Set a Reminder ~ \nHear a joke ~ See the forecast~ See the date ', background = "White", justify = "center")
    console.grid( row = 2, column = 1, columnspan= 10, padx = 20, pady= 20)
    statement.grid(row = 10 , column = 1,padx=5, pady = 20)
    b = Button(master, text = "Enter", command = process)
    b.grid(row = 11, column = 1, padx = 5, pady = 10)
 

    master.mainloop()

homescreen()


