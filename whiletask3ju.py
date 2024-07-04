i=6
sum=1
while i>=1:
    sum=sum*i
    if i>1:
        print(i,end="*")
        
    else:
        print(i,end="=")
    i=i-1
print(sum)    