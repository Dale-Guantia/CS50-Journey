from project import result, add_rice, add_water, heat_and_time
from unittest.mock import patch
import pytest


@patch("project.input", return_value="R")
def test_add_rice(mock_input):
    assert add_rice(5) == "r5"
    assert add_rice(10) == "r10"


@patch("project.input", return_value="C")
def test_add_water(mock_input):
    assert add_water(5) == "c5"
    assert add_water(10) == "c10"


@patch("project.input", return_value = 15)
def test_heat_and_time(mock_input):
    assert heat_and_time("L") == ("low", 15)
    assert heat_and_time("M") == ("medium", 15)
    assert heat_and_time("H") == ("high", 15)


def test_exception():
    with pytest.raises(Exception):
        heat_and_time("L")
        heat_and_time("M")
        heat_and_time("H")


def test_high():
    assert result("high", 16) == "burnt rice"
    assert result("high", 14) == "burnt and raw rice"


def test_medium():
    assert result("medium", 16) == "burnt rice"
    assert result("medium", 14) == "slightly burnt and raw rice"


def test_low():
    assert result("low", 31) == "burnt rice"
    assert result("low", 16) == "slightly burnt rice"
    assert result("low", 14) == "raw rice"
