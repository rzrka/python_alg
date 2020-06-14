def calculator(a, b, sign):
    if b == 0 and sign == '/':
        print('деление на ноль невозможно')
    elif sign == '+':
        print(a + b)
    elif sign == '-':
        print(a - b)
    elif sign == '*':
        print(a * b)
    elif sign == '/' and b != 0:
        print(a / b)


while True:
    sign = input('введите знак операции или 0 для выхода')
    if sign == '0':
        break
    elif sign != '*' and sign != '/' and sign != '+' and sign != '-':
        print('Неправильный знак операции')
        continue
    try:
        a = int(input('введите первое число: '))
        b = int(input('введите второе число: '))
    except ValueError:
        print('Вы ввели не число')
        continue
    calculator(a, b, sign)
