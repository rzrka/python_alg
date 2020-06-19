import timeit

def my_func(my_list):
    # линейная сложность
    print([my_list.index(j) for j in my_list if j % 2 == 0])

def my_dic_f(my_list_d):
    # линейная сложность
    for k, v in my_list_d.items():
        if v % 2 == 0:
            my_dic.append(k)


my_list = [8, 3, 15, 6, 4, 2]
my_func(my_list)



my_list_d = {0: 8,1: 3,2: 15,3: 6,4: 4,5: 2}
my_dic = []
my_dic_f(my_list_d)
print(my_dic)

print(timeit.timeit("my_func(my_list)", setup= "from __main__ import my_func, my_list", number=1000))
print(timeit.timeit("my_dic_f(my_list_d)", setup= "from __main__ import my_dic_f, my_list_d", number=1000))

"""
0.007387213 - использование списка
0.0010161630000000005 - использование словаря

Код работает быстрее если используется словарь, даже если использовать более медленный способ составление списка через
append.

P.S. У меня очень много раз принтуется результат, я так понял это из за timeit, но не понятно почему он себя так ведет,
поясните пожалуйста. Можете сами запустить код и посмотреть о чем я 
"""