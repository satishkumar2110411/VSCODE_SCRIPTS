from ex3 import *

def test_leap_year():
    assert(leap_year(1700)==False)
    assert(leap_year(2012)==True)

def test_max_2():
    assert(max_2(1.0,2.0)==2.0)
    assert(max_2(-0.4,0.4)==0.4)
    assert(max_2(10.0,10.0)==10.0)

def test_max_3():
    assert(max_3(1.0,2.0,3.0)==3.0)
    assert(max_3(1.0,1.0,0.5)==1.0)
    assert(max_3(2.0,2.0,2.0)==2.0)

def test_simple_calculator():
    assert(simple_calculator(1.0,'+',2.0)==3.0)
    assert(simple_calculator(2.0,'*', 0.0)==0.0)
    assert(simple_calculator(1.0,'/',0.0)=='Cannot divide by 0')

def test_grade():
    assert(grade(100.0)=='A1')
    assert(grade(50.0)=='C2')
    assert(grade(0.0)=='F')

test_leap_year()
test_max_2()
test_max_3()
test_simple_calculator()
test_grade()