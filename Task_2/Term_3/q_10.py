# 10. Write a Program to accept a day of week(int) and display the weekday (e.g-day=4 Thursday) (use switch case)

day = int(input('Enter the day '))

if day == 1:
    print('Sunday')
elif(day == 2):
    print('Monday')
elif(day == 3):
    print('Tuesday')
elif(day == 4):
    print('Wensday')
elif (day == 5):
    print('Thursday')
elif( day == 6):
    print("Firday")
elif(day == 7):
    print('saturday')
else:
    print('enetr valid day number')