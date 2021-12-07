class Human :
  def __init__(self, age, name) :
    self.age = age
    self.name = name
  def __eq__(self, other) :
    return self.age == other.age and self.name == other.name
  def __le__(self, other) :
    return self.age <= other.age
kim = Human(29,
"홍길동")
sang = Human(29,
"홍길동")
moon = Human(30,
"이순신")
print(kim<=sang)
print(kim<=moon)
