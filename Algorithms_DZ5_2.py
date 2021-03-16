# Написать программу сложения и умножения двух положительных целых шестнадцатеричных чисел.
# При этом каждое число представляется как коллекция, элементы которой — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
# hex() и/или int() для преобразования систем счисления = под запретом.

from collections import deque
import timeit
import cProfile

# Как легко и просто можно было бы решить с hex() и int()
"""
a = 'A2'
b = 'C4F'
c = hex(int(a, 16) + int(b, 16)) чясь
print(c.upper()[2:])
"""


# Вариант сложения без модуля collections

# print('Введите два числа в шестнадцатиричной системе исчисления:')
# num_1 = input('num_1 = ')  # Для даного решения переводить в массив нет необходимости
# num_2 = input('num_2 = ')
# Для проверки
# num_1 = 'A2'
# num_2 = 'C4F'

# num_1 = num_1.upper()
# num_2 = num_2.upper()

def sum_without_module(n):  # Добавил для теста скорости (Можно удалить)
    num_1 = 'A2'  # Добавил для теста скорости (Можно удалить)
    num_2 = 'C4F'  # Добавил для теста скорости (Можно удалить)
    # создаём список из элементов 16-ричной системы
    list_of_numbers = [str(i) for i in range(10)] + ['A', 'B', 'C', 'D', 'E', 'F']
    # Сравниваем входные строки и выбираем большую для итераций по её символам.
    if len(num_1) > len(num_2):
        num_1, num_2 = num_2, num_1
    # Переворачиваем выбранную строку и создаём список куда будем добавлять новые, найденные элементы.
    num_2 = num_2[::-1]
    answer_list = []

    j = -1
    k = 0
    for i in num_2:
        one = list_of_numbers.index(i)
        two = list_of_numbers.index(num_1[j])
        answer_list.append(
            list_of_numbers[(one + two + k) % 16])  # Чтоб не вывалится за границы, берём остаток от деления
        if (one + two) >= 15:
            k = 1
        else:
            k = 0
        j -= 1
        if j == -len(num_1) - 1:
            break

    diff = len(num_2) - len(num_1)
    # Как только цикл закончен, проверям, отличались ли у нас вообще числа.
    # Если да, то проходим по оставшимся символам большей строки и прибавляем их.
    if diff:
        for i in num_2[-diff:]:
            answer_list.append(list_of_numbers[(list_of_numbers.index(num_2[-diff]) + k) % 16])
            if list_of_numbers.index(num_2[-diff]) + 1 >= 15:
                k = 1
            else:
                k = 0
    # если после последний итерации этого цикла у нас число перешло в другой разряд, то просто добавляем ещё одну еденицу.
    if k == 1:
        answer_list.append('1')
    # переворачиваем список в нужный нам вид и преобразуем в строку
    answer_list = answer_list[::-1]
    # print(f"num_1 + num_2 = {''.join(answer_list)}")
    return f"num_1 + num_2 = {''.join(answer_list)}"  # Добавил для теста скорости (Можно удалить)


print(timeit.timeit('sum_without_module(1)', number=100, globals=globals()))  # 0.0004977000000000037
print(timeit.timeit('sum_without_module(1)', number=1000, globals=globals()))  # 0.005236999999999999
print(timeit.timeit('sum_without_module(1)', number=10000, globals=globals()))  # 0.0476898
print(timeit.timeit('sum_without_module(1)', number=100000, globals=globals()))  # 0.4814826
print(timeit.timeit('sum_without_module(1)', number=1000000, globals=globals()))  # 4.7699025

cProfile.run('sum_without_module(1)')
"""
21 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 Algorithms_DZ5_2.py:32(sum_without_module)
        1    0.000    0.000    0.000    0.000 Algorithms_DZ5_2.py:36(<listcomp>)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        6    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        3    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        6    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'join' of 'str' objects}
"""


# Вариант сложения и умножения по условию
# print('Введите два числа в шестнадцатиричной системе исчисления:')
# num_1 = input('num_1 = ')
# num_2 = input('num_2 = ')
# Для проверки
# num_1 = 'A2'
# num_2 = 'C4F'

