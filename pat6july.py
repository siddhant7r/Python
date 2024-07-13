n=int(input("how many row required"))
i=1
while i<n:
    print((n - i) * (' ') + i * ' *')
    i=i+1
i=0
while i<n:
    print(i * ' ' + (n - i) * (' *'))
    i=i+1