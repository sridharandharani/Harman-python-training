# wtp to read 3 number from user find smallest num using func
def smallest(a,b,c):
    if (a < b):
        if (a < c):
            return " A is small "
    elif b < c :
        return " B is small "
    else:
        return " C is small "
x = int(input("Enter the 1st number :"))
y = int(input("Enter the 2nd number :"))
z = int(input("Enter the 3rd number :"))
result = smallest(x,y,z)
print(result)