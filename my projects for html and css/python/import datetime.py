import datetime, time,os
today = datetime.date.today()
my_diary = [ ]

print(today)
dairy = input("WELCOME\nWHAT DO YOU WANT TO WRITE TODAY?")
my_diary.append(dairy)
view = input("do you want to view diary ?:")
if view == "yes":
    print(my_diary)

else:
    print("closed")

    