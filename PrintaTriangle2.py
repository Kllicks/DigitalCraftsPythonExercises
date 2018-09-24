
h = int(input("Print a triangle with given height: "))
i = 0
while i < h:
    print(" " * (h - i - 1) + "*" * (2 * i + 1))
    i += 1