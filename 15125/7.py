def __add__(self, other):
    obj = a(self.width + other.width, self.height + other.height)
    return obj

r1 = Rectangle(10, 5)
r2 = Rectangle(20, 15)
r3 = r1 + r2  # __add__()가 호출됨