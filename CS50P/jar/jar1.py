class Jar:
    def __init__(self, size = 0, capacity=12):
        self.capacity = capacity
        self.size = size

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        self.size += n

    def withdraw(self, n):
        self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size > self.capacity:
            raise ValueError("Cookie jar capacity exceeded")
        if size < 0:
            raise ValueError("Not enough cookies in the jar")
        self._size = size

jar = Jar(5)
jar.deposit(4)
jar.withdraw(5)
print(jar)
