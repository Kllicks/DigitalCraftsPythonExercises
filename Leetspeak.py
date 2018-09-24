# user = input("Please provide a string: ")
# response = user.upper()
# alpha = ["A", "E","G","I","O","S","T"]
# num = [4,3,6,1,0,5,7]

# counter = 0
# while counter < len(response):
#     leet_counter = 0
#     while leet_counter < len(alpha):
#         if response[counter] == alpha[leet_counter]:
#             print(num[leet_counter], end = "")
#         leet_counter += 1
#     counter += 1
# print()

# start with list********
# append to another list********

#try using list.replace(value1, value2)
#research trans and maketrans and dict

user = input("Please provide a string: ")
word = user.upper()

counter = 0
while counter < len(word):
    if word[counter] == "A":
        print(4, end = "")
    elif word[counter] == "E":
        print(3, end = "")
    elif word[counter] == "G":
        print(6, end = "")
    elif word[counter] == "I":
        print(1, end = "")
    elif word[counter] == "O":
        print(0, end = "")
    elif word[counter] == "S":
        print(5, end = "")
    elif word[counter] == "T":
        print(7, end = "")
    else:
        print(word[counter], end = "")
    counter += 1
print()


