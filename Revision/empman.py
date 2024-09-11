import sqlite3

def insert_data(d):
    n=int(input("how many ??"))
    for i in range(n): 
        eid=int(input("enter id:"))   #checkid(eid)
        ename=input("enter name;")
        des=input("enter designation;")
        gen=input("enter gender:")
        salary=int(input("enter salary:"))
        d[eid]=[ename,des,gen,salary]
    print(n,"record inserted ")
    return d


def search(d):
    name=input("whom do u want to search ,enter his/her name??")
    if any(d):
         flag=0
         for i,j in d.items(): # i=key ,j =value
             if j[0]==name: 
                flag+=1
                print("EID",i)
                print("Ename:",j[0])
                print("Des:",j[1])
                print("Gender:",j[2])
                print("Salary:",j[3])
         if flag==0:
            print("record not found")
         else:
             print(flag,"record found ")
    else:
        print("nothing to display")







def display(d):
    if any(d):
         for i,j in d.items(): # i=key ,j =value
           print("EID",i)
           print("Ename:",j[0])
           print("Des:",j[1])
           print("Gender:",j[2])
           print("Salary:",j[3])
    else:
        print("nothing to display")
        
def master(d):
  while True:
    print("-"*30,"EMS","-"*30)
    print("1 for insert data")
    print("2 for display data")
    print("3 for search by name")
    print("4 for search by id")
    print("5 for search by gender")
    print("10 for exit")
    choice=int(input("\n\nEnter choice:"))
    if choice==1:
        d=insert_data(d)
    elif choice==2:
        display(d)
    elif choice==3:
        search(d)
    if choice==10:
        print("Thank u.......")
        break
    



d={}
master(d)
