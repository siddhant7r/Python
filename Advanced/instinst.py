class Student:
    def display(self,name,age):
        self.n1=name
        self.n2=age
    def show(self):
        print(self.n1,self.n2)    

obj1=Student()
obj1.display('Rahul',27)
obj1.show()
print(obj1.n1,obj1.n2)