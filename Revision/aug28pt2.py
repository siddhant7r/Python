#WAP to create following list at run time and place them all in a single list


name=[]
age=[]
rollno=[]


x=int(input("Enter no of values you want to enter"))

for i in range(x):
    n1=input("Enter your name")
    n2=input("Enter your age")
    n3=input("Enter your roll no")
    name.append(n1)
    age.append(n2)
    rollno.append(n3)
print(name,age,rollno)
