record=int(input("How many records you want"))
st_detail=[[],[],[]]
for i in range(record):
    name=input("Enter your name")
    address=input("enter your address")
    marks=input("enter your marks")
    st_detail[0].append(name)
    st_detail[1].append(address)
    st_detail[2].append(marks)
print(st_detail)    