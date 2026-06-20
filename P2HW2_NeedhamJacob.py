#Jacob Needham

#06/20/2026

#P2HW2

#Create and interpret Lists of input data

#User input grades for Module 1 thru 6 one by one
mod1 = float(input("Enter grade for Module 1: " 
))

mod2 = float(input("Enter grade for Module 2: " 
))

mod3 = float(input("Enter grade for Module 3: " 
))

mod4 = float(input("Enter grade for Module 4: " 
))

mod5 = float(input("Enter grade for Module 5: " 
))

mod6 = float(input("Enter grade for Module 6: " 
))

print()

#Create a list of all input grades
moduleGrades = []

#append user input to list
moduleGrades.append(mod1)
moduleGrades.append(mod2)
moduleGrades.append(mod3)
moduleGrades.append(mod4)
moduleGrades.append(mod5)
moduleGrades.append(mod6)

print(
    "----------Results----------"
)

#Display the Lowest Grade


print(
 f"{'Lowest Grade:':<20}{min(moduleGrades):.2f}"   
)

#Display the Highest Grade
print(
 f"{'Highest Grade:':<20}{max(moduleGrades):.2f}"   
)

#Display the Sum of module 1 thru 6
sum = mod1 + mod2 + mod3 + mod4 + mod5 + mod6

print(
    f"{'Sum of Grades:':<20}{sum:.2f}"
)


#Display GPA
Avg = sum/len(moduleGrades)
print(
    f"{'Average:':<20}{Avg:.2f}"
)
print(
    "---------------------------"
)