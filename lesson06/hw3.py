from memory_profiler import profile

@profile
def my_func():
    n = int(input('Введите количество строк'))
    res = []
    for j in range(n):
        print(f'{j + 1}-я строка:')
        res.append([int(input()) for i in range(4)])
    del j
    for j in range(n):
        print(res[j] + [sum(res[j])])

my_func()

'''
Питон версией 3.8, ОС Windows 7 x64
В коде можно очистить переменную j когда цикл больше не нужен
Line #    Mem usage    Increment   Line Contents
================================================
     3     12.5 MiB     12.5 MiB   @profile
     4                             def my_func():
     5     12.5 MiB      0.0 MiB       n = int(input('Введите количество строк'))
     6     12.5 MiB      0.0 MiB       res = []
     7     12.5 MiB      0.0 MiB       for j in range(n):
     8     12.5 MiB      0.0 MiB           print(f'{j + 1}-я строка:')
     9     12.5 MiB      0.0 MiB           res.append([int(input()) for i in range(4)])
    10     12.5 MiB      0.0 MiB       del j
    11     12.5 MiB      0.0 MiB       for j in range(n):
    12     12.5 MiB      0.0 MiB           print(res[j] + [sum(res[j])])



Process finished with exit code 0

'''