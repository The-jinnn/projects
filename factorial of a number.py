from re import I


a=int(input("Input a number to find the factorial: "))

sum =1

for i in range (1,a+1):
    sum=sum*i
    
print(f"The factorial of the given number is: {sum}")
