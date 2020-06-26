from memory_profiler import profile

@profile
def my_func(my_list):
    max = min(my_list)
    max_ind = 0
    for i in my_list:
        if i > max and i < 0:
            max = i
            max_ind = my_list.index(i)
    del my_list
    print(f'Максимальный отрицательный элемент в данном массиве = {max}, его индекс {max_ind}')


my_list = [-55, -69, -5, 72, -41, -58, -79, 58, 74, 1]
my_func(my_list)

'''Питон версией 3.8, ОС Windows 7 x64
Здесь можно очистить входящией список my_list
Line #    Mem usage    Increment   Line Contents
================================================
     3     12.4 MiB     12.4 MiB   @profile
     4                             def my_func(my_list):
     5     12.4 MiB      0.0 MiB       max = min(my_list)
     6     12.4 MiB      0.0 MiB       max_ind = 0
     7     12.4 MiB      0.0 MiB       for i in my_list:
     8     12.4 MiB      0.0 MiB           if i > max and i < 0:
     9     12.4 MiB      0.0 MiB               max = i
    10     12.4 MiB      0.0 MiB               max_ind = my_list.index(i)
    11     12.4 MiB      0.0 MiB       print(f'Максимальный отрицательный элемент в данном массиве = {max}, его индекс {max_ind}')



Process finished with exit code 0

'''