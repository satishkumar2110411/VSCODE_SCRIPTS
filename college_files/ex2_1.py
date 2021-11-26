from math import pi
print("This program will find the area of geometric shapes")
def circle(radius):
    area = pi*radius**2
    return area
def square(side):
    area = side**2
    return area
def rectangle(length,breadth):
    area = length*breadth
    return area 
def triangle(base,height):
    area = 0.5*base*height
    return area

if __name__ == '__main__':
    print("Circle")
    radius = float(input("Enter circle radius: "))
    print(f'Area of circle = {circle(radius)}')

    print('Square')
    side = float(input('Enter side length: '))
    print(f'Area of square = {square(side)}')

    print('Rectangle')
    length = float(input('Enter length: '))
    breadth = float(input('Enter breadth: '))
    print(f'Area of rectangle = {rectangle(length,breadth)}')

    print('Triangle')
    base = float(input('Enter base length: '))
    height = float(input('Enter height: '))
    print(f'Area of triangle = {triangle(base,height)}')