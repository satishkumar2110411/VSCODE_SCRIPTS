def leap_year(year):
    if year%100==0:
        if year%400 == 0:
            return(True)
        else:
            return(False)
    elif year%4==0:
        return(True)
    else:
        return(False)

def max_2(a,b):
    if a>b:
        return(a)
    elif b>a:
        return(b)
    else:
        return('Both are Equal')

def max_3(a,b,c):
    if a>=b and a>=c:
        return a
    elif b>=a and b>=c:
        return b
    elif c>=a and c>=b:
        return c

def simple_calculator(a,op,b):
    if op == '+':
        return a+b
    elif op =='-':
        return a-b
    elif op == '*':
        return a*b
    elif op == '/':
        if b !=0.0:
            return a//b
        else:
            return('Cannot divide by 0')
        
    elif op == '**':
        return a**b

def grade(t_marks):
    if 91<=t_marks<=100:
        return 'A1'
    elif 81<=t_marks<=90:
        return 'A2'
    elif 71<=t_marks<=80:
        return 'B1'
    elif 61<=t_marks<=70:
        return 'B2'
    elif 51<=t_marks<=60:
        return 'C1'
    elif 41<=t_marks<=50:
        return 'C2'
    else:
        return 'F'

print('This program contains solutions to finding \n 1. Leap Years \n 2. max of 2 no.s \
    \n 3. max of 3 no.s \n 4. simple calculator \n 5.grade of the total mark')

i = 0
while i == 0:
    p_type = int(input('Enter the program you want to use: '))
    
    if p_type == 1:
        year = int(input('Enter the year: '))
        result = leap_year(year)
        if result == False:
            print(f'{year} is not a leap year')
        else:
            print(f'{year} is a leap year')

    elif p_type == 2:
        x = float(input('Enter the first number: '))
        y = float(input('Enter the second number: '))
        print(f'Result: {max_2(x,y)}')
    
    elif p_type == 3:
        x = float(input('Enter the first number: '))
        y = float(input('Enter the second number: '))
        z = float(input('Enter the third number: '))
        print(f'Result: {max_3(x,y,z)}')
    
    elif p_type == 4:
        x = float(input('Enter the first number: '))
        y = float(input('Enter the second number: '))
        op = input('Enter your operation(+,-,*,/,**): ')
        print(f'Result: {simple_calculator(x,op,y)}')
    
    elif p_type == 5:
        marks = float(input('Enter your total marks: '))
        print(f'Your Grade: {grade(marks)}')
    
    else:
        print('Type in a valid number')
    
    status = input('Do you want to continue? (y/n): ')
    if status != 'y':
        i = 1