#print a 5x5 square of * characters

counter_row = 0
while counter_row < 5:
    counter_col = 0
    while counter_col < 5:
        print("*", end='')
        counter_col = counter_col + 1
    counter_row = counter_row + 1
    print() 