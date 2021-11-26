def gcd(a,b):
    if a>1 and b>1:    
        if a>b:
            a,b=b,a
        divisor = 1
        for i in range(2,a+1):
            if a%i==0 and b%i==0:
                divisor = i
        else:
            return(divisor)
    elif a==1 or b==1:
        return(1)
    else:
        return('Invalid entries!')
    
def prime_number(num):
    if num<0:
        return('Invalid number')
    elif num == 1:
        return('Neither prime nor composite')
    elif num ==2:
        return('Prime number')
    else:
        limit = int(num**0.5) + 1
        for i in range(2,limit):
            if num%i==0:
                return('Not a prime number')
                break
        else:
            return('Prime number')

def integer_division():
    pass

def digit_sum(num):
    if num<0:
        num = -num
    sum_ = 0
    while num>9:
        sum_+=num%(10)
        num //= 10
    else:
        sum_+=num
    return(sum_)

def multiplication_table(x):
    for i in range(1,11):
        print(f'{x} * {i} = {x*i} \n')
    
def sum_of_series(series):
    sum_ = 0
    for i in series:
        sum_ += i
    else:
        return(sum_)

def newton_root(num,iteration):
    x = num
    for i in range(iteration):
        num = 0.5*(num + x/num)
    return(num)

def program():
    print('Enter the program you want to access: \
        \n 1. Greatest common divisor \n 2. Prime number \
        \n 3. Integer division \n 4. Sum of digits of a number \
        \n 5. Multiplication table \n 6. Sum of series \
        \n 7. Square root of a number using Newton\'s method')
    
    status = 0
    while status == 0:
        problem = int(input('Enter your choice: '))
        if problem == 1:
            print('Greatest common divisor')
            a = int(input('Enter the first number: '))
            b = int(input('Enter the second number: '))
            result = gcd(a,b)
            print(f'GCD = {result}')
    
        elif problem ==2:
            print('Prime number')
            num = int(input('Enter number to be checked: '))
            result = prime_number(num)
            print(result)
    
        elif problem == 3:
            pass

        elif problem == 4:
            print('Sum of digits of a number')
            num = int(input('Enter the number: '))
            print(f'The sum of the digits is {digit_sum(num)}')
    
        elif problem == 5:
            print('Multiplication table')
            x = int(input('Enter the table number: '))
            multiplication_table(x)
    
        elif problem == 6:
            print('Sum of series')
            n = int(input('Enter the number of values in the series: '))
            list_ =[]
            for i in range(n):
                value = float(input('Enter the number: '))
                list_ += [value,]
            else:
                print('The sum of the series is: ',sum_of_series(list_))
    
        elif problem == 7:
            print('Square root of a number using Newton\'s method')
            num = int(input('Enter the number: '))
            iteration_value = int(input('Enter the number of times newton\'s method must be applied: '))
            result = newton_root(num, iteration_value)
            print(f'Root of {num} = {result}')

        else:
            print('Invalid problem number')

        reply = input('Do you want to continue? (y/n): ')
        if reply == 'n':
            status = 1
        
    
if __name__ == '__main__':
    program()