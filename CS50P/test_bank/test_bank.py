from bank import value

def test_hello():
    assert value("Hello") == 0
    assert value("Hello Dale") == 0
    assert value("hElLo dAlE") == 0

def test_starts_h():
    assert value("Hey") == 20
    assert value("Hey Dale") == 20
    assert value("hEy dAlE") == 20


def test_without_h():
    assert value("What's up!") == 100
    assert value("What's up Dale!") == 100
    assert value("wHaT's Up dAlE!") == 100