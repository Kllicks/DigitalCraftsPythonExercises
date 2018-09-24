# Write a program that will prompt you for how many coins you want. 
# Initially you have no coins. 
# It will ask you if you want a coin? 
# If you type "yes", it will give you one coin, and print out the current tally. 
# If you type no, it will stop the program.

#initiate coins at 0 and print you have no coins
c = 0
print("You have %d coins." % (c))

#Ask the user if they want more coins
response = input("Do you want another? ")
response = response.lower()


# while response != "no":    
#     c += 1
#     print("You have %d coins" % (c))
#     response = input("Do you want another? ")
#     response = response.lower()
# print("Bye")

#while loop to ask if the user wants more coins
while response == "yes" or response == "no":
    if response == "yes":
        c += 1
        print("You have %d coins" % (c))
        response = input("Do you want another? ")
        response = response.lower()
    elif response == "no":
        print("Bye")
        break
