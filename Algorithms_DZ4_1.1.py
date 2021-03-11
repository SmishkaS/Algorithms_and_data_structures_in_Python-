# Проанализировать скорость и сложность одного любого алгоритма из разработанных
# в рамках домашнего задания первых трех уроков.
# Примечание. Идеальным решением будет:
# ● выбрать хорошую задачу, которую имеет смысл оценивать (укажите в комментарии какую задачу вы взяли),
# ● написать 3 варианта кода (один у вас уже есть),
# ● проанализировать 3 варианта и выбрать оптимальный,
# ● результаты анализа вставить в виде комментариев в файл с кодом
# (не забудьте указать, для каких N вы проводили замеры),
# ● написать общий вывод: какой из трёх вариантов лучше и почему.

# Выбрана задача Algorithms_DZ3_5:
# В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.

import random
import timeit
import cProfile

# Вариант 1
"""
def max_below_zero(size):
    # SIZE = 10
    # MIN_ITEM = -800
    # MAX_ITEM = -750
    array = [random.randint(size * -10, size * 10) for _ in range(size)]
    # print(array)

    i = 0
    index = -1

    while i < len(array):
        if array[i] < 0 and index == -1:
            index = i
        elif 0 > array[i] > array[index]:
            index = i
        i += 1

    if index != -1:
        # print(f'Максимальное отрицательное число {array[index]} '
        #       f'находится в ячейке {index}')
        return f'Максимальное отрицательное число {array[index]} ' \
               f'находится в ячейке {index}'


print(timeit.timeit('max_below_zero(10)', number=1000, globals=globals()))      # 0.014425200000000003
print(timeit.timeit('max_below_zero(100)', number=1000, globals=globals()))     # 0.137323
print(timeit.timeit('max_below_zero(1000)', number=1000, globals=globals()))    # 1.5733725
print(timeit.timeit('max_below_zero(10000)', number=1000, globals=globals()))   # 15.867839900000002

# "max_below_zero(10)"
# 1000 loops, best of 5: 13.2 usec per loop
# "max_below_zero(100)"
# 1000 loops, best of 5: 128 usec per loop
# "max_below_zero(1000)"
# 1000 loops, best of 5: 1.37 msec per loop
# "max_below_zero(10000)"
# 1000 loops, best of 5: 13.6 msec per loop


# cProfile.run('max_below_zero(10_000)')
#          63153 function calls in 0.025 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.025    0.025 <string>:1(<module>)
#         1    0.003    0.003    0.022    0.022 hw05_tested.py:13(<listcomp>)
#         1    0.002    0.002    0.025    0.025 hw05_tested.py:9(max_below_zero)
#     10000    0.009    0.000    0.011    0.000 random.py:237(_randbelow_with_getrandbits)
#     10000    0.005    0.000    0.017    0.000 random.py:290(randrange)
#     10000    0.003    0.000    0.020    0.000 random.py:334(randint)
#         1    0.000    0.000    0.025    0.025 {built-in method builtins.exec}
#     10001    0.001    0.000    0.001    0.000 {built-in method builtins.len}
#     10000    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#     13147    0.001    0.000    0.001    0.000 {method 'getrandbits' of '_random.Random' objects}
#
#
#
# Process finished with exit code 0
"""


# Вариант 2
"""
def max_below_zero(array):
    i = 0
    index = -1

    while i < len(array):
        if array[i] < 0 and index == -1:
            index = i
        elif 0 > array[i] > array[index]:
            index = i
        i += 1

    if index != -1:
        # print(f'Максимальное отрицательное число {array[index]} '
        #       f'находится в ячейке {index}')
        return f'Максимальное отрицательное число {array[index]} ' \
               f'находится в ячейке {index}'


size = 1
while size != 10000:
    size *= 10
    array = [random.randint(size * -10, size * 10) for _ in range(size)]
    print(timeit.timeit('max_below_zero(array)', number=1000, globals=globals()))

# 0.003008999999999998 - 10
# 0.027393             - 100
# 0.27870900000000004  - 1000
# 3.4331880000000004   - 10000

# python -m timeit -n 100 -s "import hw05_tested_2" "hw05_tested_2.max_below_zero(hw05_tested_2.array)"
# 100 loops, best of 5: 1.66 usec per loop    - 10
# 100 loops, best of 5: 12.7 usec per loop    - 100
# 100 loops, best of 5: 140  usec per loop    - 1000
# 100 loops, best of 5: 1.39 msec per loop    - 10000

# cProfile.run('max_below_zero(array)')
#          15 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 hw05_tested_2.py:9(max_below_zero)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        11    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""


# Вариант 3
def max_below_zero_while(array):
    i = 0
    index = -1

    while i < len(array):
        if array[i] < 0 and index == -1:
            index = i
        elif 0 > array[i] > array[index]:
            index = i
        i += 1

    if index != -1:
        return f'Максимальное отрицательное число {array[index]} ' \
               f'находится в ячейке {index}'


def max_below_zero_for(array):
    index = -1

    for i in range(len(array)):
        if array[i] < 0 and index == -1:
            index = i
        elif 0 > array[i] > array[index]:
            index = i

    if index != -1:
        return f'Максимальное отрицательное число {array[index]} ' \
               f'находится в ячейке {index}'


def max_below_zero_enumerate(array):
    max_below = index = None

    for i, item in enumerate(array):
        if item < 0 and max_below is None:
            max_below = item
            index = i
        elif 0 > item > max_below:
            max_below = item
            index = i

    if max_below is not None:
        return f'Максимальное отрицательное число {max_below} ' \
               f'находится в ячейке {index}'


with open('result.txt', 'w', encoding='utf-8') as f:
    f.write(f'size,while,for,enumerate\n')
    for size in range(100, 10_001, 100):
        data = [random.randint(size * -10, size * 10) for _ in range(size)]
        whi_ = timeit.timeit('max_below_zero_while(data)', number=1000, globals=globals())
        for_ = timeit.timeit('max_below_zero_for(data)', number=1000, globals=globals())
        enu_ = timeit.timeit('max_below_zero_enumerate(data)', number=1000, globals=globals())
        f.write(f'{size},{whi_},{for_},{enu_}\n')
