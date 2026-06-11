#Jacob Needham
#06/10/2026
#P1HW1.py
#In tis program we will calculate exponenets and some other addition and subtraction functions

#Calculate Exponents

print(
    "--------Exponents--------"
)
print()

base = int(input("Enter a base number: "))
exponent = int(input("Enter an exponent: "))

result = base ** exponent

print(
    base, "raised to the power of", exponent, "is", result
)