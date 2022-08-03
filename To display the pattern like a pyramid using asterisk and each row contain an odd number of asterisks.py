a=int(input("Input number of rows: "))

for i in range (1,a*2):
    if(i%2!=0):
        for j in range(a*2,i,-1):
            print(end=' ')
        for s in range(0,i):
            print('*',end=' ')
        print("\n")

        
