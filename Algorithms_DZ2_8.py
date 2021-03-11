# Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

required_digit = int(input('Введите цифру, которую хотите найти: '))
numbers = int(input('В скольки числах нужно искать вашу цифру: '))
count = 1
number_count_in = 0

while count <= numbers:
    number = int(input(f'Введите число №{count}: '))
    while True:
        if number % 10 == required_digit:
            number_count_in += 1
        if number // 10 == 0:
            break
        number //= 10
    count += 1

print(f'Цифра {required_digit} встречается {number_count_in} раз')


# Вариант решения Преподавателя:
"""
BASE = 10

num = int(input("Введите количество чисел: "))
digit = int(input("Какую цифру подсчитать: "))
count = 0
for i in range(1, num + 1):
    ans = int(input(f'Введите число {i}: '))
    while ans > 0:
        if ans % BASE == digit:
            count += 1
        ans //= BASE  # ans = ans // 10

print(f'Было введено {count} цифр {digit}')
"""
