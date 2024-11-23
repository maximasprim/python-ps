import datetime #import datetime module to work with date and time

# Get the current date and time
now= datetime.datetime.now()

#display the current date and time
print("current date and time:")

#print the current date and time
print(now.strftime("%Y-%M-%D %H:%M:%S"))

