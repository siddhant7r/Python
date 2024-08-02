# class Student:
#     def display():
#         print("Hello")
#     def show():
#         print("Welcome")
# obj=Student
# obj.display()     
# obj.show()     

class Student:
    @staticmethod
    def display():
        print("Hello")
    @staticmethod
    def show():
        print("Welcome")
obj=Student()
obj.display()     
obj.show()     


