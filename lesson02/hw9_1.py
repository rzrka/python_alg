def my_max(n):
    max_sum = 0
    for i in range(n):
        order = input('Введите очередное число:')
        max_order = order
        a = 0
        for j in range(len(order)):
            a += int(order) % 10
            order = int(order) // 10
        if a > max_sum:
            max_sum = a
            max_dig = max_order
    print(f'Наибольшее число по сумме цифр: {max_dig}, сумма его цифр: {max_sum}')




n = int(input('Введите количество чисел: '))
my_max(n)