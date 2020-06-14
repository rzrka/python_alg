import random

def guess(n = 10):
    if n < 0:
        print(f'Вы проиграли. Ответ: {answer}')
        return
    else:
        user_answer = int(input())
        if user_answer == answer:
            print('Вы угадали')
            return
        elif user_answer > answer:
            print('Ваше число больше загаданного')
        else:
            print('Ваше число меньше загаданного')
        return guess(n-1)

answer = random.randint(0, 100)
guess()