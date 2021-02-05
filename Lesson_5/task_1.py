# Пользователь вводит данные о количестве предприятий,
# их наименования и прибыль за 4 квартал (т.е. 4 числа) для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий)
# и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.
from collections import defaultdict

#  Заполняем данными "базу"
report = defaultdict(list)
top_company = defaultdict(list)
while True:
    company = str(input('Для выхода введите 0\nВведите название компании: '))
    if company == '0':
        break
    else:
        for i in range(1, 4 + 1):
            profit = float(input(f'Введите прибыль за {i} квартал: '))
            report[company].append(profit)
print(report)

# подсчитываем среднюю прибыль
avg_profit = sum([sum(report[i]) for i in report]) / len(report)

# отделяем прибыльные от убыточных
for i in report:
    if sum(report[i]) >= avg_profit:
        top_company['profitable'].append((i, f'Прибыль {sum(report[i])}'))
    else:
        top_company['unprofitable'].append((i, f'Прибыль {sum(report[i])}'))

print(f'Прибыльные компании: {top_company["profitable"]}\n'
      f'Убыточные компании: {top_company["unprofitable"]}')


