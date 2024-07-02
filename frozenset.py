my_list=[10,12,45,6,"rohan",2,52]
my_tuple=(12,54,67,43)
my_set={23,76,86,45,"siddhant"}
my_dict={"shubham","shreya","Sejal","Rathore"}


p=frozenset(my_list)
q=frozenset(my_tuple)
r=frozenset(my_set)
s=frozenset(my_dict)


# print(p)
# print(q)
# print(r)
# print(s)

print(max(q))
print(sum(q))
print(frozenset(q))
print(q.symmetric_difference(r))