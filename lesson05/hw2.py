from collections import deque

def f():
    my_dic = {}

    for el in range(1, 3):
        my_dic[f'n{el}'] = deque(input('Введите число').upper())

    my_sum = int(''.join(my_dic['n1']), 16) + int(''.join(my_dic['n2']), 16)
    my_composition = int(''.join(my_dic['n1']), 16) * int(''.join(my_dic['n2']), 16)

    print(hex(my_sum)[2:])
    print(hex(my_composition)[2:])

f()