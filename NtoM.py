#using a while loop, print out the numbers from start to end each on own line

#prompt user for numbers to start and end 
a = int(input("Start from: "))
b = int(input("End on: "))

#while loop to print each int
while a <= b:
    print(a, "")
    a += 1