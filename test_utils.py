import utils

def test_total():
    actual_value = utils.total(5, 11)
    expected_value = 16
    assert actual_value == expected_value
    
def test_multiply():
    actual_value = utils.multiply(5, 11)
    expected_value = 55
    assert actual_value == expected_value