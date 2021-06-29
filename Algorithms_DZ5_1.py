# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа)
# для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий) и
# отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.
# Задача считается решённой, если в ней использована как минимум одна коллекция из модуля collections.
import collections

number_enterprises = 0
companies = collections.defaultdict(list)
company_profit = 0
all_profit = 0
mid_profit = 0
above_average_profit = collections.deque()
below_average_profit = collections.deque()

while True:
    try:
        number_enterprises = int(input('Сколько предприятий Вы будите вводить?: '))
    except ValueError:
        print('Вы ввели недопустимое значение')
        continue
    break

for i in range(number_enterprises):
    name = input(f'\nВведите название {i + 1}-ого предприятия: ')
    quarter = 1
    while quarter <= 4:
        profit = 0
        try:
            profit = float(input(f'Введите прибыль за {quarter}-й квартал: '))
            company_profit += profit
        except ValueError:
            print('Вы ввели недопустимое значение')
            continue
        quarter += 1
        companies[name].append(company_profit)

all_profit += company_profit
mid_profit = all_profit / number_enterprises

for i, item in companies.items():
    if item >= mid_profit:
        above_average_profit.append(i)
    else:
        below_average_profit.append(i)

print(f'\nСредняя прибыль для всех предприятий составила: {mid_profit}')
print(f'\nПрибыль выше среднего у предприятий:')
for name in above_average_profit:
    print(name)
print(f'\nПрибыль ниже среднего у предприятий:')
for name in below_average_profit:
    print(name)