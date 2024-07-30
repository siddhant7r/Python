#constructor

class Student:
    def __init__(self,name,age):
        self.n1=name
        self.n2=age
    def display(self):
        print("Name is ",self.n1)    
        print("Age is ",self.n2)

obj1=Student('Siddhant',28)
obj1.display()
obj2=Student('Rahul',27)
obj2.display()

