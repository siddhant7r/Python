def fun1(x):
    def fun2(y):
       return x+y
    return fun2
	    
var1=fun1(5)
var2=var1(10)
print(var2)