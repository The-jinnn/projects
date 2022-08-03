a=int(input("Input number of terms: "))

print("The odd numbers are: ")

sum=0

for i in range(1,a*2):
    if(i%2!=0):
        print(i,end=" ")
        
        sum=sum+i

print(f"\nThe Sum of odd Natural Numbers upto {a} terms: {sum}")
