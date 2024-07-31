class Student:
    school='SPS'
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
        Student.center_code=101
    def display(self):
        Student.grade='12th'
        print('Name=',self.name)
        print('Rollno=',self.roll)    
        print('School=',Student.school)    
        print('Center=',Student.center_code)    
        print('Grade=',Student.grade)
        print('City=',Student.city)
        print(id(Student.grade))

obj=Student("Siddhant",12)

Student.city="Bhopal"
Student.grade='13th'
print(id(Student.grade))
obj.display()
#print("School",Student.school)            