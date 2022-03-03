num = int(input("Enter the number:"))
reverse = 0
while num != 0:
    rem = num % 10
    reverse =  reverse * 10 + rem
    num //= 10
print("The reverse of number is :" + str(reverse))
