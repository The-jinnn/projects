a = input("Input any number : ")

n=len(a)
c=0

print(f"The first digit of {a} is: {a[0]}")
print(f"The last digit of {a} is: {a[n-1]}")

for i in range (n):
    if i==0:
        c=c+int(a[i])
    if i==n-1:
        c=c+int(a[i])

print(f"The sum of first and last digit of {a} is: {c}")
