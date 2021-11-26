from ex4 import *

def test_gcd():
    assert(gcd(1,1)==1)
    assert(gcd(9,3)==3)
    assert(gcd(72,12)==12)
    assert(gcd(357,70)==7)

def test_prime_number():
    assert(prime_number(1)=='Neither prime nor composite')
    assert(prime_number(2)=='Prime number')
    assert(prime_number(49)=='Not a prime number')
    assert(prime_number(7)=='Prime number')
    assert(prime_number(92)=='Not a prime number')

def test_digit_sum():
    assert(digit_sum(104)==5)
    assert(digit_sum(123456789)==45)
    assert(digit_sum(10244098)==28)

def test_sum_of_series():
    assert(sum_of_series([1,2,3,4,5,6,7,8,9])==45)
    assert(sum_of_series((2,4,6,8))==20)
    assert(sum_of_series((9,4,5,6,2,8))==34)

def test_newton_root():
    assert(newton_root(4,100)==2)
    assert(newton_root(144,100)==12)

test_prime_number()
test_sum_of_series()
test_digit_sum()
test_gcd()
test_newton_root()