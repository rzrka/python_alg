import hashlib
def bi():
    user = input('Введите строку состоящую из маленьких букв')
    my_set = set()
    for i in range(len(user)):
        for j in range(len(user), i, -1):
            if user[i:j] == user:
                continue
            a = bytearray(user[i:j], encoding='utf-8')
            h = hashlib.sha1(a)
            my_set.add(h.hexdigest())
            if user[i:j] not in my_set:
                print(user[i:j])

    print(my_set)
    print(f'Количество различных подстрок в строке {user} равно {len(my_set)}')

bi()
