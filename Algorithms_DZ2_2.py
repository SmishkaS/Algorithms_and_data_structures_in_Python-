#  Посчитать четные и нечетные цифры введенного натурального числа.
#  Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

num = input('Введите натуральное число: ')

# Мой вариант.
even_digits = "02468"
odd_digits = "13579"
even = 0
odd = 0

for i in num:
    if i in even_digits:
        even += 1
    if i in odd_digits:
        odd += 1

print(f'{even} - Четные\n{odd} - Нечетные')


# Варианты решения Преподавателя:
"""
# вариант 1
num = int(input('Введите целое число: '))
even, odd = 0, 0
while num > 0:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
    num = num // 10
print(f"четных - {even}, нечетных - {odd}")


# вариант 2, рекурсия
def even_odd(number, even_=0, odd_=0):
    if number == 0:
        return even_, odd_
    if number % 2 == 0:
        even_ += 1
    else:
        odd_ += 1
    number = number // 10
    return even_odd(number, even_, odd_)


num = int(input('Введите целое число: '))
print(even_odd(num))
"""
