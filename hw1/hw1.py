user = int(input())
my_sum = user // 100 + (user % 100) // 10 + user % 10
my_composition = (user // 100) * ((user % 100) // 10) * (user % 10)
print(my_sum)
print(my_composition)