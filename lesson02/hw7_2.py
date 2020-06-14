import sys

sys.setrecursionlimit(100000000)

def evidence(n, j = 1):
    if j == n * (n-1) / 2:
        print(f'сумма натуральных чисел n = n * (n-1) / 2: {j}')
        return
    else:
        return evidence(n, j + 1)


n = int(input('Введите число: '))
evidence(n)