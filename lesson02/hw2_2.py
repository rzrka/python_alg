def even_and_odd(entr_obj):
    global count_even
    global count_odd

    if int(entr_obj) // 10 == 0:
        if (int(entr_obj) % 10) % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
        print(f'Количество четных и нечетных цифр в числе равно: ({count_even}, {count_odd})')
        return
    elif int(entr_obj) // 10 > 0:
        if (int(entr_obj) % 10) % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
        entr_obj = int(entr_obj) // 10
        return even_and_odd(entr_obj)


count_even = 0
count_odd = 0

entr_obj = input('Введите число: ')
even_and_odd(entr_obj)