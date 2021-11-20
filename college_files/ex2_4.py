print("Program to calculate the net salary of an employee")

def net_salary():
    basic_salary = float(input('Enter the basic salary: '))

    #allowances
    dearness_allowance = float(input('Enter the dearness allowness: '))
    home_rental_allowance = float(input('Enter the home rental allowness: '))

    gross_salary = basic_salary + dearness_allowance + home_rental_allowance

    #deductions
    pf = float(input("Enter PF: "))
    tax_percent = float(input('Enter tax percentage: '))
    tax = (tax_percent*basic_salary)/100 
    medical_instruments = float(input('Enter medical instrument deduction: '))

    total_deductions = pf + tax + medical_instruments

    net_pay = gross_salary - total_deductions
    return(net_pay)

if __name__ == '__main__':
    print("Your net salary is Rs.",net_salary())
