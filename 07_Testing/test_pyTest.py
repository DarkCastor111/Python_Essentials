def inc(x):
    return x + 1


def test_first():
    assert inc(3) == 5

def test_IgNoIg():
    assert 5 == 5
    assert 5 == 3

def test_Type():
    assert type(5) is int # Success Example
    assert type(5) is not int # Fail Example

def test_IsBooleano():
    verdad = 5==5
    assert verdad is True # Success Example
    assert verdad is False # Fail Example

def test_InNotIn():
    list_one=[1,3,5,6]
    assert 5 in list_one # Success Example
    assert 5 not in list_one # Fail Example

def test_MayorMenor():
    assert 5 > 4 # Success Example
    assert 5 > 7 # Fail Example

def test_Modulo():
    assert 2 % 2 == 0 # Success Example
    assert 2 % 2 == 1 # Fail Example

example = [5,3,1,6,6]
booleans = [False, False,True, False]
faux = [False, False, False]

def test_Any():
    
    assert any(example) # Success Example
    assert any(faux) # Success Example

def test_All():
    assert all(example)
    assert all(faux)
    assert all(booleans)