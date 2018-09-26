# Given a histogram tally (one returned from either letter_histogram or word_summary), print the top 3 words or letters

# Check solutions for other ways to do this.
# Possibly find max and append to empty list instead of deleting highest value

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
print("The top three words are: ")
counter = 0
while counter < 3:
    maximum = max(word_dict, key = word_dict.get)
    print("%s: %d" % (maximum, word_dict[maximum]))
    del word_dict[maximum]
    counter += 1
