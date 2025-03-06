def test_add():
    assert 1+1 == 2

def squqre(a):
    return a**2

s = [10,20,30]
result = list(map(squqre, s))

def test_check():
    assert result == [100,400,900]


