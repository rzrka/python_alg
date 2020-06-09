first_dig = int(input())
second_dig = int(input())
third_dig = int(input())

if second_dig < first_dig < third_dig or third_dig < first_dig < second_dig:
    print(first_dig)
elif third_dig < second_dig < first_dig or first_dig < second_dig < third_dig:
    print(second_dig)
elif second_dig < third_dig < first_dig or first_dig < third_dig < second_dig:
    print(third_dig)