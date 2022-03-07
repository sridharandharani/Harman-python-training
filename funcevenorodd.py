def evenorodd(x):
    if (x % 2 == 0):
        return "the value is even"
    else:
        return "the value is odd"

a = int(input("enter the value "))
result = evenorodd(a)
print(result)
