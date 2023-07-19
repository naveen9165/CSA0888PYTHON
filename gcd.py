no = int(input("enter first number"))
nt = int(input("enter second number"))
a = no
b = nt
while b!=0:
    temp = b
    b = a%b
    a = temp

hcf = a
lcm = int((no*nt)/hcf)

print("lcm of two numbers is",lcm)
print("hcf of two numbers is",hcf)
