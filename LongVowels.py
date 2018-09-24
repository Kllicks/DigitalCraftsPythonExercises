#given a string, print vowels 5 times

#response = input("Please provide a string: ")
# response = response.lower()
# vowels = ["a", "e", "i", "o", "u"]

# for i in response:
#     for x in vowels:
#         if i == x:
#             print(i * 4, end = "")
#     print(i, end = "")
# print()


#---------------------------------------------


response = input("Please provide a string: ")
response = response.lower()
vowels = ["a", "e", "i", "o", "u"]

count = 0 
while count < len(response):
    vowel_count = 0
    while vowel_count < len(vowels):
        if response[count] == vowels[vowel_count]:
            print(response[count] * 4, end = "")
        vowel_count += 1
    print(response[count], end = "")
    count += 1    
print()


#------------------------------------------


# response = input('Provide a string: ')
#
# vowels = ['a', 'e', 'i', 'o', 'u']
# count = 0 
#
# while count < len(response):
#     if response[count] == vowels[0]:
#         print(response[count] * 5, end = '')
#     elif response[count] == vowels[1]: 
#         print(response[count] * 5, end = '')
#     elif response[count] == vowels[2]: 
#         print(response[count] * 5, end = '')
#     elif response[count] == vowels[3]: 
#         print(response[count] * 5, end = '')
#     elif response[count] == vowels[4]: 
#         print(response[count] * 5, end = '')
#     else:
#         print(response[count], end = '')
#     count += 1    
# print()