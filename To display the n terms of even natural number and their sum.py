a=int(input("Input number of terms: "))

print("The Even numbers are: ")

sum=0

for i in range(1,a*2+1):
    if(i%2==0):
        print(i,end=" ")
        
        sum=sum+i

print(f"\nThe Sum of Even Natural Numbers upto {a} terms: {sum}")