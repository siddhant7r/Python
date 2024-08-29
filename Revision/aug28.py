''' WAP
        name=["ajay","aman","Aakash","Sonam"]
        st_marks=[25,36,42,51]
        address=["bhopal","ujjain","Ratlam","agra"]

'''

name=["ajay","aman","Aakash","Sonam","radha"]
st_marks=[25,36,56,51,56]
address=["bhopal","ujjain","Ratlam","agra","bhopal"]

# for i in st_marks:
mx=max(st_marks)
count=st_marks.count(mx)

index=-1
for i in range(count):
    index=st_marks.index(mx,index+1)
    print(index)
    print("student name",name[index])
    print("Student Address",address[index])
    print("Student Marks",st_marks[index])

        