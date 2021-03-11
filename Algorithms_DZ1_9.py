#  Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

print('Ведите 3 разных числа:')

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

mid = a + b + c - max(a, b, c) - min(a, b, c)

print(f'Число {mid} - среднее')


# Вариант Препоавателя:
print('Введите три разных целых числа: ')
a = int(input('1-е: '))
b = int(input('2-е: '))
c = int(input('3-е: '))

if b < a < c or c < a < b:
    print('Среднее:', a)
elif a < b < c or c < b < a:
    print('Среднее:', b)
else:
    print('Среднее:', c)

# print(5 in range(1, 10))  # 1 < 5 < 10    -> быстро
# print(5 in [1, 2, 3, 4, 5, 6, 7, 8, 9])   -> медленно


# Вариант Препоавателя:
print('Введите три разных целых числа: ')
a = int(input('1-е: '))
b = int(input('2-е: '))
c = int(input('3-е: '))

if b < a < c or c < a < b:
    print('Среднее:', a)
elif a < b < c or c < b < a:
    print('Среднее:', b)
else:
    print('Среднее:', c)

# print(5 in range(1, 10))  # 1 < 5 < 10    -> быстро
# print(5 in [1, 2, 3, 4, 5, 6, 7, 8, 9])   -> медленно