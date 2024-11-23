
n= int (input("Input a posiive number: "))
a,b=0,1

if n<=0:
    print("Please enter a positive number")

else:
    print("Fibonnacci sequence:")
    for _ in range(n):
        print(a,end=' ')
        a,b=b,a+b
    