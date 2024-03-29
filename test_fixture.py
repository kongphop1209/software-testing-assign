import pytest

@pytest.fixture
def  input_val() :
    input = 27
    return input

def test_divide_by_three(input_val):
    assert input_val % 3 == 0
    
def test_divide_by_five(input_val):
    assert input_val % 5 == 0