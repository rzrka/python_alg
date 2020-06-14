def main(obj):
    global count

    if obj // 10 == 0:
        count += str(obj % 10)
    else:
        count += str(obj % 10)
        obj = obj // 10
        return main(obj)
    print(count)

count = ''
user = int(input('Введите число'))
main(user)