a=int(input("Enter the number: "))

if(a>3):
 for i in range(2,a) :
    if ((a%i)==0):
        print("The number is not prime")
        break
else :
   print("The number is prime")