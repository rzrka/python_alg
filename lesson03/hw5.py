

def my_func(my_list):
    max = min(my_list)
    max_ind = 0
    for i in my_list:
        if i > max and i < 0:
            max = i
            max_ind = my_list.index(i)
    print(f'Максимальный отрицательный элемент в данном массиве = {max}, его индекс {max_ind}')


my_list = [-55, -69, -5, 72, -41, -58, -79, 58, 74, 1]
my_func(my_list)