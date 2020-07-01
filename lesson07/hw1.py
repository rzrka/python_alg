import random
import timeit

def bubble(org_list):
    for j in range(len(org_list)):
        for i in range(len(org_list) - j):
            try:
                if org_list[i] < org_list[i + 1]:
                    org_list[i], org_list[i+1] = org_list[i+1], org_list[i]
            except IndexError:
                break
    return org_list

def bubble_sort(org_list, n=0):
    while org_list != sorted(org_list, reverse=True):
        for i in range(len(org_list) - n):
            try:
                if org_list[i] < org_list[i + 1]:
                    org_list[i], org_list[i+1] = org_list[i+1], org_list[i]
            except IndexError:
                n += 1
                break
    return org_list

def bubble_sort_v2(org_list):
    check = 0
    for j in range(len(org_list)):
        for i in range(len(org_list) - j):
            try:
                if org_list[i] < org_list[i + 1]:
                    org_list[i], org_list[i + 1] = org_list[i + 1], org_list[i]
                    check += 1
            except IndexError:
                break
        if check == 0:
            return org_list
        check = 0
    return org_list

org_list = [random.randint(-100, 99) for _ in range(100)]
print(org_list)
print(bubble(org_list))

# замер без улучшения самая медленная
print(timeit.timeit("bubble(org_list)",
    setup="from __main__ import bubble, org_list", number=1000))

org_list = [random.randint(-100, 99) for _ in range(100)]
print(org_list)
print(bubble_sort(org_list))
# замер улучшенной быстрее всего
print(timeit.timeit("bubble_sort(org_list)",
    setup="from __main__ import bubble_sort, org_list", number=1000))

org_list = [random.randint(-100, 99) for _ in range(100)]
print(org_list)
print(bubble_sort_v2(org_list))
# замеры улучшенной средняя по скорости
print(timeit.timeit("bubble_sort_v2(org_list)",
    setup="from __main__ import bubble_sort_v2, org_list", number=1000))