def line(n):
    global count
    global main_dig
    if n <= 0:
        return
    else:
        count += 2 / (2 ** main_dig)
        n -= 1
        main_dig += 1
        if n <= 0:
            return
        count += 2 / (2 ** main_dig) * (-1)
        main_dig += 1
        n -= 1
        line(n)

main_dig = 1
count = 0
n = int(input('Введите количество элементов: '))
line(n)
print(f'Количество элементов - {n}, их сумма - {count}')