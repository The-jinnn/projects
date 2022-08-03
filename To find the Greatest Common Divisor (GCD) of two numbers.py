a=int(input("Input the first number: "))
b=int(input("Input the second number: "))

d=0

if a>b:
    c=b
else:
    c=a

#print(c)

for i in range (2,c+1):
    if (a%i==0) and (b%i==0):
        if (i>d):
            d=i
print(f"The Greatest Common Divisor is: {d}")
