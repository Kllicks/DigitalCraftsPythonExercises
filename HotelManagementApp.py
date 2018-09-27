# Display a menu asking whether to check in or check out.
# Prompt the user for a floor number, then a room number.
# If checking in, ask for the number of occupants and what their names are.
# If checking out, remove the occupants from that room.
# Do not allow anyone to check into a room that is already occupied.
# Do not allow checking out of a room that isn't occupied.

hotel = {
  '1': {
    '101': ['George Jefferson', 'Wheezy Jefferson'],
  },
  '2': {
    '237': ['Jack Torrance', 'Wendy Torrance'],
  },
  '3': {
    '333': ['Neo', 'Trinity', 'Morpheus']
  }
}

# for floor in hotel:
#     for room in hotel[floor]:
#         print("floor:%s room:%s" % (floor,room))
#         for occupants in hotel[floor][room]:
#             print("\t\t" + occupants)
# print()

check = input("Would you like to check in or out? ")
check = check.lower()

if check == "in":
    floor = input("What floor would you like to be on? ")
    room = input("What room would you like? ")
    occupants = input("How many occupants are their? ")
    
    for floor in hotel:
      for room in hotel[floor]:
        for occupants in hotel[floor][room]:
          

    

    counter = 1
    while counter < int(occupants) + 1:
        name = input("Name of occupant %d: " % (counter))
        counter += 1
print(hotel)
# elif check == "out":
#     print("So you're checking out")