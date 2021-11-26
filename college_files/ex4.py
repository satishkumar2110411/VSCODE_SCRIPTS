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

