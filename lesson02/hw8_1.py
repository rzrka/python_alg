def meeting(n, n_search):
    count = 0
    order = ''
    for i in range(n):
        order += input(f'Число {i + 1}: ')
    for i in range(len(order)):
        if int(order) % 10 == n_search:
            count += 1
            order = int(order) // 10
        else:
            order = int(order) // 10
    print(f'Было выведено {count} цифр "{n_search}"')

n = int(input('Сколько будет чисел? - '))
n_search = int(input('Какую цифру считать? - '))
meeting(n, n_search)