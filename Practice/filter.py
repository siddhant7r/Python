def evens(n):
    if n%2==0:
        print(n)

nums=[12,4,5,6,7,9,3,34]
#res=list(filter(evens,nums))
res=list(filter(lambda n : n%2==0, nums))

print(res)