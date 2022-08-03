a=input("Input a number: ")

rev=0

for i in range (1,len(a)+1):
    
    rem = int(a) % 10  
    rev = (rev * 10) + rem 
    a = int(a) // 10  

print("The number in reverse order is :",rev)

