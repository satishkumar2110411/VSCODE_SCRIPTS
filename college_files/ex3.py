def leap_year(year):
    if year%100==0:
        if year%400==0:
            return(True)
        else:
            return(False)
    elif year%4==0:
        return(True)
    else:
        return(False)

def max_2(a,b):
    if a>b:
        return a
    elif b>a:
        return b
    else:
        return('Both are equal.')

def max_3(a,b,c):
    if a>=b and a>=c:
        return a
    elif b>=a and b>=c:
        return b
    elif c>=a and c>=b:
        return c

def grade(marks):
    if marks >= 75:
        return('A')
    elif 60<=marks<75:
        return('B')
    elif 40<=marks<60:
        return('C')
    else:
        return('F')
    
def simple_calc(a,op,b):
    if op =='+':
        return a+b
    elif op == '-':
        return a-b
    elif op == '*':
        return a*b
    elif op == '/':
        if b!=0:
            return a/b
        else:
            return('Cannot divide by 0')
    else:
        return('Invalid operator. Please try =,-,*,/ ')

def program():
    i=0
    while i==0:
        print('This program contains solutions to finding \n 1. Leap Years \n 2. max of 2 no.s \
        \n 3. max of 3 no.s \n 4. simple calculator \n 5.grade of the total mark')
        p_type = int(input('Enter the program you want to use: '))
        if p_type == 1:
            print('Leap year')
            year = int(input('Enter the year: '))
            result = leap_year(year)
            if result == True:
                print(f'{year} is a leap year.')
            else:
                print(f'{year} is not a leap year.')
        
        elif p_type == 2:
            print('Max of 2 numbers')
            num1 = float(input("Enter the first number: "))
            num2 = int(input('Enter the second number: '))
            print(f'Result of comparison: {max_2(num1,num2)}')
            
        elif p_type ==3:
            print('Max of 3 numbers')
            num1 = float(input("Enter the first number: "))
            num2 = int(input('Enter the second number: '))
            num3 = float(input('Enter the third number: '))
            print(f'Result of comparison: {max_3(num1,num2,num3)}')

        elif p_type == 4:
            print('Simple calculator')
            num1 = float(input('Enter a: '))
            num2 = float(input("Enter b: "))
            op = input('Enter the operation (=,-,/,*): ')
            result = simple_calc(num1,op,num2)
            print(f'Result = {result}')
        
        elif p_type == 5:
            print('Marks to grade conversion')
            marks = float(input("Enter student marks: "))
            print(f'Grade of student: {grade(marks)}')
        
        else:
            print('Invalid type of problem.')
        
        status = input('Do you want to continue? (y/n): ')
        if status == 'n':
            i = 1
        
if __name__ == '__main__':
    program()