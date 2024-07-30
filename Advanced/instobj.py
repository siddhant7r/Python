#instance variable declaration through object

class Student:
    # def __init__(self,name,age):
    #     self.n1=name
    #     self.n2=age
    def display(self):
        print("Name is ",self.n1)    
        print("Age is ",self.n2)

obj1=Student()
obj1.n1="Shreya"
obj1.n2=27
obj1.display()