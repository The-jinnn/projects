a=int(input("Input the number upto: "))

for i in range(1,10+1):
    for j in range(1,a+1):

        print(f"{j}X{i}={i*j}",end=" ")

    print('\n')
    
