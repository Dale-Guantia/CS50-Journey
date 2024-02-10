from plates import is_valid

def test_first_two_letters():
    assert is_valid("CS") == True
    assert is_valid("C5") == False
    assert is_valid("5C") == False
    assert is_valid("50") == False

def test_max_and_min_length():
    assert is_valid("CS") == True
    assert is_valid("CS5000") == True
    assert is_valid("C") == False
    assert is_valid("CS50000") == False

def test_punctuation():
    assert is_valid("CS50") == True
    assert is_valid("CS 50") == False
    assert is_valid("CS.!50") == False

def test_numbers_in_middle():
    assert is_valid("CS50") == True
    assert is_valid("CS50A") == False

def test_number_zero():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False