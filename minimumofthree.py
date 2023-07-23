num1 = int(input("enter number one"))
num2 = int(input("enter number two"))
num3 = int(input("enter number three"))
if(num1<num2 and num1<num3):
    print("num1 is samllest")
elif(num2<num1 and num2<num3):
    print("num2 is smallest")
else:
    print("num3 is smallest")
