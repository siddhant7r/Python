def add():
    x=int(input("Enter 1st number"))
    y=int(input("Enter 2nd number"))
    sum=x+y
    print(sum)

def sub():
    x=int(input("Enter 1st number"))
    y=int(input("Enter 2nd number"))
    diff=x-y
    print(diff)

def mul():
    x=int(input("Enter 1st number"))
    y=int(input("Enter 2nd number"))
    multiply=x*y
    print(multiply)


def div():
    x=int(input("Enter 1st number"))
    y=int(input("Enter 2nd number"))
    divide=x/y
    print(divide)



print("Enter 1 for Addition")
print("Enter 2 for Substraction")
print("Enter 3 for Multiplication")
print("Enter 4 for Division")
choice=int(input("Enter your choice"))
if choice==1:
    add()
elif choice==2:
    sub()
elif choice==3:
    mul()
elif choice==4:
    div()
else:
    print("Wrong choice")        
