class P:
    city="Bhopal"
    def display(self):
        print("This is from Display")
class C(P):
    def show(self):
        print("This is from Show")
        print("City=",P.city) 
obj=C()
obj.show()
print(obj.city,obj.display())               