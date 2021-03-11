# Проанализировать скорость и сложность одного любого алгоритма из разработанных
# в рамках домашнего задания первых трех уроков.
# Примечание. Идеальным решением будет:
# ● выбрать хорошую задачу, которую имеет смысл оценивать (укажите в комментарии какую задачу вы взяли),
# ● написать 3 варианта кода (один у вас уже есть),
# ● проанализировать 3 варианта и выбрать оптимальный,
# ● результаты анализа вставить в виде комментариев в файл с кодом
# (не забудьте указать, для каких N вы проводили замеры),
# ● написать общий вывод: какой из трёх вариантов лучше и почему.

# Выбрал задачу Algorithms_DZ3_9:
# Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import timeit
import cProfile
import random

SIZE_LINES = 5
SIZE_COLUMNS = 5
MIN_ITEM = -100
MAX_ITEM = 100


# Cоздам объект класса Matrix, что бы было проще играть с диапазонами.

class Matrix:

    def __init__(self, SIZE_LINES, SIZE_COLUMNS, MIN_ITEM, MAX_ITEM):
        self.SIZE_LINES = SIZE_LINES
        self.COLUMNS = SIZE_COLUMNS
        self.MIN_ITEM = MIN_ITEM
        self.MAX_ITEM = MAX_ITEM
        self.MATRIX = [[random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_COLUMNS)] for _ in range(SIZE_LINES)]

    def __str__(self):
        return f'{self.MATRIX}'


# test = Matrix(SIZE_LINES, SIZE_COLUMNS, MIN_ITEM, MAX_ITEM)
# print(test)  # Проверка работы класса

# Test1 Меняем SIZE
Test1_1 = Matrix(SIZE_LINES=150, SIZE_COLUMNS=150, MIN_ITEM=-100, MAX_ITEM=100)
Test1_2 = Matrix(SIZE_LINES=300, SIZE_COLUMNS=300, MIN_ITEM=-100, MAX_ITEM=100)
Test1_3 = Matrix(SIZE_LINES=450, SIZE_COLUMNS=450, MIN_ITEM=-100, MAX_ITEM=100)

# Test2 Меняем ITEM
Test2_1 = Matrix(SIZE_LINES=5, SIZE_COLUMNS=5, MIN_ITEM=-300, MAX_ITEM=300)
Test2_2 = Matrix(SIZE_LINES=5, SIZE_COLUMNS=5, MIN_ITEM=-900, MAX_ITEM=900)
Test2_3 = Matrix(SIZE_LINES=5, SIZE_COLUMNS=5, MIN_ITEM=-2700, MAX_ITEM=2700)

# Test3 Меняем и SIZE и ITEM
Test3_1 = Matrix(SIZE_LINES=150, SIZE_COLUMNS=150, MIN_ITEM=-300, MAX_ITEM=300)
Test3_2 = Matrix(SIZE_LINES=300, SIZE_COLUMNS=300, MIN_ITEM=-900, MAX_ITEM=900)
Test3_3 = Matrix(SIZE_LINES=450, SIZE_COLUMNS=450, MIN_ITEM=-2700, MAX_ITEM=2700)


# Прогоняем через мой вариант решения.
def my_version(matrix):
    min_item_of_columns = []
    min_item_of_columns.extend(matrix[0])
    for item in matrix:
        # print(item)
        i = 0
        for j in item:
            if j < min_item_of_columns[i]:
                min_item_of_columns[i] = j
            i += 1
    max_among_min = min_item_of_columns[0]
    for i in range(1, SIZE_LINES):
        if min_item_of_columns[i] > max_among_min:
            max_among_min = min_item_of_columns[i]
    return max_among_min
    # print('Максимальный элемент среди минимальных элементов столбцов матрицы:', max_among_min)


