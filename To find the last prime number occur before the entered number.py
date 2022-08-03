a=int(input("Input a number to find the last prime number occurs before the number: "))

c=0

for i in range(2,a+1):
        for j in range (2,i):
            if((i%j)==0):
                break
        else:
            c=i

print(f"{c} is the last prime number before {a}")
