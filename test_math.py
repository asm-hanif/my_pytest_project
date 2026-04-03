import pytest
from my_math import add

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    
def test_add_fail():
    assert add(5, 5) == 10