n= int(input("ENter any number"))
count=0
p,m=n,n
sum=0
while n>0:
    n=n//10
    count=count+1
print("count=",count)

while m>0:
    digit=m%10
    sum=sum+digit**count
    m=m/10

if sum==p:
    print("It is an armstrong")

