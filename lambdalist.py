# num_list = [ 1,2,3,5,65,67,34,64,24,345,564] #create a list
# odd_list = list(filter(lambda x : (x % 2 != 0 ),num_list)) #use list func to create a list,use filter to display only the condition,  use lambda to set an condition and pass the arguments
# print(odd_list)

num_list = [ 1,2,3,5,65,67,34,64,24,345,564] #create a list
odd_list = list(map(lambda x : (x % 2 != 0 ),num_list)) #use list func to create a list,use map to check all the values in the list if the condition is satisfying,  use lambda to set an condition and pass the arguments
print(odd_list) #use map to check all the values in the list if the condition is satisfying
