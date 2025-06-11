class Person():
  def _init_(self,name,age,gender):
    self.name=name
    self.age=age
    self.gender=gender

  def show_details(self):
    print("The name is {}, age is {} and gender is {} ".format(name,age,gender))


p1=Person("Navneet",18,"Male")
p1.show_details()
