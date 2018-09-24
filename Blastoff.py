#program that counts down

import time

#numbers to start and end 
a = int(input("Where should we countdown from: "))
b = 0

#while loop that doesn't allow the user to go over 20
while a > 20:
    print("Please pick a number less than 20")
    a = int(input("Where should we countdown from: "))

#while loop to print each int
while a >= b:
    print(a, "")
    if a == 0:
        print("BLASTOFF!")
    a -= 1
    time.sleep(1)