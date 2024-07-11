def ope (x,y):
    return x+y,x-y,x*y,x/y

p=int(input("Enter first no"))
q=int(input("Enter first no"))

a,b,c,d=ope(p,q)
print(a,b,c,d)