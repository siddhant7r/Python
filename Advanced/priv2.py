# class P1:
#     __name="Ronaldo"
#     def display(self):
#         print(P1.__name)
# class C1(P1):
#     name=P1.__name
#     def show(self):
#         print("Name= ",C1.name)
# obj=C1()
# obj.show()
# print(obj.__name)


class P1:
    __name="Ronaldo"
    def display(self):
        print(P1.__name)
obj=P1()
obj.display()        
