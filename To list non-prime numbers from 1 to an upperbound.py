a=int(input("Input the upperlimit:  "))

found=False

print("The non-prime numbers are: ")

for i in range(1,a+1):
    if(i>2):
        for j in range(2,i):
            if(i%j==0):
                found=False
                break
            else:
                found=True
        
        if(found==False):
            print(i,end=" ")