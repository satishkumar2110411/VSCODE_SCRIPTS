print('This program will print the roots of a quadratic equation')
def roots(a,b,c):
    #discriminant
    d = b**2-4*a*c

    #roots
    r1 = (-b+(d)**0.5)/(2*a)
    r2 = (-b-(d)**0.5)/(2*a)
    return(r1,r2)

if __name__ == '__main__':
    #Coefficients
    a = float(input('Enter value of a: '))
    b = float(input('Enter value of b: '))
    c = float(input('Enter value of c: '))

    roots(a,b,c)
    print(f"The roots are {r1} and {r2}")

