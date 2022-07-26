from os import sep


a=int(input("Input the value for nth term: "))

c=0
sum=0

for i in range (1,a+1):
   
    c=(1/i)

    print(f"1/{i}",end=" + ")
    
    sum=sum+c

print(f"\nThe sum of the series upto {a} terms: {sum}")
