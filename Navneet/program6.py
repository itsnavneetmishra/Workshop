class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        
    @staticmethod
    def hello():
        print("hello")


    def get_avg(self):
        sum=0
        for _ in self.marks:
            sum+=_
        print("hi",self.name,"Your avg score is",sum/3)


s1=Student("Navneet",[99,98,97])
print(s1.name,s1.marks)
s1.name="Navneet Mishra"
s1.get_avg()

s1.hello()
