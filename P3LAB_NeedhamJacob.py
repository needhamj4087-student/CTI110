#Jacob Needham
#06/26/2026
#P3LAB
#Calculate the most efficient number of dollars, quarters, dimes, nickels, and pennies needed to make the given amount of money.
#learning to use if/else statements
#When dividing in python if you use // instead of / it ignores the decimel point and gives you a whole number


#variable Change creation 
#get value from user
change = float(input("Enter an amount of money: $"))
#print(f"Change Amount: {change}")


#convert float to integer for numerical accuracy
change = round(change * 100)

#print(f"Change Amount: {change}")

#Determine how many dollars and coins are needed
dollars = change // 100
change = change - (dollars * 100)

#print(f"${dollars}.{change}")

#variable quarters
quarters = change // 25
change = change - (quarters * 25)

#Dimes
dimes = change // 10
change = change - (dimes * 10)

#nickles
nickles = change // 5
change = change - (nickles * 5)

#pennies
pennies = change 


#numer of dollar change to give the user
if dollars > 0:
    if dollars == 1:
        print(
            f"{dollars} Dollar"
        )
    else:
        print(
            f"{dollars} Dollars"
        )

#number of quarter change for the user
if quarters > 0:
    if quarters == 1:
        print(
            f"{quarters} Quarter"
        )
    else:
        print(
            f"{quarters} Quarters"
        )

#numer of dime change
if dimes > 0:
    if dimes == 1:
        print(
            f"{dimes} Dime"
        )
    else:
        print(
            f"{dimes} Dimes"
        )

#number of nickle change
if nickles > 0:
    if nickles == 1:
        print(
            f"{nickles} Nickel"
        )
    else:
        print(
            f"{nickles} Nickels"
        )

#number of penny change to desplay to user
if pennies > 0:
    if pennies == 1:
        print(
            f"{pennies} Penny"
        )
    else:
        print(
            f"{pennies} Pennies"
        )

        


