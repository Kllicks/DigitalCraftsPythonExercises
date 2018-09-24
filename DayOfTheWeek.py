day = int(input("Day (0-6)? " ))

week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

if day >= 0 and day <= 6:
    print (week[day])
else:
    print("Please pick from 0-6")

# if day == 0:
#     print("Sunday")
# elif day == 1:
#     print("Monday")
# elif day == 2:
#     print("Tuesday")
# elif day == 3:
#     print("Wednesday")
# elif day == 4:
#     print("Thursday")
# elif day == 5:
#     print("Friday")
# elif day == 6:
#     print("Saturday")
# else:
#     print("That's not (0-6)")