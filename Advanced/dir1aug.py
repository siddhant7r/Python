class Student:
    x=10
    y=10

    def display(x,y):
        print("Hello")
    def show():
        print("Welcoe")
# print(dir(Student))            
# print(__dict__(Student))
obj=Student
obj.display(10,20)
print(Student.__dict__)