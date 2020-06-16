def my_func(my_list):
    print([my_list.index(j) for j in my_list if j % 2 == 0])

my_list = [8, 3, 15, 6, 4, 2]
my_func(my_list)
