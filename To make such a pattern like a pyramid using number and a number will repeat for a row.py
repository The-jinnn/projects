a=int(input("Input number of rows: "))

for i in range (1,a+1):
    for j in range(a,i,-1):
        print(end=' ')
    for s in range(1,i+1):
        print(i,end=' ')
    print("\n")
    
