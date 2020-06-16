def my_func(my_list):
    a, pos_a = max(my_list), my_list.index(max(my_list))
    b, pos_b = min(my_list), my_list.index(min(my_list))
    my_list[pos_b], my_list[pos_a] = a, b
    print(my_list)

my_func(my_list = [int(i) for i in input('Введите значения через пробел ').split()])


