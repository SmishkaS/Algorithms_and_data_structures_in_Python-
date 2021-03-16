# 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех
# уроков. Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для одной и той же задачи.
# Результаты анализа вставьте в виде комментариев к коду. Также укажите в комментариях версию Python и разрядность
# вашей ОС.

# Выбрал задачу Algorithms_DZ2_3:
# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843.
import sys
import inspect
from collections import deque

# Сформируем число из 10 цифр сразу:
N = [1234567890]
memory = {}


def show_size(x):
    size = sys.getsizeof(x)
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                size += show_size(key)
                size += show_size(value)
        elif not isinstance(x, str):
            for item in x:
                size += show_size(item)

    return size


def version_loop_while(n):
    n_num = N[n]
    memory[inspect.stack()[0][3]] = 0
    res = 0
    while n_num > 0:
        res = res * 10 + n_num % 10
        n_num = n_num // 10

    for locs in locals().values():
        memory[inspect.stack()[0][3]] += show_size(locs)

    return res


def version_loop_for(n):
    n_num = N[n]
    memory[inspect.stack()[0][3]] = 0
    n_rev = ''
    n_num = str(n_num)
    for i in n_num:
        n_rev = i + n_rev

    for locs in locals().values():
        memory[inspect.stack()[0][3]] += show_size(locs)

    return int(n_rev)


def version_recursion(n):
    n_num = N[n]
    memory[inspect.stack()[0][3]] = 0

    def rev(a, a_rev):
        for locs in locals().values():
            memory[inspect.stack()[-2][3]] += show_size(locs)

        if a == 0:
            return a_rev
        else:
            return rev(a // 10, a_rev * 10 + a % 10)

    for locs in locals().values():
        memory[inspect.stack()[0][3]] += show_size(locs)

    return rev(n_num, 0)


def version_deque(n):
    n_num = N[n]
    n_rev = deque(str(n_num))
    n_rev.reverse()
    memory[inspect.stack()[0][3]] = 0
    for locs in locals().values():
        memory[inspect.stack()[0][3]] += show_size(locs)

    return int(''.join(n_rev))


version_loop_while(0)
version_loop_for(0)
version_recursion(0)
version_deque(0)

for name in memory:
    print(f'{name} потребляет {memory[name]} байт памяти под переменные для разворота')

# Выводы:
# Лидером c наиболее эффективным использованием памяти стал вариант "version_loop_while" потребляет 76 байт памяти
# на втором месте version_loop_for потребляет 192 байт памяти
# на третьем месте version_deque потребляет 1188 байт памяти
# самый не эффекивный version_recursion потребляет 2296 байт памяти
# Измерение проводил на ноуте Aser Predator PH315-51 Процессор i7 8750H 2.20GHz x64 ОЗУ 16Гб OS Windows 10 home
