def test_uppercase():
    assert "python".upper() == "PYTHON"
    
def test_reverse():
    assert list(reversed([100, 200, 300 , 400, 500])) == [500, 400, 300, 200, 100]
    
def test_some_primes():
    assert 41 in  {
        num
        for num in range(2, 50)
        if not any(num % div == 0 for div in range(2, num))
    }