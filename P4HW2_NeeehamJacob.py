#Jacob Needham
#06//2026
#P4HW2
# A program to 
# Asks the user employee name,
# Enter user pay rate and hours worked
# Calculate overpay and regular pay. Store these values in variables, at the end of the program you will display overtime total, regular pay total, gross pay total, and number of employees entered
# Ask user to enter another employee's name to calculate salary for or "Done" to terminate program. Note we are using sentinels here.
# When user chooses to stop entering employee information , display results as shown in image below.
# THE PROGRAM ONLY TERMINATES IF THE USER ENTERS "Done" for employee name.
# Working with loops

#request employee info name, hours worked, hourly pay rate
name = input("Enter employee name or 'Done' to finish: ")

#create accumulator variables for Gross pay reg pay and overtime pay with an employee count
gross_total = 0
reg_total = 0
ovrtm_total = 0 
employee_count = 0

#loop evaluter
while name != 'Done':
    #employee count
    employee_count += 1 #employee = employee + 1
    hrs = float(input("How many hours did " +name+ " work this week? "))
    rate = float(input("What is " +name+ "'s hourly pay rate? "))
    print()

    #evalute if the employee has worked overtime
    if hrs > 40:
        #calc the overtime
        ovrtm_hrs = hrs - 40
        #calc overtime pay
        ovrtm_pay = ovrtm_hrs * (rate * 1.5)
        #calc salary for regular hrs
        reg_pay = 40 * rate
        #calc gross pay
        gross = reg_pay + ovrtm_pay
    else:
        ovrtm_pay = 0 
        ovrtm_hrs = 0
        reg_pay = hrs * rate
        gross = reg_pay

    # add to accumulator total
    ovrtm_total += ovrtm_pay
    reg_total += reg_pay
    gross_total += gross
    


    #Display Gross pay and user info
    print("----------------------------------------------------------------------------")
    print("Employee Name:", name)
    print()
    print(f'{"Hours worked":<20}{"Pay Rate":<15}{"Overtime Pay":<15}{"Regular Pay":<15}{"Gross Pay":<15}')
    print("----------------------------------------------------------------------------")
    print(f'{hrs:<20.2f}{rate:<15.2f}{ovrtm_pay:<15.2f}{reg_pay:<15.2f}{gross:<15.2f}')
    print()




    name = input("Enter employee name or 'Done' to finish: ")

print("Total number of employees entered: ", employee_count)
print("Total amount paid for overtime: $", format(ovrtm_total, ',.2f'))
print("Total amount paid for regular hours: $", format(reg_total, '.2f'))
print("Total amount paid in gross: $", format(gross_total, '.2f'))




