def number_of_numbers(i):
    global order
    order += input(f'Число: ')
    return meeting(i, n_search)
def meeting(n, n_search):
    global count
    global order
    if n == 0:
        if int(order) // 10 == 0:
            if int(order) % 10 == n_search:
                count += 1
            print(f'Было выведено {count} цифр "{n_search}"')
            return
        else:
            if int(order) % 10 == n_search:
                count += 1
                order = int(order) // 10
            else:
                order = int(order) // 10
            return meeting(n, n_search)
    else:
        return number_of_numbers(n - 1)


count = 0
order = ''
n = int(input('Сколько будет чисел? - '))
n_search = int(input('Какую цифру считать? - '))
meeting(n, n_search)