import collections

n = int(input('Количество предприятий: '))
companies = collections.defaultdict(list)
companies_profit = {}
for el in range(n):
    name = input('название предприятия')
    companies_profit[name] = 0
    for j in range(4):
        k = int(input('прибыль за {} квартал: '.format(j+1)))
        companies[name].append(k)
        companies_profit[name] += k

max_comp = ''
min_comp = ''
print(f'Средняя годовая прибыль всех предприятий: {sum(companies_profit.values()) / n}')
for i, j in companies_profit.items():
    if sum(companies_profit.values()) / n < j:
        max_comp += '{}' ' '.format(i)
    else:
        min_comp += '{}' ' '.format(i)

print(f'Предприятия, с прибылью выше среднего значения: {max_comp}')
print(f'Предприятия, с прибылью ниже среднего значения: {min_comp}')