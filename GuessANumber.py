import random

secret_number = random.randint(1,10)
print("I am thinking of a number between 1 and 10.")
guess = int(input("What's the number? "))

x = 0
while x < 5:
    if guess == secret_number:
        print("You win!")
        break
    elif guess != secret_number:
        if guess > secret_number:
            print("%d is too high" % (guess))
        else:
            print("%d is too low" % (guess))
        x += 1
