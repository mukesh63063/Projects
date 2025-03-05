import pytest

test_data = [
    (1,2,3),
    (12,10,22),
    (22, 45, 67),
    (10, -5, 5)

]
@pytest.mark.parametrize('a,b,exp', test_data)
def test_addition(a,b,exp):
    assert a+b == exp