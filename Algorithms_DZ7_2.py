# Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.

import random
from collections import deque
import itertools

array = [round(random.triangular(0, 50), 2) for i in range(10)]
print(array)
# array = [24.0, 34.89, 25.49, 18.0, 15.16, 11.31, 37.31, 18.26, 1.8, 10.38]


def merge_sort(sort_array):
    if len(sort_array) <= 1:
        return sort_array

    new_size = len(sort_array) // 2

    left = deque(itertools.islice(sort_array, 0, new_size))
    right = deque(itertools.islice(sort_array, new_size, len(sort_array)))

    left = merge_sort(left)
    right = merge_sort(right)

    for i in range(len(sort_array)):
        if len(left) == 0:
            sort_array[i] = right.popleft()
        elif len(right) == 0:
            sort_array[i] = left.popleft()
        else:
            if left[0] <= right[0]:
                sort_array[i] = left.popleft()
            else:
                sort_array[i] = right.popleft()

    return sort_array


print(merge_sort(array))

