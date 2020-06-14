def my_def():
    for i in range(32, 127):
        print(f'{i} - {chr(i)}', end='')
        if i % 10 == 1:
            print('')

my_def()
