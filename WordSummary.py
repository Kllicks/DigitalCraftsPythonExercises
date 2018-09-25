# Write a word_histogram program that asks the user for a sentence as its input, and prints a dictionary containing the tally of how many times each word in the alphabet was used in the text

user = input("Please enter a sentence: ")
user = user.lower()
user = user.split(' ')
word_dict = {}

for i in user:
    keys = word_dict.keys()
    if i in keys:
        word_dict[i] += 1
    else:
        word_dict[i] = 1
        
print(word_dict)

