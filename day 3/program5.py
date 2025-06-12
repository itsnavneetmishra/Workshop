class Person:
    def __init__(self,name):
        self.name=name

    def __repr__(self):
        return f"Person({self.name})"
    
class Greeting:
    def generate_greetings(self,person):
        return f"Hello, {person.name}, !WELCOME!"
        

person=Person("Navneet Mishra")
greeting= Greeting()
message=greeting.generate_greetings(person)
print(message)
