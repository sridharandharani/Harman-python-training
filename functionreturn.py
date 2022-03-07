def addnumbers(a, b):  # defining the function
    c = a + b
    return c  # returns the value to called function


x = int(input("Enter the number :"))
y = int(input("Enter the number :"))
total = addnumbers(x, y)  # calling the function
print(total)
