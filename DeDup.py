# Given a list of numbers or strings
# Create a new list containing the same elements as the first list 
# Except with any duplicate values removed. 
# Print the list.

user_list = input("Please provide a list of numbers or strings: ")
user_list = user_list.replace(" ", "")
new_list = []

for i in user_list:
    if i not in new_list:
        new_list.append(i)
print(new_list)