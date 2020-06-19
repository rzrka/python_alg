import timeit

def without_Eratosthenes(i):
    count = 0
    a = 0
    for k in range(1, i ** i):
        for j in range(1, k + 1):
            if k % j == 0:
                count += 1
        if count <= 2:
            a += 1
        count = 0
        if a == i:
            #print(k)
            return

def Eratosthenes(i):
    start = 1
    end = i
    count = 0
    while True:
        for k in range(start, end + 1):
            for j in range(1, k + 1):
                if k % j == 0:
                    count += 1
            if count <= 2 and k not in res:
                res.append(k)
            end += 1
            count = 0
            start += 1
            if len(res) == i:
                #print(res[-1])
                return
res = []
i = int(input('Введите i-тое число'))
Eratosthenes(i)
without_Eratosthenes(i)

print(timeit.timeit("without_Eratosthenes(i)", setup= "from __main__ import without_Eratosthenes, i", number=100))
print(timeit.timeit("Eratosthenes(i)", setup= "from __main__ import Eratosthenes, i", number=100))

"""
Время работы алгоритма для поиска 10-го простого числа 100 раз:
простой (without_Eratosthenes) - 0.0034508600000000555
решето (Eratosthenes) - 0.00010631500000002347

С решето у меня даже в первом случае получилось быстрее, видимо не достаточно хорошо написал код :(

Время работы алгоритма для поиска 100-го простого числа 100 раз:
простой (without_Eratosthenes) - 0.9242910040000001
решето (Eratosthenes) - 0.00010962700000005654

Время работы алгоритма для поиска 1000-го простого числа 100 раз:
простой (without_Eratosthenes) - 272.307131938
решето (Eratosthenes) - 0.00011625299998740957
"""




