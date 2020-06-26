from memory_profiler import profile

@profile

def my_func(my_list):
    print(f'Наименьший элемент: {min(my_list)}, встречается в этом массиве {my_list.count(min(my_list))} раз')
    for i in range(my_list.count(min(my_list))):
        my_list.remove(min(my_list))
    print(f'Второй наименьший элемент: {min(my_list)}, встречается в этом массиве {my_list.count(min(my_list))} раз')

my_list = [28, -86, 44, -37, -7, -52, -19, -3, -15, -73, -86]
my_func(my_list)