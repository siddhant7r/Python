x=int(int(input("Enter any bumber")))

def fact(x):
    if x==0:
        return 1
    return x*fact(x-1)
res=fact(x)
print(res)