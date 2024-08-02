class Student:
    city="Bhopal"
    def __init__(self,name,roll):
        self.name=name         #instance variable
        self.roll=roll         #instance variable                         
    def display(self):
        print("this is")   
    def show(self):
        print("Name=",self.name )
        print("Roll no=",self.roll)
        # self.display()       access instance method inside of the class
obj=Student("Sid",28)
obj.show()   
obj.display()          #access instance method outside of the class