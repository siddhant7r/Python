class Book:
    price=1000
    def details(self,author_name,author_city):
        print("Name= ",author_name)
        print("City= ",author_city)
        print("Price=",Book.price)
    @classmethod
    def update_price(cls,updated_price):
        cls.price=updated_price
obj=Book()
obj.details("Siddhant","Bhopal")
obj.update_price(1500)
obj.details("Siddhant","Bhopal")            