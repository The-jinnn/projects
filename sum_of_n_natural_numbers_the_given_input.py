n=int(input("Input a number of terms: "))

sum = 0

print(f"The natural numbers upto {n}th term are : ")

for i in range (1,n+1):
    print(i,end=" ")
    sum=sum+i

print(f"\nThe sum of the natural numbers is: {sum}")
