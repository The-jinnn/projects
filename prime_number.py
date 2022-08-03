a=int(input("Input a number to check prime or not: "))
found= False
if (a<2):
    print("The entered number is not a prime numer")
else:
    for i in range (2,a):
        if(a%i==0):
            found= True
    if(found==True):
        print("The entered number is not a prime numer")
    else:
        print("The entered number is a prime number")
