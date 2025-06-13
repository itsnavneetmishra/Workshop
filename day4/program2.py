class ParentClass:

    def parent_method(self):
        print("This is a method from our parent class")

class ChildClass(ParentClass):

    def child_method(self):
        print("This is a method from child class" )


parent_obj=ParentClass()

child_obj=ChildClass()

parent_obj.parent_method()
child_obj.parent_method()

child_obj.child_method()


              