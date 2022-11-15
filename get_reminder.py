import time
from tkinter import *
import tkinter.messagebox
import tkinter

root = tkinter.Tk()

root.title("Click the button for pop up message")
root.geometry('500x300')
message = tkinter.StringVar()


def onClick():
    tkinter.messagebox.showinfo(
        "Hello I am Tualy and here to assist!", "Hi I'm your message")


button = Button(root, text="Click Me!!!!!",
                command=onClick, height=5, width=10)


button.pack(side='bottom')
root.mainloop()

text = str(input("Enter reminder here! :"))

local_time = float(input("In how many minutes from now? :"))
local_time = local_time*60
time.sleep(local_time)
print(text)