print('my_version timeit:')
print(timeit.timeit('my_version(Test1_1.MATRIX)', number=1000, globals=globals()))  # 1.2330352000000002
print(timeit.timeit('my_version(Test1_2.MATRIX)', number=1000, globals=globals()))  # 5.597966100000001
print(timeit.timeit('my_version(Test1_3.MATRIX)', number=1000, globals=globals()))  # 11.6389542
print(timeit.timeit('my_version(Test2_1.MATRIX)', number=1000, globals=globals()))  # 0.0022687999999995156
print(timeit.timeit('my_version(Test2_2.MATRIX)', number=1000, globals=globals()))  # 0.0022604000000008284
print(timeit.timeit('my_version(Test2_3.MATRIX)', number=1000, globals=globals()))  # 0.002248300000001535
print(timeit.timeit('my_version(Test3_1.MATRIX)', number=1000, globals=globals()))  # 1.2035202999999974
print(timeit.timeit('my_version(Test3_2.MATRIX)', number=1000, globals=globals()))  # 4.9103932000000015
print(timeit.timeit('my_version(Test3_3.MATRIX)', number=1000, globals=globals()))  # 11.6717419

cProfile.run('my_version(Test1_3.MATRIX)')
cProfile.run('my_version(Test2_3.MATRIX)')
cProfile.run('my_version(Test3_3.MATRIX)')

"""
5 function calls in 0.012 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.012    0.012 <string>:1(<module>)
        1    0.012    0.012    0.012    0.012 Algorithms_DZ4_1.py:59(my_version)
        1    0.000    0.000    0.012    0.012 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method 'extend' of 'list' objects}


         5 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 Algorithms_DZ4_1.py:59(my_version)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method 'extend' of 'list' objects}


         5 function calls in 0.012 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.012    0.012 <string>:1(<module>)
        1    0.012    0.012    0.012    0.012 Algorithms_DZ4_1.py:59(my_version)
        1    0.000    0.000    0.012    0.012 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method 'extend' of 'list' objects}
"""


# Прогоняем через вариант преподавателя.
def teacher_version(matrix):
    max_ = None

    for j in range(len(matrix[0])):
        min_ = matrix[0][j]

        for i in range(len(matrix)):
            if matrix[i][j] < min_:
                min_ = matrix[i][j]

        if max_ is None or max_ < min_:
            max_ = min_
    return max_
    # print(f'Max in min = {max_}')


print('teacher_version timeit')
print(timeit.timeit('teacher_version(Test1_1.MATRIX)', number=1000, globals=globals()))  # 1.0987319999999983
print(timeit.timeit('teacher_version(Test1_2.MATRIX)', number=1000, globals=globals()))  # 4.567094399999995
print(timeit.timeit('teacher_version(Test1_3.MATRIX)', number=1000, globals=globals()))  # 11.430183600000007
print(timeit.timeit('teacher_version(Test2_1.MATRIX)', number=1000, globals=globals()))  # 0.0031652999999991493
print(timeit.timeit('teacher_version(Test2_2.MATRIX)', number=1000, globals=globals()))  # 0.0031560999999982187
print(timeit.timeit('teacher_version(Test2_3.MATRIX)', number=1000, globals=globals()))  # 0.0031340000000028567
print(timeit.timeit('teacher_version(Test3_1.MATRIX)', number=1000, globals=globals()))  # 1.1421200999999996
print(timeit.timeit('teacher_version(Test3_2.MATRIX)', number=1000, globals=globals()))  # 4.879401399999999
print(timeit.timeit('teacher_version(Test3_3.MATRIX)', number=1000, globals=globals()))  # 12.549986400000009

