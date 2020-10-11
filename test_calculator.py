from calculator import add, subtract
import pytest
def test_add():
    test1 = add(1, 3)
    assert(test1 == 4)

    test2 = add(5.125, 5)
    assert(test2 == 10.125)

def test_subtract():
    test3 = subtract(4, 1)
    assert(test3 == 3)

    test4 = subtract(2.5, 6.8)
    assert(test4 == -4.3)