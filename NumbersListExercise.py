# The given list of numbers
num = [1,2,3,4,5,6,7,8, -1]

# print a sum of all numbers of a given list
print("Sum of list: %d" % (sum(num)))
# print the largest number from a given list
print("Largest number: %d" % (max(num)))
# print the smallest number from a given list
print("Smallest Number: %d" % (min(num)))

# print all the even numbers from a given list
print("List of even number: ", end = "")
for i in num:
    if i % 2 == 0:
        print("%d " % (i) , end = "")
print()

# print all the positive numbers from a given list
print("List of positive numbers: ", end = "")
for i in num:
    if i > 0:
        print("%d " % (i) , end = "")
print()

# create a new list and store all positive numbers from the original list in the new list
even_num = []
print("New list of positive number: ", end = "")
for i in num:
    if i > 0:
        even_num.append(i)
print(even_num)

# Given a list of numbers, and a single factor (also a number), 
# create a new list consisting of each of the numbers in the first list multiplied by the factor
factor = 2
mult_list = []
print("New list after being multiplied: ", end = "")
for i in num:
    mult_list.append(i * 2)
print(mult_list)

# Given two lists of numbers of the same length, 
# create a new list by multiplying the pairs of numbers in corresponding positions in the two lists
# num = [1,2,3,4,5,6,7,8, -1]
num2 = [4,5,6,7,8,9,-3,-6, 1]
mult_pair = []
print("New list after two lists being multiplied: ", end = "")
counter = 0
while counter < len(num):
    mult_pair.append(num[counter] * num2[counter])
    counter += 1
print(mult_pair)

# Given two two-dimensional lists of numbers of the size 2x2
# Calculate the result of adding the two matrices
matrix1 = [[1,3], [2,4]]
matrix2 = [[5,2], [1,0]]
new_matrix = []
print("The sum of two given matrices: ")
for i in range(len(matrix1)):
    for j in range(len(matrix1[i])):
        new_matrix.append(matrix1[i][j] + matrix2[i][j])
print(new_matrix)



