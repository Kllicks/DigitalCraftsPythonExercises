day = int(input("Day (0-6)? " ))

if day >= 0 and day <= 6:
    if day in range (1,6):
        print("Go to work")
    else:
        print("Sleep in")
else:
    print("Please pick from 0-6")

#week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

# if day == 0:
#     print(week[0])
# elif day == 1:
#     print(week[1])
# elif day == 2:
#     print(week[2])
# elif day == 3:
#     print(week[3])
# elif day == 4:
#     print(week[4])
# elif day == 5:
#     print(week5])
# elif day == 6:
#     print(week[6])
# else:
#     print("That's not (0-6)")