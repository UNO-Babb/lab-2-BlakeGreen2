#FutureTime.py
#Name: Blake Green
#Date: 9/1/2025
#Assignment: Future Time

# datetime will allow us to access the system date and time.
import datetime

def main():
  #getting current time from system, storing to variable
  now = datetime.datetime.now()
  currentHour = now.hour + 7
  currentMinute = now.minute

 #this is just for checking, we should delete it later

  #TODO:
  #Ask user for hours
  Hours = int(input("Enter an amount of hours: "))
  #Ask user for minute
  Mins = int(input("Enter an amount of minutes: "))
  #Calculate the time after the user-supplied time has passed.
  futurehours = currentHour + Hours
  futuremins = currentMinute + Mins
  futurehours += futuremins // 60
  futuremins = futuremins % 60
  #Do not use any if statements in calculating the time.
  print("If you add those hours and minutes, the future time will be: " + str(futurehours) + ":" + str(futuremins))
  #Output the future time in standard format "HH:MM"


if __name__ == '__main__':
  main()
