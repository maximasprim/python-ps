
number=input("Input an integer number: ")

sum_of_digits=0

for digit in number:
    sum_of_digits += int(digit)

print(f"The sum of the digits in {number} is {sum_of_digits}")