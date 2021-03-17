# Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.
# Примечание: задачу можно решить без сортировки исходного массива.
# Но если это слишком сложно, используйте метод сортировки, который не рассматривался на уроках
# (сортировка слиянием также недопустима).

import random

m = 5
array = [random.randint(-100, 100) for _ in range(2 * m + 1)]
print(array)


def median(arr, k):
    if len(arr) == 1:
        return arr[0]

    pivot = random.choice(arr)

    left_el = [el for el in array if el < pivot]
    right_el = [el for el in array if el > pivot]
    pivots = [el for el in array if el == pivot]

    if k < len(left_el):
        return median(left_el, k)
    elif k < len(left_el) + len(pivots):
        return pivots[0]
    else:
        return median(right_el, k - len(left_el) - len(pivots))


print(f'Медианой списка является:{median(array, len(array) / 2)}')
array.sort()
print(f'Проверка:\n{array}')
