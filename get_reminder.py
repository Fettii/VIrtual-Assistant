
import time
from tkinter import *
import tkinter.messagebox
import tkinter

root = tkinter.Tk()

root.title("Reminders")
root.geometry('500x300')
message_var = tkinter.StringVar()
timer_var = tkinter.StringVar()


def onClick():
    message = message_var.get()
    message_var.set("")

    timer = float(timer_var.get())
    timer = timer*60
    time.sleep(timer)
    tkinter.messagebox.showinfo("Current Reminder", message)


submit_but = Button(root, text="Submit",
                    command=onClick)

message_entry = tkinter.Entry(root, textvariable=message_var,
                              font=('calibre', 10, 'normal'))
timer_entry = tkinter.Entry(root, textvariable=timer_var,
                            font=('calibre', 10, 'normal'))
timer_label = tkinter.Label(root, text='Timer: ', font=('calibre', 10, 'bold'))
message_label = tkinter.Label(
    root, text='Message: ', font=('calibre', 10, 'bold'))

message_label.grid(row=0, column=0)
submit_but.grid(row=2, column=0)
message_entry.grid(row=0, column=1)
timer_entry.grid(row=1, column=1)
timer_label.grid(row=1, column=0)

root.mainloop()
