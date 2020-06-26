def my_func():
    n = int(input('Введите количество строк'))
    res = []
    for j in range(n):
        print(f'{j + 1}-я строка:')
        res.append([int(input()) for i in range(4)])
    for j in range(n):
        print(res[j] + [sum(res[j])])

my_func()

