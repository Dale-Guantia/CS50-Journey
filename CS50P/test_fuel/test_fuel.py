from fuel import convert, gauge
import pytest

def test_convert():
    assert convert("0/1") == 0
    assert convert("1/4") == 25
    assert convert("1/2") == 50
    assert convert("3/4") == 75
    assert convert("1/1") == 100

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(50) == "50%"

def test_ZeroDivisionError():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_ValueError():
    with pytest.raises(ValueError):
        convert("1.5/3")
        convert("three/four")