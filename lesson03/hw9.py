def my_func():
    min_list = []
    n = int(input('Задайте количество строк в матрице: '))
    m = int(input('Задайте количество столбцов в матрице: '))
    matr = [input().split() for i in range(n)]
    count_min = 0
    for i in range(m):
        for j in range(n):
            if count_min == 0 or int(matr[j][i]) < count_min:
                count_min = int(matr[j][i])
        min_list.append(count_min)
        count_min = 0
    print(f'{min_list} минимальные значения по столбцам')
    print(f'Максимальное среди них = {max(min_list)}')

my_func()