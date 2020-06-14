def my_def(a=32):
    if a > 127:
        return
    else:
        print(f'{a} - {chr(a)}', end='')
        if a % 10 == 1:
            print('')
        return my_def(a + 1)

my_def()
