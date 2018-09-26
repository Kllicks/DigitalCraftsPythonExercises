# Write a letter_histogram program that asks the user for input, and prints a dictionary containing the tally of how many times each letter in the alphabet was used in the word.

user = input("Please enter a word: ")
user = user.lower()
user = user.replace(" ", "")
word_dict = {}

for i in user:
    keys = word_dict.keys()
    if i in keys:
        word_dict[i] += 1
    else:
        word_dict[i] = 1
        
print(word_dict)

# or
# 
# for letter in user:
#     if letter in word_dict:
#         word_dict[letter] += 1
#     else:
#         word_dict[letter] = 1
# print(word_dict)
# 
# or
# 
# for letter in user:    
#     word_dict[letter] = word_dict.get(letter, 0) + 1
# print(word_dict)
