print("Please input the kind of data you wanna add")
a=input()
if a=='int':
    x=int(input("Enter the first element: "))
    y=int(input("Enter the second element: "))
elif a=='float':
    x=float(input("Enter the first element: "))
    y=float(input("Enter the second element: "))
elif a=='string':
    x=input("Enter the first element: ")
    y=input("Enter the second element: ")
else :
    print("Invalid type of data")
print(f"{x}+{y}={x+y}")