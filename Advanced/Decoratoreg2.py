def outer_fun(fun):
    def inner_fun(x,y):
        x=x+10
        y=y+10
        
        return fun(x,y)
        
        print("main function call")
    return inner_fun
    
def main_fun(x,y):
    return x+y
    
    
var1=outer_fun(main_fun)
var2=var1(5,6)
print(var2)