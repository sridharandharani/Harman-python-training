# wtp a to check wheather is divisible by 8 or not using func
def divby8(x):
    if (x % 8 == 0):
        return "It is divisible"
    else:
        return " It is not divisible"

div = int(input("Enter the number :"))
result = divby8(div)
print(result)
