# В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.

import random

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'{array} Наш массив')

i = 0
max_negative_item = -1
for i in range(len(array)):  # или while i < len(array):
    if array[i] < 0 and max_negative_item == -1:
        max_negative_item = i
    elif 0 > array[i] > array[max_negative_item]:
        max_negative_item = i
if max_negative_item == -1:
    print('Отрицательных элементов в массиве нет.')
else:
    print(f'Максимальный отрицательный элемент = {array[max_negative_item]}, его позиция {max_negative_item}')

# вариант 2 (от Преподавателя)
"""
import random

SIZE = 10
MIN_ITEM = -800
MAX_ITEM = -750
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

num = float('-inf')
for i, item in enumerate(array):
    if 0 > item > num:
        num = item
        index = i

if num != float('-inf'):
    print(f'Максимальное отрицательное число {num} '
          f'находится в ячейке {index}')
"""
