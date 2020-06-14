def evidence(n):
    j = 0
    for i in range(n):
        j += i
    if j == n * (n-1) / 2:
        print(f'сумма натуральных чисел n = n * (n-1) / 2: {j}')

n = int(input('Введите число: '))
evidence(n)