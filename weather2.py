import pywapi  #requires install -- see README
import time


MonthList = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
#used to pull name of month into speech string

DayList = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
#List of days to put into speech string

Time = time.time()
#Time as Epoch time

Real_Time = time.localtime(Time)
#convert Epoch Time to Time as a readable string

Hour = Real_Time[3]
#pull the hour
Minute = int(Real_Time[4])
#pull the minute


if Minute < 10:
    #if the hour is single digit, append a 0 to the front
    Minute = '0' + str(Minute)
    #convert to string
else:
    Minute = str(Minute)
    #convert to string

Day = DayList[int(Real_Time[6])]
#Pull the name of the day, as opposed to a number

Month = MonthList[(int(Real_Time[1]) -1)]
#pull the name of the month, adjusted because index starts at zero

Month_Day = int(Real_Time[2])
#Pull the numbered day of the month for use with the month.


if Hour <= 11:
    #if in the morning, greet appropriately
    Greet = 'Good Morning'
elif 12 <= Hour <=16:
    #If in the afternoon, greet as such
    Greet = 'Good Afternoon'
else:
    #like above, if in the evening, greet as so
    Greet = 'Good Evening'

if Hour > 12:
    #Indicator for morning or evening, adjusted for 12 hour time.
    #comment out or delete this entire if statement for 24 hour time.
    indicator = 'P.M.'
    Hour -= 12
else:
    indicator = "A.M."

#Create a neat time string
#minute was made string above.
Time = str(Hour) + ':' + Minute + ' ' + indicator

try:
    Location = pywapi.get_weather_from_google(48825)  #Can also use yahoo and NDAAP

    Temp = int(Location['current_conditions']['temp_f'])
    #Pull Temp as unicode, just the digit, from google variable

    Sky = Location['current_conditions']['condition'].lower()
    #Pull Sky conditions, i.e. partly cloudy, from google variable


except: #If no internet connection
    errorspeech = "however, I cannot obtain weather data for you."
    Speech = "%s Mr. Gardner. It is %s on %s, %s %d, %s"%(Greet, Time, Day, Month, Month_Day, errorspeech)
    #Creates the entire string to be spoken without internet

    
else:
    Speech = "%s Mr. Gardner. It is %s on %s, %s %d, and %d degrees \
with %s skies."%(Greet, Time, Day, Month, Month_Day, Temp, Sky)
    #Creates the entire string to be spoken if no error


fd = open('Login.txt', 'w') #open file Login.txt
fd.write(Speech)  #Write the speech variable to the file
fd.close()  #close the file
