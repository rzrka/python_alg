my_list = [1, 2, 2, 2, 3, 4, 5]
print(max(my_list, key=lambda x: my_list.count(x)))
