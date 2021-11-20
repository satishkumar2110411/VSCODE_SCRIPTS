from math import pi
print("This program will find the area of geometric shapes")

def circle(radius):
    area = pi*radius**2
    return(area)
        
def square(side):
    area = side**2
    return(area)

def rectangle(length,breadth):
    area = length*breadth
    return(area)

def triangle(base,height):
    area = 0.5*base*height
    return(area)

if __name__ == '__main__':
    print('Circle')
    radius = float(input('Enter radius of the circle: '))
    print(f"The area of the circle is {circle(radius)} units squared.")
    
    print('Square')
    side = float(input('Enter side length of square: '))
    print(f"The area of the circle is {square(side)} units squared.")
    
    print('rectangle')
    length = float(input("Enter length of rectangle: "))
    breadth = float(input("Enter breadth of rectangle: "))
    print(f"The area of the circle is {rectangle(length,breadth)} units squared.")
    
    print("Triangle")
    base = float(input('Enter base length: '))
    height = float(input('Enter triangle height: '))
    print(f"The area of the circle is {triangle(base,height)} units squared.")
