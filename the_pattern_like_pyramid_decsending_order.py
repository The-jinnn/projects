a=int(input("Input number of rows: "))

for i in range (1,a+1):
    for j in range(a,i,-1):
        print(end=' ')
    for s in range(i,0,-1):
        print(s,end=' ')
        s=i-1
    print("\n")
