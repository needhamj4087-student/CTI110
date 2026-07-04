#Jacob Needham
#06//2026
#P4HW1
#A Program to 
#Ask user to enter for number of scores they would like to enter. (10 points)
#Create a loop to collect the number of scores the user wants to enter. (25 points)
#Note every time a score is entered, the following should be done
#Evaluate if the score is valid, it should be between 0 and 100 . 
#If it is not, notify the user and ask for a VALID score to be entered. (20 points)
#Hint - you will need to use more than one loop in this program
#
#
#Create and interpret Lists of input data, module grades.

#User input grades for Module 1 thru 6 one by one
scores = int(input(
    "How Many Scores do you wish to enter? "
))
#list for user scores
userScores = []
print()

#loop to collect the users scores
for num in range(1, scores + 1):
    while True:
        score = int(input(f"Enter Score #{num}: "))
        if 0 <= score <= 100:
            userScores.append(score)
            break
        else:
            print()
            print("INVALID Score entered!!!")
            print("Score should be between 0 and 100")
            print(f"Enter score #{num} again: ")
            

print()

print(
    "----------Results----------"
)

#Display the Lowest Grade


print(
 f"{'Lowest Score':<20}:{min(userScores):.1f}"   
)

# Remove the lowest Score from the list then display it
userScores.remove(min(userScores))

print(
    f"{'Modified List':<20}:{userScores}"
)






#Display GPA
Avg = sum(userScores) / len(userScores)
print(
    f"{'Scores Average:':<20}:{Avg:.2f}"
)

# find the letter grade
if Avg >= 90:
    letter_grade = 'A'
elif Avg >= 80:
    letter_grade = 'B'
elif Avg >= 70:
    letter_grade = 'C'
elif Avg >= 60:
    letter_grade = 'D'
else:
    letter_grade = 'F'

print(f"{'Grade':<20}:{letter_grade}")

    
print(
    "---------------------------"
)




