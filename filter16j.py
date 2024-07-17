my_list=[20,30,40,50,60]
def new(n):
    if n>30:
        return True
print(list(filter(new,my_list)))    