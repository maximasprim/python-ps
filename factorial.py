

number=int(input("Input a non-negative number: "))
factorial=1

if number< 0:
    print("factorial is not defined for negative numbers")
else:
    for i in range(1,number+1):
        factorial=factorial*i
    print(f"The factorial of {number} is {factorial}")

