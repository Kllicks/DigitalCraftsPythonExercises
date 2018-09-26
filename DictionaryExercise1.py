# Print Elizabeth's phone number.
# Add an entry to the dictionary: Kareem's number is 938-489-1234.
# Delete Alice's phone entry.
# Change Bob's phone number to '968-345-2345'.
# Print all the phone entries.

phonebook_dict = {
  'Alice': '703-493-1834',
  'Bob': '857-384-1234',
  'Elizabeth': '484-584-2923'
}

print(phonebook_dict['Elizabeth'])
# print(phonebook_dict)
phonebook_dict['Kareem'] = '968-345-2345'
# print(phonebook_dict)
del phonebook_dict['Alice']
# print(phonebook_dict)
phonebook_dict['Bob'] = '968-345-2345'
# print(phonebook_dict)

for person in phonebook_dict:
  print("%s: %s" % (person, phonebook_dict[person]))
# or
for person, phone in phonebook_dict.items():
  print("%s: %s" % (person, phone))