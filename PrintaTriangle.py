#Print a triangle consisting of * characters

# for i in range (h):
#     print(" "*(h - i - 1) + "*" * (2 * i + 1))

h = 4
i = 0
while i < h:
    print(" " * (h - i - 1) + "*" * (2 * i + 1))
    i += 1