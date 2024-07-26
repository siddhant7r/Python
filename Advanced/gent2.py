def gen(x,y):
    while x<=y:
        yield x
        x=x+1
var1=gen(1,10)
print("Hello")
print(next(var1))
print("Welcome")
print(next(var1))

for i in var1:
    print(i)