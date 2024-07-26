def gen():
    i=1
    my_list=[]
    while i<10:
        my_list.append(i)
        i=i+1
    return my_list
var1=gen()
print(var1)
    

# def gen():
#     i=1
#     my_list=[]
#     while i<10:
#         my_list.append(i)
#         i=i+1
#     yield my_list
# var1=gen()
# print(next(var1))    


# 1	def gen():
# 2	    i=1
# 3	    my_list=[]
# 4	    while i<10:
# 5	        my_list.append(i)
# 6	        i=i+1
# 7	    yield my_list
# 8	var1=gen()
# 9	#print(next(var1))
# 10	for i in var1:
# 11	    print(i)