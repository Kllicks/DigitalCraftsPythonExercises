#Given a height and width, input by the user, print a box consisting of * characters as its border

#user input
w = int(input("Width? "))
h = int(input("Height? "))

#initialize variable for while loop
counter_row = 0
while counter_row < h:
    counter_col = 0
    while counter_col < w:
        if counter_col == 0 or counter_col == w - 1 or counter_row == 0 or counter_row == h-1:
            print("*", end='')
        # moved to have only one print statement
        # elif counter_row == 0 or counter_row == h-1:
        #     print("*", end='')
        else:
            print(" ", end = '')
        counter_col = counter_col + 1
    counter_row = counter_row + 1
    print() 
