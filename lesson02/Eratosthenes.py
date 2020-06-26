import sys
from memory_profiler import profile

sys.setrecursionlimit(100000000)
@profile
def Eratosthenes(start, end, n=1, k=0):
    global res
    if start == end + 1:
        print(res)
        return
    else:
        if n == start + 1:
            if k <= 2:
                res += str(start) + ' '
            return Eratosthenes(start + 1, end, n=1)
        else:
            if start % n == 0:
                return Eratosthenes(start, end, n + 1, k + 1)
            return Eratosthenes(start, end, n + 1, k)

res = ''
start = int(input('Введите стартовое число'))
end = int(input('Введите конечное число'))
Eratosthenes(start, end)