a = int(input("Input the base : "))
b = int(input("Input the exponent : "))

c=1

for i in range (b):
     c=c*a
print(f'{a}^{b} = {c}')
