a=int(input("Input the value for nth term: "))

c=0

sum=0

for i in range (1,a+1):
    c=(1/(i**i))
    print(f"1/{i}^{i}= {c}")
    sum=sum+c
print(f"The sum of the above series is: {sum}")
