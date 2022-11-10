from tkinter import * 
from tkinter.ttk import *
import os
import random
import datetime as dt
import getpass
import ssl
import smtplib
from email.message import EmailMessage



def process():
    user_input = statement.get().lower()
  
    if "joke" in user_input:
      joke()

    if "reminder" in user_input:
      pass

    if "forecast" in user_input:
      pass

    if "date" in user_input:
      date()

    if "email" in user_input:
      email()
      
    if "time" in user_input:
      time_zone = input("Type in your timezone, (ex: MST = US/Arizona, CST = US/Central, EST= US/Eastern, HST = US/Hawaii, PST = America/Los_Angeles) *Type in Abbreviation*: ")
      time(time_zone)
      



def joke():
  # opens list of jokes
  file = open("jokes.txt")
  content = file.readlines()
  # randomly selects a number from 1 to 100
  number=(random.randrange(1, 100))
  selected_joke = content[number]
  updateconsole(selected_joke)


def email():
    email_send = input("Enter email please: ")
    password = getpass.getpass(
    "FOR GMAIL ONLY PLEASE ENABLE TWO STEP VERIFIACTION AND ENTER IN APP PASSWORD ONLY: ")
    email_recieve = input("Enter To Address Please: ")

    subject = input('Enter subject: ')
    body = input("Please enter body: ")

    em = EmailMessage()
    em['From'] = email_send
    em['To'] = email_recieve
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as       smtp:
      smtp.login(email_send, password)
      smtp.sendmail(email_send, email_recieve, em.as_string())

def date():
  todays_date = dt.datetime.now()
  if todays_date.month == 1:
    month = "January"
  elif todays_date.month == 2:
    month = "February"
  elif todays_date.month == 3:
    month = "March"
  elif todays_date.month == 4:
    month = "April"
  elif todays_date.month == 5:
    month = "May"
  elif todays_date.month == 6:
    month = "June"
  elif todays_date.month == 7:
    month = "July"
  elif todays_date.month == 8:
    month = "August"
  elif todays_date.month == 9:
    month = "September"
  elif todays_date.month == 10:
    month = "October"
  elif todays_date.month == 11:
    month = "November"
  elif todays_date.month == 12:
    month = "December"
  the_date = (str(month) + " " + str(todays_date.day) + "," + " " + str(todays_date.year))
  updateconsole(the_date)

from datetime import datetime
import pytz

def time(time_zone):
  if time_zone == 'MST':
    time_zone = 'US/Arizona'
  elif time_zone == 'CST':
    time_zone = 'US/Central'
  elif time_zone == 'EST':
    time_zone = 'US/Eastern'
  elif time_zone == 'HST':
    time_zone = 'US/Hawaii'
  elif time_zone == 'PST':
    time_zone = 'America/Los_Angeles'
  time = pytz.timezone(time_zone)
  current_time = datetime.now(time)
  t = current_time.strftime('%I:%M %p')
  #current_time = pytz.all_timezones (check all timezones)
  updateconsole(t)


''''' function changes the label on the gui '''

def updateconsole(message):
  console.config(text = message, font = ("Times", 10),wraplength=console.winfo_width())

''''' function generates the gui and homepage'''

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
    console= Label(labelframe, text = 'Welcome to your Virtual Assistant\n Would you like to: \n Send an Email ~ Set a Reminder ~ \nHear a joke ~ See the forecast~ See the date ', background = "White", justify = "center", width = 50)
    console.grid( row = 2, column = 1, columnspan= 10, padx = 20, pady= 20)
    statement.grid(row = 10 , column = 1,padx=5, pady = 20)
    b = Button(master, text = "Enter", command = process)
    b.grid(row = 11, column = 1, padx = 5, pady = 10)
 

    master.mainloop()

homescreen()


