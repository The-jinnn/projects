a=int(input("Input number of rows: "))

for i in range(a,0,-1):
    for j in range(0,a-i):
        print(end=' ')
    for k in range(1,i+1):
        print(k,end=' ')
    print("\n")
