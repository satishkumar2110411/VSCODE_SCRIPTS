from cmath import sqrt
print('This program will print the roots of a quadratic equation')
def roots(a,b,c):
    #discriminant
    d = b**2-4*a*c

    #roots
    r1 = (-b+sqrt(d))/(2*a)
    r2 = (-b-sqrt(d))/(2*a)
    return r1,r2

if __name__ == '__main__':
    #Coefficients
    a = float(input('Enter value of a: '))
    b = float(input('Enter value of b: '))
    c = float(input('Enter value of c: '))

    r1_r2 = roots(a,b,c)
    print(f"The roots are {r1_r2[0]} and {r1_r2[1]}")

