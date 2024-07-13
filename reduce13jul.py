#import functools
from functools import reduce

lista=[12,24,565,556,353,34,436]
def max(x,y):
    if x>y:
        return x
    else:
        return y
print(reduce(max,lista))
#print(functools.reduce(maxdigit,lista))