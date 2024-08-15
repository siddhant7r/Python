class A:
    def display(self):
        print("This is Class A")
class B(A):
    def display(self):
        print("This is Class B")
    def show(self):
        return super().display()
obj=B()
obj.display()
obj.show()       