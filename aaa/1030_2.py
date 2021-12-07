class Add :
  def add(self, a, b) :
    return a+b
class Multiply :
  def multiply(self, a, b) :
    return a*b
class Sub:
  def sub(self, a, b) :
    return a-b
class Div:
  def div(self, a, b):
    return a/b
class Calculator(Add, Multiply, Div, Sub):
  pass #☞ 클래스 Add, Multiply로부터 다중 상속
 

c = Calculator()
print(c.add(1,2))
print(c.multiply(2,10))
print(c.sub(2,10))
print(c.div(10,2))