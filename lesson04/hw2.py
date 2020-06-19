import timeit

def my_def_cycle():
    # линейная сложность
    for i in range(32, 127):
        print(f'{i} - {chr(i)}', end='')
        if i % 10 == 1:
            print('')

my_def_cycle()

def my_def_rec(a=32):
    # сложность константа
    if a > 127:
        return
    else:
        print(f'{a} - {chr(a)}', end='')
        if a % 10 == 1:
            print('')
        return my_def_rec(a + 1)

my_def_rec()

print(timeit.timeit("my_def_cycle", setup= "from __main__ import my_def_cycle", number=1000))
print(timeit.timeit("my_def_rec", setup= "from __main__ import my_def_rec", number=1000))

"""
1.445699999999897e-05 через цикл
1.3552999999999482e-05 через рекурсию

Через цикл функция работает быстрее
"""