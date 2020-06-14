def main(obj):
    count = ''

    while obj // 10 != 0:
        count += str(obj % 10)
        obj = obj // 10
    count += str(obj % 10)
    print(count)


user = int(input('Введите число'))
main(user)