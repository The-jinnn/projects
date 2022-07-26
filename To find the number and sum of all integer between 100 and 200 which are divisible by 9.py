sum=0

print("Numbers between 100 and 200, divisible by 9: ")
for i in range (100,200+1):
    if(i%9==0):

        sum=sum+i

        print(i,end=" ")

print(f"\nThe sum : {sum}")