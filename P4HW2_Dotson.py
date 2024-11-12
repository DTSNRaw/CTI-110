#Damian Dotson
#11/7/2024
#P4HW2
# calculate regular and overtime pay, given an amployees hours worked.

# This is the pesudocode
'''
Input: Get the name as the string 
Input: Get the hours worked as an integer
Input: Get the pay rate as a float.

Output: print the employee name

If hours worked is greater than 40
     Calculate any OT hours worked by (HoursWOrked - 40
     Calculate OT pay (OT hours * (Pay rate * 1.5)
     Calculate reg pay (40 * Reg pay rate)
     Calculate gross by adding OT pay and REG play
     Calculate gross pay is equal to regualar pay.
     
else (employee worked 40 less hours) 
    overtime hours = 0
    overtime pay = 0
    Calculate regualar apy by multiplying original hours worked by reg pay rate

    
Output:
Display total hours worked

display regualar pay rate

Display overtime hours worked

Display overtime pay (OT hours TIMES OT pay rate)

Display pay for regualar hours worked a reg pay rate

Display gross pay - both reg pay and ot pay
rrr

'''
#the real code


# Get employee details
employee_name = input("Enter Employee name or type 'DONE' to end program: ")
#increments
total_employees = 0
total_overtime = 0
total_reg_hours = 0
total_gross = 0

while employee_name.lower() != "done":
    total_employees += 1
    hours_worked = int(input("Enter number of hours worked: "))
    
    pay_rate = float(input("Enter your pay rate: "))
    # Declare variables

    regular_pay = 0
    overtime_hours = 0
    overtime_pay = 0
    gross_pay = 0

    # Calculate pay based on hours worked
    if hours_worked > 40:
        # Calculate overtime
        overtime_hours = hours_worked - 40
        overtime_pay = overtime_hours * (pay_rate * 1.5)
        regular_pay = 40 * pay_rate
        gross_pay = regular_pay + overtime_pay
    else:
        # No overtime
        regular_pay = hours_worked * pay_rate
        overtime_hours = 0
        overtime_pay = 0
        gross_pay = regular_pay
    total_overtime = total_overtime + overtime_pay
    total_reg_hours = total_reg_hours + regular_pay
    total_gross = total_gross + gross_pay

    # Display the yummy results
    print("=*" * 50)
    print(f"Employee name:     {employee_name}")
    print("====================================================================")
    print("_-" * 50)
    print(f"{'Hours worked':<15}{'Pay Rate':<12}{'Overtime Hours':<17}{'Overtime Pay':<15}{'Regular Pay':<15}{'Gross Pay':<15}")
    print(f"{hours_worked:<15}{pay_rate:<12.2f}{overtime_hours:<17}{overtime_pay:<15.2f}{regular_pay:<15.2f}{gross_pay:.2f}")
    print("=*" * 50)
    employee_name = input("Enter Employee name or type 'DONE' to end program: ")
    # Wanted to do a fun little bit after this, but it was messing with the code too much :(
print(f"Total number of employees entered: {total_employees}")
print(f"Total amount payed for overtime: ${total_overtime:.2f}")
print(f"Total amount payed for regular hours: ${total_reg_hours:.2f}")
print(f"EWWWWW, total gross pay: ${total_gross:.2f}")
print("Program has ended!" * 100)




























