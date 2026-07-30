class Temperatura:
    def __init__(self, daraja, birlik):
        self.daraja = daraja
        self.birlik = birlik

    def __str__(self):
        return f"{self.daraja}°{self.birlik}"

    def __repr__(self):
        return f"Temperatura({self.daraja}, '{self.birlik}')"

    
    def __eq__(self, other):
        if not isinstance(other, Temperatura):
            return NotImplemented
        return self.daraja == other.daraja

    def __lt__(self, other):
        if not isinstance(other, Temperatura):
            return NotImplemented
        return self.daraja < other.daraja

    def __le__(self, other):
        if not isinstance(other, Temperatura):
            return NotImplemented
        return self.daraja <= other.daraja

    def __gt__(self, other):
        if not isinstance(other, Temperatura):
            return NotImplemented
        return self.daraja > other.daraja

    def __ge__(self, other):
        if not isinstance(other, Temperatura):
            return NotImplemented
        return self.daraja >= other.daraja


t1 = Temperatura(36.6, "C")
t2 = Temperatura(40, "C")
t3 = Temperatura(36.6, "F")

print(t1)
print(repr(t1))

print(t1 == t2)
print(t1 == t3)

print(t1 < t2)
print(t1 <= t2)

print(t2 > t1)
print(t2 >= t1)