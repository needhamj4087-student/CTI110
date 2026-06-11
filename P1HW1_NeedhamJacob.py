#Jacob Needham
#06/10/2026
#P1HW1.py
#In tis program we will calculate exponenets and some other addition and subtraction functions

#Calculate Exponents

print(
    "--------Calculating Exponents--------"
)
print()

base = int(input("Enter an integer as the base value: "))
exponent = int(input("Enter an integer as the exponent: "))

result = base ** exponent

print()

print(
    base, "raised to the power of", exponent, "is", result, "!!"
)
print()


#Calculating Addition and Subtraction



print(
    "--------Addition and Subtraction--------"
)
print()

num1 = int(input("enter you starting integer: "))
num2 = int(input("enter an integer to add: "))
num3 = int(input("enter an integer to be subtracted: "))

sum_result = num1 + num2
final_result = sum_result - num3

print()

print(
    num1, "+", num2, "-", num3, "is equal to", final_result,
)