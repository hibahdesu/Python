#Date and Time
import datetime

print(datetime.datetime.now())

#The Year
print(datetime.datetime.now().year)

#The Month
print(datetime.datetime.now().month)

#The Day
print(datetime.datetime.now().day)

#The Hour
print(datetime.datetime.now().hour)

#The Minute
print(datetime.datetime.now().minute)

#The Second
print(datetime.datetime.now().second)

#The Time
print(datetime.datetime.now().time())

#Specific Time
print(datetime.datetime(1996, 9, 15))

#How much I have lived till now
birthdayTime = (datetime.datetime(1996, 9, 15))

print(birthdayTime.strftime('%a'))
print(birthdayTime.strftime('%A'))
print(birthdayTime.strftime('%b'))
print(birthdayTime.strftime('%B'))
print(birthdayTime.strftime('%d'))
print(birthdayTime.strftime('%D'))
print(birthdayTime.strftime('%H'))
print(birthdayTime.strftime(f'%d\%B\%Y'))

nowTime = datetime.datetime.now()

print(f'I have lived for about {nowTime - birthdayTime}')

print(f'I have lived for about {(nowTime - birthdayTime).days} Days till now')
