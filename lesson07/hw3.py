import random, statistics
user = int(input()) * 2 + 1
org_list = [random.randint(-100, 99) for _ in range(user)]

def median(org_list):
    check_up = 0
    check_low = 0
    for n1, i in enumerate(org_list):
        for n2, j in enumerate(org_list):
            if i >= j and n1 != n2:
                check_up += 1
            elif i < j and n1 != n2:
                check_low += 1
        if check_low == check_up:
            return i
        check_low = 0
        check_up = 0


print(org_list)
print(statistics.median(org_list))
print(median(org_list))
