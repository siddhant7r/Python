class P:
    city="Bhopal"
    def display(self):
        print("This is from Display")
class C(P):
    def show(self):
        print("This is from Show")
        print("City=",P.city)
class C1(C):
    city1=P.city
    def show1(self):
        print(self.display())
        print(self.show())
    
obj=C1()
print(obj.city1)
obj.show1()
obj.show()
obj.display()
print(obj.city)