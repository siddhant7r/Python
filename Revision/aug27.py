lis=["we","sid","shreya","rahul"]

# 
# s=str(lis)


# print(type(s))

# print(s[0])
# for i in range(0,len(lis)):
#     lis[i]=lis[i].capitalize
# print(lis)

for i in range(0,len(lis)):
    lis[i]=lis[i][0].upper() +lis[i][1:]
print(lis)    