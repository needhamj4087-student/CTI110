#Jacob Needham
#06/28/2026
#P3HW2_calc
# A program to Evaluate salaries and weather the employee has worked overtime (more than 40 hours). If yes, calculate the amount owed to employee for overtime hours

#request employee info name, hours worked, hourly pay rate
name = input("Enter employee name: ")

hrs = float(input("Enter the number of hours worked: "))

rate = float(input("Enter hourly pay rate: "))

#evalute if the employee has worked overtime
if hrs > 40:
    #calc the overtime
    ovrtm_hrs = hrs - 40

    #calc over pay
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


#Display Gross pay and user info
print("----------------------------------------------------------------------------")
print("Employee Name:", name)
print()
print(f'{"Hours worked":<20}{"Pay Rate":<15}{"Overtime Pay":<15}{"Regular Pay":<15}{"Gross Pay":<15}')
print("----------------------------------------------------------------------------")
print(f'{hrs:<20.2f}{rate:<15.2f}{ovrtm_pay:<15.2f}{reg_pay:<15.2f}{gross:<15.2f}')