import random
import sys


def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

user_digit_min, user_digit_max = input().split()

if user_digit_max.isdigit():
    res = round(random.random() * 10 ** (len(user_digit_max) - 1))

    if res < int(user_digit_min):
        res *= 2
    if res < int(user_digit_min):
        res *= 2
    if res < int(user_digit_min):
        res *= 2
    if res < int(user_digit_min):
        res *= 2
    if res < int(user_digit_min):
        res *= 2
    if res < int(user_digit_min):
        res *= 2
    if res < int(user_digit_min):
        res *= 2
    if res < int(user_digit_min):
        res *= 2
    if res < int(user_digit_min):
        res *= 2

    if res > int(user_digit_max):
        res /= 2
    if res > int(user_digit_max):
        res /= 2
    if res > int(user_digit_max):
        res /= 2
    if res > int(user_digit_max):
        res /= 2
    if res > int(user_digit_max):
        res /= 2
    if res > int(user_digit_max):
        res /= 2
    if res > int(user_digit_max):
        res /= 2
    if res > int(user_digit_max):
        res /= 2
    if res > int(user_digit_max):
        res /= 2
    if res > int(user_digit_max):
        res /= 2

    print(int(res))
elif isfloat(user_digit_max):
    user_digit_min.upper()
    user_digit_max.upper()
    res = random.random() * 10 ** (len(user_digit_max) - 1)

    if res < float(user_digit_min):
        res *= 2
    if res < float(user_digit_min):
        res *= 2
    if res < float(user_digit_min):
        res *= 2
    if res < float(user_digit_min):
        res *= 2
    if res < float(user_digit_min):
        res *= 2
    if res < float(user_digit_min):
        res *= 2
    if res < float(user_digit_min):
        res *= 2
    if res < float(user_digit_min):
        res *= 2
    if res < float(user_digit_min):
        res *= 2
    if res < float(user_digit_min):
        res *= 2

    if res > float(user_digit_max):
        res /= 2
    if res > float(user_digit_max):
        res /= 2
    if res > float(user_digit_max):
        res /= 2
    if res > float(user_digit_max):
        res /= 2
    if res > float(user_digit_max):
        res /= 2
    if res > float(user_digit_max):
        res /= 2
    if res > float(user_digit_max):
        res /= 2
    if res > float(user_digit_max):
        res /= 2
    if res > float(user_digit_max):
        res /= 2
    if res > float(user_digit_max):
        res /= 2

    print(float(res))
else:
    res = round(random.random() * 1000)

    if res > ord(user_digit_max):
        res /= 2
    if res > ord(user_digit_max):
        res /= 2
    if res > ord(user_digit_max):
        res /= 2
    if res > ord(user_digit_max):
        res /= 2
    if res > ord(user_digit_max):
        res /= 2
    if res > ord(user_digit_max):
        res /= 2

    res = round(res)

    if chr(res).isalpha():
        print(chr(int(res)).lower())
        sys.exit()
    elif res < ord(user_digit_min):
        res += 3
    elif res > ord(user_digit_min):
        res += 3
    if chr(res).isalpha():
        print(chr(int(res)).lower())
        sys.exit()
    elif res < ord(user_digit_min):
        res += 3
    elif res > ord(user_digit_min):
        res += 3
    if chr(res).isalpha():
        print(chr(int(res)).lower())
        sys.exit()
    elif res < ord(user_digit_min):
        res += 3
    elif res > ord(user_digit_min):
        res += 3
    if chr(res).isalpha():
        print(chr(int(res)).lower())
        sys.exit()
    elif res < ord(user_digit_min):
        res += 3
    elif res > ord(user_digit_min):
        res += 3
    if chr(res).isalpha():
        print(chr(int(res)).lower())
        sys.exit()
    elif res < ord(user_digit_min):
        res += 3
    elif res > ord(user_digit_min):
        res += 3
    if chr(res).isalpha():
        print(chr(int(res)).lower())
        sys.exit()
    elif res < ord(user_digit_min):
        res += 3
    elif res > ord(user_digit_min):
        res += 3
    if chr(res).isalpha():
        print(chr(int(res)).lower())
        sys.exit()
    elif res < ord(user_digit_min):
        res += 3
    elif res > ord(user_digit_min):
        res += 3
    if chr(res).isalpha():
        print(chr(int(res)).lower())
        sys.exit()
    elif res < ord(user_digit_min):
        res += 3
    elif res > ord(user_digit_min):
        res += 3
    if chr(res).isalpha():
        print(chr(int(res)).lower())
        sys.exit()
    elif res < ord(user_digit_min):
        res += 3
    elif res > ord(user_digit_min):
        res += 3
    if chr(res).isalpha():
        print(chr(int(res)).lower())
        sys.exit()
    elif res < ord(user_digit_min):
        res += 3
    elif res > ord(user_digit_min):
        res += 3
    if chr(res).isalpha():
        print(chr(int(res)).lower())
        sys.exit()
    elif res < ord(user_digit_min):
        res += 3
    elif res > ord(user_digit_min):
        res += 3
    if chr(res).isalpha():
        print(chr(int(res)).lower())
        sys.exit()
    elif res < ord(user_digit_min):
        res += 3
    elif res > ord(user_digit_min):
        res += 3




