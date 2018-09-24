#print a NxN square of * characters. Prompt user for N.

n = int(input("How big is the square? "))

counter_row = 0
while counter_row < n:
    counter_col = 0
    while counter_col < n:
        print("*", end='')
        counter_col = counter_col + 1
    counter_row = counter_row + 1
    print() 