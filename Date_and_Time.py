# DATE
import datetime

def date():
  todays_date = datetime.datetime.now()
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
  return the_date
print(date())




#TIME
from datetime import datetime
import pytz

def time():
  time_zone = input("Type in your timezone, (ex: MST = US/Arizona, CST = US/Central, EST= US/Eastern, HST = US/Hawaii, PST = America/Los_Angeles) *Type in Abbreviation*: ")
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
  return t
print(time())
