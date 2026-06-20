#Jacob Needham
#06/20/2026
#P2HW1.py
# a clean up of a Program to determine travel expenses


#Title statement
print(
    "This Program calculates and dislayes travel expenses"
)

print()


#Ask user for inicial budget
budget = float(input(
    "Enter your Budget: "
))
print()


#Ask the User where they are going
dest = input(
    "Now Enter your destination: "
)
print()


#prompt user to input projected Gas expense
gas = float(input(
    "How much do you think you will spend on gas? "
))
print()


#Prompt User to Aproximate their hotel cost
hotel = float(input(
    "Aproximately, how much will you need for accomodations/hotel? "
))
print()


#Ask User for their food cost projection
food = float(input(
    "Lastly, how much do you need for food cost? "
))

print()


#summary title
print(
    "--------- Travel Expenses ----------"
)
 #users input for destination
print(
   f"{'Location:':<20}{dest:<30}"
)


#users input for budget
print(
   f"{'Initial Budget:':<20}${budget:<30.2f}"
)


#users input for gas cost
print(
   f"{'Fuel:':<20}${gas:<30.2f}"
)

#users input for hotel stay price
print(
    f"{'Accomodation:':<20}${hotel:<30.2f}" 
)

#users input for food cost
print(
    f"{'Food:':<20}${food:<30.2f}"
)


#Calculating total cost and remaining funds
cost = gas + hotel + food

remaining = budget - cost

print(
    "------------------------------------"
)
print()

#Dislay users remaining budget
print(
    f"{'Remaining Balance:':<20}${remaining:<30.2f}"
)