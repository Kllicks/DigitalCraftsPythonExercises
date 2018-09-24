#using while loop, print out the odd numbers 1-10 inclusive, one on a line

#initiate variable
i = 1

#while loop to cycle through and print 1-10
while i <= 10: 
    
    #if statement to check if the number is also odd
    #can't use and on outer while loop because it would end the program when 2 failed
    if i % 2 != 0:
        print(i, "")
    i += 1