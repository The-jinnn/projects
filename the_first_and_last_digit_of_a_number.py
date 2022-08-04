a=(input("Input any number: "))

for i in range(0,len(a)):
    if i==0:
        print(f"The first digit of {a} is: {a[i]}")

print(f"The first digit of {a} is: {a[len(a)-1]}")
