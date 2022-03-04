# wtp to create a new list which contains all the number in between 2 and 100 which is divisible by 7
list = []
for i in range (2,101):
    if i % 7 == 0:
        list.append(i)

print(list)