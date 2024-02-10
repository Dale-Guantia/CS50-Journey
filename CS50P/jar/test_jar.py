from jar import Jar


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    jar = Jar(5)
    assert jar.capacity == 5


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(11)
    assert jar.size == 11
    jar.deposit(1)
    assert jar.size == 12


def test_withdraw():
    jar = Jar()
    jar.deposit(12)
    jar.withdraw(0)
    assert jar.size == 12
    jar.withdraw(5)
    assert jar.size == 7