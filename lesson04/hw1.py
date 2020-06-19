import timeit

def memorize(func):
    def g(n, memory={}):
        r = memory.get(n)
        if r is None:
            r = func(n)
            memory[n] = r
        return r
    return g


@memorize
def line_cycle_mem(n):
    # линейная сложность
    count = 0
    main_dig = 1
    while n > 0:
        count += 2 / (2 ** main_dig)
        n -= 1
        main_dig += 1
        if n <= 0:
            return count
        count += 2 / (2 ** main_dig) * (-1)
        main_dig += 1
        n -= 1
    return count

def line_cycle(n):
    # линейная сложность
    count = 0
    main_dig = 1
    while n > 0:
        count += 2 / (2 ** main_dig)
        n -= 1
        main_dig += 1
        if n <= 0:
            return count
        count += 2 / (2 ** main_dig) * (-1)
        main_dig += 1
        n -= 1
    return count


n = int(input('Введите количество элементов: '))

print(f'Количество элементов - {n}, их сумма - {line_cycle_mem(n)}')
print(f'Количество элементов - {n}, их сумма - {line_cycle(n)}')

print(timeit.timeit("line_cycle_mem(n)", setup= "from __main__ import line_cycle_mem, n", number=1000))
print(timeit.timeit("line_cycle(n)", setup= "from __main__ import line_cycle, n", number=1000))

"""
Результат
0.00018040300000010667- с мемезацией
0.0017651850000000024 - без мемезацией

С мемезацией быстрее
"""