cProfile.run('teacher_version(Test1_3.MATRIX)')
cProfile.run('teacher_version(Test2_3.MATRIX)')
cProfile.run('teacher_version(Test3_3.MATRIX)')
"""
455 function calls in 0.012 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.012    0.012 <string>:1(<module>)
        1    0.012    0.012    0.012    0.012 Algorithms_DZ4_1.py:98(teacher_version)
        1    0.000    0.000    0.012    0.012 {built-in method builtins.exec}
      451    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


         10 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 Algorithms_DZ4_1.py:98(teacher_version)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        6    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


         455 function calls in 0.013 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.013    0.013 <string>:1(<module>)
        1    0.013    0.013    0.013    0.013 Algorithms_DZ4_1.py:98(teacher_version)
        1    0.000    0.000    0.013    0.013 {built-in method builtins.exec}
      451    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

# Прогоним используя библиотеку numpy
import numpy as np


def numpy_version(matrix):
    max_among_min = 0
    matrix = np.rot90(matrix)
    for i in matrix:
        if min(i) > max_among_min:
            max_among_min = min(i)
    return max_among_min


print('numpy_version timeit')
print(timeit.timeit('numpy_version(Test1_1.MATRIX)', number=1000, globals=globals()))  # 2.429730400000011
print(timeit.timeit('numpy_version(Test1_2.MATRIX)', number=1000, globals=globals()))  # 9.33642789999999
print(timeit.timeit('numpy_version(Test1_3.MATRIX)', number=1000, globals=globals()))  # 20.596078399999996
print(timeit.timeit('numpy_version(Test2_1.MATRIX)', number=1000, globals=globals()))  # 0.01914309999999375
print(timeit.timeit('numpy_version(Test2_2.MATRIX)', number=1000, globals=globals()))  # 0.01933089999999993
print(timeit.timeit('numpy_version(Test2_3.MATRIX)', number=1000, globals=globals()))  # 0.01951090000000022
print(timeit.timeit('numpy_version(Test3_1.MATRIX)', number=1000, globals=globals()))  # 2.4581646999999975
print(timeit.timeit('numpy_version(Test3_2.MATRIX)', number=1000, globals=globals()))  # 9.396607399999994
print(timeit.timeit('numpy_version(Test3_3.MATRIX)', number=1000, globals=globals()))  # 20.822831000000008

cProfile.run('numpy_version(Test1_3.MATRIX)')
cProfile.run('numpy_version(Test2_3.MATRIX)')
cProfile.run('numpy_version(Test3_3.MATRIX)')
"""
482 function calls (480 primitive calls) in 0.021 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <__array_function__ internals>:2(flip)
        1    0.000    0.000    0.011    0.011 <__array_function__ internals>:2(rot90)
        1    0.000    0.000    0.000    0.000 <__array_function__ internals>:2(transpose)
        1    0.000    0.000    0.021    0.021 <string>:1(<module>)
        1    0.000    0.000    0.020    0.020 Algorithms_DZ4_1.py:136(numpy_version)
        1    0.000    0.000    0.011    0.011 _asarray.py:110(asanyarray)
        1    0.000    0.000    0.000    0.000 fromnumeric.py:52(_wrapfunc)
        1    0.000    0.000    0.000    0.000 fromnumeric.py:598(_transpose_dispatcher)
        1    0.000    0.000    0.000    0.000 fromnumeric.py:602(transpose)
        1    0.000    0.000    0.000    0.000 function_base.py:146(_flip_dispatcher)
        1    0.000    0.000    0.000    0.000 function_base.py:150(flip)
        1    0.000    0.000    0.000    0.000 function_base.py:55(_rot90_dispatcher)
        1    0.000    0.000    0.011    0.011 function_base.py:59(rot90)
        2    0.000    0.000    0.000    0.000 index_tricks.py:748(__getitem__)
        1    0.000    0.000    0.000    0.000 numeric.py:1341(normalize_axis_tuple)
        1    0.000    0.000    0.000    0.000 numeric.py:1391(<listcomp>)
        1    0.000    0.000    0.000    0.000 {built-in method _operator.index}
        1    0.000    0.000    0.021    0.021 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.getattr}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.hasattr}
        3    0.000    0.000    0.000    0.000 {built-in method builtins.len}
      450    0.009    0.000    0.009    0.000 {built-in method builtins.min}
        1    0.000    0.000    0.000    0.000 {built-in method numpy.arange}
        1    0.011    0.011    0.011    0.011 {built-in method numpy.array}
      3/1    0.000    0.000    0.011    0.011 {built-in method numpy.core._multiarray_umath.implement_array_function}
        1    0.000    0.000    0.000    0.000 {built-in method numpy.core._multiarray_umath.normalize_axis_index}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method 'transpose' of 'numpy.ndarray' objects}


         37 function calls (35 primitive calls) in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <__array_function__ internals>:2(flip)
        1    0.000    0.000    0.000    0.000 <__array_function__ internals>:2(rot90)
        1    0.000    0.000    0.000    0.000 <__array_function__ internals>:2(transpose)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 Algorithms_DZ4_1.py:136(numpy_version)
        1    0.000    0.000    0.000    0.000 _asarray.py:110(asanyarray)
        1    0.000    0.000    0.000    0.000 fromnumeric.py:52(_wrapfunc)
        1    0.000    0.000    0.000    0.000 fromnumeric.py:598(_transpose_dispatcher)
        1    0.000    0.000    0.000    0.000 fromnumeric.py:602(transpose)
        1    0.000    0.000    0.000    0.000 function_base.py:146(_flip_dispatcher)
        1    0.000    0.000    0.000    0.000 function_base.py:150(flip)
        1    0.000    0.000    0.000    0.000 function_base.py:55(_rot90_dispatcher)
        1    0.000    0.000    0.000    0.000 function_base.py:59(rot90)
        2    0.000    0.000    0.000    0.000 index_tricks.py:748(__getitem__)
        1    0.000    0.000    0.000    0.000 numeric.py:1341(normalize_axis_tuple)
        1    0.000    0.000    0.000    0.000 numeric.py:1391(<listcomp>)
        1    0.000    0.000    0.000    0.000 {built-in method _operator.index}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.getattr}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.hasattr}
        3    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        5    0.000    0.000    0.000    0.000 {built-in method builtins.min}
        1    0.000    0.000    0.000    0.000 {built-in method numpy.arange}
        1    0.000    0.000    0.000    0.000 {built-in method numpy.array}
      3/1    0.000    0.000    0.000    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
        1    0.000    0.000    0.000    0.000 {built-in method numpy.core._multiarray_umath.normalize_axis_index}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method 'transpose' of 'numpy.ndarray' objects}


         482 function calls (480 primitive calls) in 0.021 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <__array_function__ internals>:2(flip)
        1    0.000    0.000    0.012    0.012 <__array_function__ internals>:2(rot90)
        1    0.000    0.000    0.000    0.000 <__array_function__ internals>:2(transpose)
        1    0.000    0.000    0.021    0.021 <string>:1(<module>)
        1    0.000    0.000    0.021    0.021 Algorithms_DZ4_1.py:136(numpy_version)
        1    0.000    0.000    0.012    0.012 _asarray.py:110(asanyarray)
        1    0.000    0.000    0.000    0.000 fromnumeric.py:52(_wrapfunc)
        1    0.000    0.000    0.000    0.000 fromnumeric.py:598(_transpose_dispatcher)
        1    0.000    0.000    0.000    0.000 fromnumeric.py:602(transpose)
        1    0.000    0.000    0.000    0.000 function_base.py:146(_flip_dispatcher)
        1    0.000    0.000    0.000    0.000 function_base.py:150(flip)
        1    0.000    0.000    0.000    0.000 function_base.py:55(_rot90_dispatcher)
        1    0.000    0.000    0.012    0.012 function_base.py:59(rot90)
        2    0.000    0.000    0.000    0.000 index_tricks.py:748(__getitem__)
        1    0.000    0.000    0.000    0.000 numeric.py:1341(normalize_axis_tuple)
        1    0.000    0.000    0.000    0.000 numeric.py:1391(<listcomp>)
        1    0.000    0.000    0.000    0.000 {built-in method _operator.index}
        1    0.000    0.000    0.021    0.021 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.getattr}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.hasattr}
        3    0.000    0.000    0.000    0.000 {built-in method builtins.len}
      450    0.009    0.000    0.009    0.000 {built-in method builtins.min}
        1    0.000    0.000    0.000    0.000 {built-in method numpy.arange}
        1    0.012    0.012    0.012    0.012 {built-in method numpy.array}
      3/1    0.000    0.000    0.012    0.012 {built-in method numpy.core._multiarray_umath.implement_array_function}
        1    0.000    0.000    0.000    0.000 {built-in method numpy.core._multiarray_umath.normalize_axis_index}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method 'transpose' of 'numpy.ndarray' objects}
