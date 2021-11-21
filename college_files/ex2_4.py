print("Program to calculate the net salary of an employee")

def net_salary(B_salary,DA,HRA,pf,tax_percent,MI):
    gross_salary = B_salary + DA + HRA
    tax = (tax_percent*B_salary)/100 

    total_deductions = pf + tax + MI

    net_pay = gross_salary - total_deductions
    return(net_pay)

if __name__ == '__main__':
    B_salary = float(input('Enter the basic salary: '))

    #allowances
    DA = float(input('Enter the dearness allowness: ')) #Dearness allowance
    HRA = float(input('Enter the home rental allowness: ')) #Home rental allowance
    
    #deductions
    pf = float(input("Enter PF: "))
    tax_percent = float(input('Enter tax percentage: '))
    MI = float(input('Enter medical instrument deduction: ')) #Medical instruments

    print(f"Your net salary is Rs.\
    {net_salary(B_salary,DA,HRA,pf,tax_percent,MI)}")
