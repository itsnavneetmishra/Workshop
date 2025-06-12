class Car():
 
    def __init__(self, model, color):
      
        self.model = model
        self.color = color

    def carmodel(self):
        print("started",self.model)

    def carcolor(self):
        print("stopped",self.color)


objj= Car(1993,"Pink")