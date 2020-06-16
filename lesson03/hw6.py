def my_func(my_list):
    a = my_list[(my_list.index(max(my_list))+1):my_list.index(min(my_list))]
    if a == []:
        a = my_list[(my_list.index(min(my_list))+1):my_list.index(max(my_list))]
    print(f'Сумма элементов между минимальным ({min(my_list)})  и максимальным ({max(my_list)}) элементами: {sum(a)}')
my_list = [88, 58, 50, 77, 49, 89, 88, 67, 14, 6, 2]
my_func(my_list)