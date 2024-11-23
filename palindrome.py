#checks if the string is the same forwards and backwards
string=input("Enter a string: ")

if string==string[::-1]:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")