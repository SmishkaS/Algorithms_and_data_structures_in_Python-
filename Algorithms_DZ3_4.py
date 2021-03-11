# Определить, какое число в массиве встречается чаще всего.

import random

SIZE = 10
MIN_ITEM = 0
array = [random.randint(MIN_ITEM, SIZE // 1.5) for _ in range(SIZE)]
print(array)

# вариант 1 с обращением по индексу и вложенными циклами
num = array[0]
frequency = 1
for i in range(len(array)):
    spam = 1
    for j in range(i + 1, len(array)):
        if array[i] == array[j]:
            spam += 1
    if spam > frequency:
        frequency = spam
        num = array[i]

print(f'Число {num} встречется {frequency} раз(а)' if frequency > 1 else 'Все элементы уникальны')

# ваниант 2 со словарём
counter = {}
frequency = 1
num = None
for item in array:
    if item in counter:
        counter[item] += 1
    else:
        counter[item] = 1

    if counter[item] > frequency:
        frequency = counter[item]
        num = item

if num is not None:
    print(f'Число {num} встречется {frequency} раз(а)')
else:
    print('Все элементы уникальны')
