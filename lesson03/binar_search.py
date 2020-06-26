from memory_profiler import profile

@profile

def binar_seacrh(my_list):
    new_list = []
    n = int(input('Введите число: '))
    while my_list != [n]:
        a = len(my_list) // 2
        if n < my_list[a]:
            for i in my_list[:a]:
                new_list.append(i)
            my_list = new_list
            new_list = []
        else:
            for i in my_list[a:]:
                new_list.append(i)
            my_list = new_list
            new_list = []
    print(my_list)

my_list = [1, 3, 7, 8, 15, 16, 19, 20, 30, 32]
binar_seacrh(my_list)