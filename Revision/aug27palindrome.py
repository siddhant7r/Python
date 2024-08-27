#Wap to create a new list with the help of list
#lis such that it contain onlypalinfrome string
#which has a length more then 2


lis=['ababa','nitin','we','new','ww','a','aaaaa']
lis1=[]

for i in lis:
    if lis[i]==lis[i][::-1]:
        lis1.append(lis[i]) 