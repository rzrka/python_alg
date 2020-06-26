from memory_profiler import profile

@profile
def meeting(n, n_search):
    count = 0
    order = ''
    for i in range(n):
        order += input(f'Число {i + 1}: ')
    del i
    for i in range(len(order)):
        if int(order) % 10 == n_search:
            count += 1
            order = int(order) // 10
        else:
            order = int(order) // 10
    del i
    print(f'Было выведено {count} цифр "{n_search}"')

n = int(input('Сколько будет чисел? - '))
n_search = int(input('Какую цифру считать? - '))
meeting(n, n_search)

'''Питон версией 3.8, ОС Windows 7 x64
В коде можно очистить переменную i когда цикл больше не нужен
Line #    Mem usage    Increment   Line Contents
================================================
     3     12.5 MiB     12.5 MiB   @profile
     4                             def meeting(n, n_search):
     5     12.5 MiB      0.0 MiB       count = 0
     6     12.5 MiB      0.0 MiB       order = ''
     7     12.5 MiB      0.0 MiB       for i in range(n):
     8     12.5 MiB      0.0 MiB           order += input(f'Число {i + 1}: ')
     9     12.5 MiB      0.0 MiB       for i in range(len(order)):
    10     12.5 MiB      0.0 MiB           if int(order) % 10 == n_search:
    11     12.5 MiB      0.0 MiB               count += 1
    12     12.5 MiB      0.0 MiB               order = int(order) // 10
    13                                     else:
    14     12.5 MiB      0.0 MiB               order = int(order) // 10
    15     12.5 MiB      0.0 MiB       print(f'Было выведено {count} цифр "{n_search}"')
'''