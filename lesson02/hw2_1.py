def even_and_odd(entr_obj):
    count_even = 0
    count_odd = 0

    while int(entr_obj) // 10 != 0:
        if (int(entr_obj) % 10) % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
        entr_obj = int(entr_obj) // 10
    if (int(entr_obj) % 10) % 2 == 0:
        count_even += 1
    else:
        count_odd += 1
    print(f'В числе {entr_obj} всего {count_odd + count_even} цифр, из которых {count_even} чётных и {count_odd} нечётных')

entr_obj = input('Введите число: ')
even_and_odd(entr_obj)
