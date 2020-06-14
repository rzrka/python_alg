import random

def guess():
    answer = random.randint(0, 100)
    for i in range(10):
        user_answer = int(input())
        if user_answer == answer:
            print('Вы угадали')
            return
        elif user_answer > answer:
            print('Ваше число больше загаданного')
        else:
            print('Ваше число меньше загаданного')
    print(f'Вы проиграли. Ответ: {answer}')

guess()