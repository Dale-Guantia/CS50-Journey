from numb3rs import validate

def test_format():
    assert validate(r"0.0.0.0") == True
    assert validate(r"1.2.3.4") == True
    assert validate(r"1.2.3") == False
    assert validate(r"1.2") == False
    assert validate(r"1") == False
    assert validate(r"cat") == False

def test_range():
    assert validate(r"255.255.255.255") == True
    assert validate(r"500.255.255.255") == False
    assert validate(r"255.500.255.255") == False
    assert validate(r"255.255.500.255") == False
    assert validate(r"255.255.255.500") == False
