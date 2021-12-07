class Calc :
  def __init__(self,a,b) :
    self.a=a
    self.b=b
    return print(self.a,self.b)
  def __call__(self,a,b) :
    self.a=a
    self.b=b
    return print(self.a + self.b)
    
s = Calc(1,2)
s(7,8)
