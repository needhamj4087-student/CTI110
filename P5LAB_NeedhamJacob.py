#Jacob Needham
#07/15/2026
#P5Lab
#A Program to simulate a Customer using a self-checkout machine
#
import random 

def disperse_change(change) :
    
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

def main() :
    #logic goes in main
    # 
    #generate the amount of money owed

    amount_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"You owe: ${amount_owed:.2f}")

    #Create variable for the money payed by user
    money_in = float(input("How much Cash will you put in the self-checkout? "))

    #Calculate the change owed
    change = money_in - amount_owed

    print(f"Change owed: ${change:.2f}")
    print()

    #call diseperse change func
    disperse_change(change)




#Call the main function    
main() 
