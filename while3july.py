n=int(input("enter your number"))
i=1
# while i<=n:
     
#      print(i,end=',')
#      i=i+1
   

# while i<=n:
#     if i<=n-1:
#         print(i,end=",")
#     else:
#         print(i)
#     i=i+1       

sum=0
while i<=n:
    if i<=n-1:
        print(i,end=",")
        sum=sum+i
    else:
        print(i)
    i=i+1
print(sum)        