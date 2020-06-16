def my_func(start, end):
    for j in range(2, 10):
        print(f'В диапазоне {start}-{end}: {len([i for i in range(start, end+1) if i % j == 0])} чисел кратны {j}')

start, end = input('Введите диапазон через пробел').split()
my_func(int(start), int(end))

