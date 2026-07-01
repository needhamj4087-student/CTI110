#Jacob Needham
#06/30/2026
#P4LAB2
#program that asks the user to enter an integer. Only if the integer is zero or higher, the program should display the multiplication table for that integer from 1 to 12
#
#



again = "yes"

while again != "no":

    #Ask user for input/integer
    num = int(input("Enter An Integer: "))
    print()

    #If greater then 0 and a positive integer it proceed
    #use a while loop and for loop for validation and continuation

    if num >= 0:
        #Display the multiplication tables for user input if validated
        #display multiplication table 1 to 12
        for item in range(1, 13):
            print(f"{num} * {item} = {num * item}")
    else:
        print("This program does not handle negative values.")
    print()    


#Ask user to run again if yes start over if no exit program
    again = input("Would you like to run the program again? ")
    print()

#loop break
print("Program is ending ....")






