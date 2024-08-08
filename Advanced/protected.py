class P1:
    _name="Ronaldo"
    def display(self):
        print(P1._name)
class C1(P1):
    name=P1._name
    def show(self):
        print("Name= ",C1.name)
obj=C1()
obj.show()
print(obj._name)        
