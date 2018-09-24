bill = float(input("Total Bill Amount: "))
service_level = input("Level of Service? ")
service_level = service_level.lower()
people = float(input("Split how many ways? "))

if service_level == "good":
    tip_percent = .20
elif service_level == "fair" :
    tip_percent = .15
elif service_level == "bad" :
    tip_percent = .10

tip_amount = tip_percent * bill
total = tip_amount + bill
split = total / people 
print("Tip amount: $%.2f \nTotal amount: $%.2f \nAmount per person: $%.2f" % (tip_amount, total, split))

#print("Tip amount: $%.2f " % (tip_amount))
#print("Total amount: $%.2f " % (total))
#print("Amount per person: $%.2f " % (split))