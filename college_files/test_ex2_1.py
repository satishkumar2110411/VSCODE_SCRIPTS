from ex2_1 import *

def test_circle():
    assert(circle(3)==28.274333882308138)
    assert(circle(0)==0.0)

def test_square():
    assert(square(2)==4.0)
    assert(square(0)==0.0)

def test_rectangle():
    assert(rectangle(1,2)==2.0)

def test_triangle():
    assert(triangle(2,1)==1.0)
    
test_circle()
test_square()
test_rectangle()
test_triangle()