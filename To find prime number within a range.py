from operator import truediv


a=int(input("Input number for starting range: "))
b=int(input("Input number for ending range: "))
sum=0
print(f"The prime numbers between {a} and {b} are: ")
for i in range (a,b+1):
    if(1<i):
        for j in range (2,i):
            if((i%j)==0):
                break
        else:
            print(i,end=' ')

            sum=sum+1

print(f"\nThe total number of prime numbers between {a} to {b} is: {sum}")

