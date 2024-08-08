class P1:
    def add(*n):
        sum=0
        for i in n:
            sum=sum+i
        return sum
obj=P1
print(obj.add(5))        
print(obj.add(5,12,34)) 

