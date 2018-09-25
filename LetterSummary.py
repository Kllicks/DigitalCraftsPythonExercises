# Write a letter_histogram program that asks the user for input, and prints a dictionary containing the tally of how many times each letter in the alphabet was used in the word.

user = input("Please enter a word: ")
user = user.replace(" ", "")
word_dict = {}

for i in user:
    keys = word_dict.keys()
    if i in keys:
        word_dict[i] += 1
    else:
        word_dict[i] = 1
        
print(word_dict)

