def my_max(n):
    global max_sum
    global max_dig
    if n == 0:
        print(f'Наибольшее число по сумме цифр: {max_dig}, сумма его цифр: {max_sum}')
        return
    else:
        order = input('Введите очередное число:')
        max_order = order
        a = 0
        for j in range(len(order)):
            a += int(order) % 10
            order = int(order) // 10
        if a > max_sum:
            max_sum = a
            max_dig = max_order
        return my_max(n-1)


max_sum = 0
max_dig = 0
n = int(input('Введите количество чисел: '))
my_max(n)