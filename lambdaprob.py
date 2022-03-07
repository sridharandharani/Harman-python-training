# wtp to create a new list which contains all the numbers which is divisible by 5
num_list = [i for i in range(1,101)]
divby5 = list(filter(lambda x : (x % 5 == 0),num_list))
print(divby5)


