n=int(input("Enter any number"))
digit,x=0,n



while n>0:
    rev=n%10
    digit=digit*10+rev
    n=n//10
# print(digit)
# print(n)
# print(x)
if x==digit:
    print("Palindrome")
else:
    print("Not a palindroeme")    