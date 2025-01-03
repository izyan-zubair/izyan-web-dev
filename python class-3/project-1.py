age = 18
if age >= 18:
    print("you can vote")

number = 10
if number * 2 == 20:
    print("true")
else:
    print("false")

mark = 80
if mark >= 80:
    print("A grade")
elif mark >= 70:
    print("B grade")
elif mark >= 60:
    print("C grade")
elif mark >= 50:
    print("D grade")
else:
    print("E grade")

number = 10
if number > 0:
    if number % 2 == 0:
        print("positive number")
    else:
        print("negative number")
else:
    print("odd")

currentTime = datetime.datetime.now()
print("Current Date and time:", currentTime)

print("Year:",currentTime.year)
print("Month:",currentTime.month)
print("Day:",currentTime.day)
print("Hour:",currentTime.hour)
print("Minute:",currentTime.minute)
print("Second:",currentTime.second)

formatted_Time = currentTime.strftime("%d-%m-%Y %H:%M:%S")
print("formatted Date and time:", formatted_Time)     