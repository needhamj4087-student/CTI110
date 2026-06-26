#Jacob Needham
#06/26/2026
#P3HW1
#Troubleshooting a given program disired outcome being a grading program that takes numbers and assigns letter grades 

# I  put a comment here
# My Last Name is Needham


# This program takes a number grade, determines average and displays letter grade for average.

# Enter grades for six different modules

mod_1 = float(input('Enter grade for Module 1: '))

mod_2 = float(input('Enter grade for Module 2: '))

mod_3 = float(input('Enter grade for Module 3: '))

mod_4 = float(input('Enter grade for Module 4: '))

mod_5 = float(input('Enter grade for Module 5: '))

mod_6 = float(input('Enter grade for Module 6: '))

# add grades entered to a list

grades = []

grades.append(mod_1)
grades.append(mod_2)
grades.append(mod_3)
grades.append(mod_4)
grades.append(mod_5)
grades.append(mod_6)
# TO DO: determine lowest, highest , sum and average for grades

#print(grades)

low = min(grades)
high = max(grades)
sum = sum(grades)
avg = sum/len(grades)





print(
    "------------Results------------"
)

#Display the Lowest Grade


print(
 f"{'Lowest Grade:':<20}{low:.1f}"   
)

#Display the Highest Grade
print(
 f"{'Highest Grade:':<20}{high:.1f}"   
)


print(
    f"{'Sum of Grades:':<20}{sum:.1f}"
)


#Display GPA

print(
    f"{'Average:':<20}{avg:.2f}"
)
print(
    "-------------------------------"
)


# determine letter grade for average

if avg >= 90:
    print('Your Grade is: A')
elif avg >= 80:
    print('Your Grade is: B')
elif avg >= 70:
    print('Your Grade is: C')
elif avg >= 60:
    print('Your Grade is: D')
else:
    print('Your Grade is: F')





