#prompt user to input a sequence of numbers
values=input("Input some comma seprated numbers : ")
#split the values strin into a list using commas as separators and store it in a list variable
list=values.split(",")
#convert the list into a tuple
tuple=tuple(list)

print('List : ',list)
print('Tuple : ',tuple)