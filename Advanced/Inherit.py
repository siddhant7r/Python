class p1:
    def display(self):
        print("P1 class")
class c1(p1):
    def display(self):
        print("from c1")
obj=c1()
obj.display()
# obj.show()            