# num_1 = deque(num_1.upper())
# num_2 = deque(num_2.upper())
def sum_with_modul(n):  # Добавил для теста скорости (Можно удалить)
    num_1 = 'A2'  # Добавил для теста скорости (Можно удалить)
    num_2 = 'C4F'  # Добавил для теста скорости (Можно удалить)
    list_of_numbers = [str(i) for i in range(10)] + ['A', 'B', 'C', 'D', 'E', 'F']
    # Создаём два словаря с 16-ой системой исчисления для поиска по ключам.
    hex_dec = {list_of_numbers[i]: i for i in range(len(list_of_numbers))}
    dec_hex = {i: list_of_numbers[i] for i in range(len(list_of_numbers))}

    if len(num_1) < len(num_2):
        num_1, num_2 = num_2, num_1

    # Сложение
    def sum_hex(num_1, num_2):
        sum_ = deque()
        add = 0

        for i in range(len(num_1) - 1, -1, -1):
            l_dec = hex_dec[num_1[i]]  # l = left
            r_i = len(num_2) - (len(num_1) - i)  # r = right

            if r_i < 0:
                r_dec = 0
            else:
                r_dec = hex_dec[num_2[r_i]]
            sum_dec = l_dec + r_dec + add
            sum_.appendleft(dec_hex[sum_dec % 16])
            add = sum_dec // 16

        if add != 0:
            sum_.appendleft(dec_hex[add])
        return sum_

    return f"a + b = {''.join(sum_hex(num_1, num_2))}"  # Добавил для теста скорости (Можно удалить)


print(timeit.timeit('sum_with_modul(1)', number=100, globals=globals()))  # 0.0006653000000005349
print(timeit.timeit('sum_with_modul(1)', number=1000, globals=globals()))  # 0.006504900000000369
print(timeit.timeit('sum_with_modul(1)', number=10000, globals=globals()))  # 0.06470629999999922
print(timeit.timeit('sum_with_modul(1)', number=100000, globals=globals()))  # 0.6565325
print(timeit.timeit('sum_with_modul(1)', number=1000000, globals=globals()))  # 6.6353976999999995

cProfile.run('sum_with_modul(1)')
"""
23 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 Algorithms_DZ5_2.py:113(sum_with_modul)
        1    0.000    0.000    0.000    0.000 Algorithms_DZ5_2.py:116(<listcomp>)
        1    0.000    0.000    0.000    0.000 Algorithms_DZ5_2.py:118(<dictcomp>)
        1    0.000    0.000    0.000    0.000 Algorithms_DZ5_2.py:119(<dictcomp>)
        1    0.000    0.000    0.000    0.000 Algorithms_DZ5_2.py:126(sum_hex)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
       11    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        3    0.000    0.000    0.000    0.000 {method 'appendleft' of 'collections.deque' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method 'join' of 'str' objects}
"""
"""
# Умножение
def mult_hex(num_1, num_2):
    mult_ = deque()

    for i in range(len(num_2) - 1, -1, -1):
        add = 0
        mult_i = deque()
        r_dec = hex_dec[num_2[i]]

        for j in range(len(num_1) - 1, -1, -1):
            l_dec = hex_dec[num_1[j]]
            mult_dec = r_dec * l_dec + add
            mult_i.appendleft(dec_hex[mult_dec % 16])
            add = mult_dec // 16
        mult_i.appendleft(dec_hex[add])

        for j in range(len(num_2) - 1 - i):
            mult_i.append('0')
        mult_ = sum_hex(mult_i, mult_)

    return mult_


sum_total, mult_total = num_1, num_2

print(f"\na + b = {''.join(sum_hex(num_1, num_2))}")
print(f"a * b = {''.join(mult_hex(num_1, num_2))}")
"""

# Вывод:
# Если все правильно сделал то при сложении двух одинаковых переменных
# скорость при варианте без использования модуля и с переворачиванием массива быстрее на 25%.
