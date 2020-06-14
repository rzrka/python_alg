def line(n):
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
print(f'Количество элементов - {n}, их сумма - {line(n)}')