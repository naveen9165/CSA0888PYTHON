n=int(input("enter a number"))
a=[]
while(n>0):
    dig=n%2
    a.append(dig)
    n=n//2
a.reverse()
print("binary equivalent is:")
for i in a:
    print(i, end=" ")
