# Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random

SIZE_LINES = 3
SIZE_COLUMNS = 3
MIN_ITEM = -100
MAX_ITEM = 100
matrix = [[random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_COLUMNS)] for _ in range(SIZE_LINES)]

min_item_of_columns = []
min_item_of_columns.extend(matrix[0])

for item in matrix:
    print(item)
    i = 0
    for j in item:
        if j < min_item_of_columns[i]:
            min_item_of_columns[i] = j
        i += 1
max_among_min = min_item_of_columns[0]
for i in range(1, SIZE_LINES):
    if min_item_of_columns[i] > max_among_min:
        max_among_min = min_item_of_columns[i]

print('-' * 15)
print(min_item_of_columns)
print('Максимальный элемент среди минимальных элементов столбцов матрицы:', max_among_min)

# Вариант преодавателя
"""
import random

SIZE_ROW = 5
SIZE_COL = 4
MIN_ITEM = 0
MAX_ITEM = 100
matrix = [[random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_COL)] for _ in range(SIZE_ROW)]

for line in matrix:
    print(*line, sep='\t')


max_ = None

for j in range(len(matrix[0])):
    min_ = matrix[0][j]

    for i in range(len(matrix)):
        if matrix[i][j] < min_:
            min_ = matrix[i][j]

    if max_ is None or max_ < min_:
        max_ = min_

print(f'Max in min = {max_}')
"""
