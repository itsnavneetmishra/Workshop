#Multi level
class Apple:
  def Sweet(self):
    print("Apple is sweet")
  def Sour(self):
    print("Apple is sour not")
#obj = Apple()
#obj.Sweet()
class Orange(Apple):
  def Sweet1(self):
    print("Apple is sweet of Orange Class")
  def Sour1(self):
    print("Apple is sour not")
#obj1 = Orange()
#obj1.Sweet()
class Lemon(Orange):
  def abc(self):
    print("Defalut");
obj2=Lemon()
obj2.Sweet()