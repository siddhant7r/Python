class Student:
  
    def __init__(self):
        print(id(self))
    @staticmethod    
    def display():
        print("This is from Display")

obj=Student
print(id(obj))
obj1=Student()
print(id(obj1))            