"""


# Вариант по просьбе преподователя.
# с транспонированием через zip(*matrix).
def transpose_zip(matrix):
    max_among_min = 0
    matrix[:] = [list(x) for x in zip(*matrix)]
    for i in matrix:
        if min(i) > max_among_min:
            max_among_min = min(i)
    return max_among_min


print('transpose_zip timeit:')
print(timeit.timeit('transpose_zip(Test1_1.MATRIX)', number=1000, globals=globals()))  # 0.6490236999999865
print(timeit.timeit('transpose_zip(Test1_2.MATRIX)', number=1000, globals=globals()))  # 2.5829484999999863
print(timeit.timeit('transpose_zip(Test1_3.MATRIX)', number=1000, globals=globals()))  # 6.419689099999999
print(timeit.timeit('transpose_zip(Test2_1.MATRIX)', number=1000, globals=globals()))  # 0.0025757999999882486
print(timeit.timeit('transpose_zip(Test2_2.MATRIX)', number=1000, globals=globals()))  # 0.0022338999999931275
print(timeit.timeit('transpose_zip(Test2_3.MATRIX)', number=1000, globals=globals()))  # 0.0022076000000197382
print(timeit.timeit('transpose_zip(Test3_1.MATRIX)', number=1000, globals=globals()))  # 0.6537979000000007
print(timeit.timeit('transpose_zip(Test3_2.MATRIX)', number=1000, globals=globals()))  # 2.7480726000000004
print(timeit.timeit('transpose_zip(Test3_3.MATRIX)', number=1000, globals=globals()))  # 7.703316000000001

cProfile.run('transpose_zip(Test1_3.MATRIX)')
cProfile.run('transpose_zip(Test2_3.MATRIX)')
cProfile.run('transpose_zip(Test3_3.MATRIX)')
"""
 455 function calls in 0.012 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.012    0.012 <string>:1(<module>)
        1    0.005    0.005    0.012    0.012 Algorithms_DZ4_1.py:166(transpose_zip)
        1    0.003    0.003    0.003    0.003 Algorithms_DZ4_1.py:168(<listcomp>)
        1    0.000    0.000    0.012    0.012 {built-in method builtins.exec}
      450    0.005    0.000    0.005    0.000 {built-in method builtins.min}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


         10 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 Algorithms_DZ4_1.py:166(transpose_zip)
        1    0.000    0.000    0.000    0.000 Algorithms_DZ4_1.py:168(<listcomp>)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        5    0.000    0.000    0.000    0.000 {built-in method builtins.min}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


         455 function calls in 0.012 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.012    0.012 <string>:1(<module>)
        1    0.001    0.001    0.012    0.012 Algorithms_DZ4_1.py:166(transpose_zip)
        1    0.006    0.006    0.006    0.006 Algorithms_DZ4_1.py:168(<listcomp>)
        1    0.000    0.000    0.012    0.012 {built-in method builtins.exec}
      450    0.006    0.000    0.006    0.000 {built-in method builtins.min}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

# Вывод:
# Увеличивая диапазон ITEM с -100:100 до -2700:2700 скорость особо не меняется,
# однако если увеличивать SIZE матрицы с 150:150 до 450:450 время работы ощютимо увеличивается.
# Лидером по скорости оказался вариант transpose_zip на втором месте my_version с небольшим отрывом от teacher_version
# и самый тормозной вариант через numpy_version
# 1) transpose_zip 7.70
# 2) my_version 11.67
# 3) teacher_version 12.54
# 4) numpy_version 20.82

