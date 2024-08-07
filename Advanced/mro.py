class A:
    def display(self):
        print("This is class A")
class B:
    def display(self):
        print("This is class B")
class C(A,B):
    def show(self):
        self.display()
obj=C()
obj.display()        
obj.display()        
