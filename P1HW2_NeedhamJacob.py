#Jacob Needham
#06/10/2026
#P1HW2.py
#Program to determine travel expenses


#Title statement
print(
    "This Program calculates and dislayes travel expenses"
)

print()


#Ask user for inicial budget
budget = int(input(
    "Enter your Budget: "
))
print()


#Ask the User where they are going
dest = input(
    "Now Enter your destination: "
)
print()


#prompt user to input projected Gas expense
gas = int(input(
    "How much do you think you will spend on gas? "
))
print()


#Prompt User to Aproximate their hotel cost
hotel = int(input(
    "Aproximately, how much will you need for accomodations/hotel? "
))
print()


#Ask User for their food cost projection
food = int(input(
    "Lastly, how much do you need for food cost? "
))

print()


#summary title
print(
    "------- Travel Expenses --------"
)
 #users input for destination
print(
   "Location:",dest
)


#users input for budget
print(
   "Initial Budget:",budget
)

print()


#users input for gas cost
print(
"Fuel: ", gas
)

#users input for hotel stay price
print(
    "Accomodation: ", hotel  
)

#users input for food cost
print(
    "Food: ",food
)

print()


#Calculating total cost and remaining funds
cost = gas + hotel + food

remaining = budget - cost

#Dislay users remaining budget
print(
    "Remaining Balance: ",remaining
)