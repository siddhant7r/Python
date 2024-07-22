# f=open("new1.txt",'x')

#g=open("new1.txt","w")

# h=open("new2.txt","a")

# i=open("new2.txt",'r')
# print(i.read())


f=open("n1.txt",'x')

print(f.readable())
print(f.writable())
print(f.closed)

f.close()
print(f.closed)
print(f.writable())