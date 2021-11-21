from ex2_3 import *

def test_roots():
    assert(roots(1,2,1)==(-1.0,-1.0))
    assert(roots(1,1,1)==((-0.5+0.8660254037844386j),(-0.5-0.8660254037844386j)))
test_roots()
