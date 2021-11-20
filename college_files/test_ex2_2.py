from ex2_2 import *

def test_S_I():
    assert(S_I(1000,2,6)==120.0)
    assert(S_I(1200,6,1)==72.0)
    assert(S_I(10500,2.5,2.5)==656.25)

test_S_I()