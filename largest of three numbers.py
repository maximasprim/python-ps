#prompt user to input the three numbers

num1=float(input("Input the first number: "))
num2=float(input("Input the second number: "))
num3=float(input("Input the third number: "))
#check which number is the largest

if num1>=num2 and num1>=num3:
    print("The largest number is: ",num1)
elif num2>=num1 and num2>=num3:
    print("The largest number is: ",num2)
else:    
    print("The largest number is: ",num3)   