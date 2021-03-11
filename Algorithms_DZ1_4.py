# Вариант решения Преподавателя:
# Написать программу, которая генерирует в указанном пользователем диапазоне:
#   случайное целое число,
#   случайное вещественное число,
#   случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона.
# Если надо получить случайный символ от 'a' до 'f', вводятся эти символы.
# Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
import random


#   случайное целое число
print('Случайное целое число')  # В блок-схеме не отражен данный вывод
num_start = int(input('Начало диапазона: '))
num_end = int(input('Конец диапазона: '))
# result = int(random.random() * (num_end - num_start + 1)) + num_start
result = random.randint(num_start, num_end)
print(result)

#   случайное вещественное число
print('Случайное вещественное число')  # В блок-схеме не отражен данный вывод
num_start = float(input('Начало диапазона: '))
num_end = float(input('Конец диапазона: '))
# result = random.random() * (num_end - num_start) + num_start
result = random.uniform(num_start, num_end)
print(round(result, 3))

#   случайный символ
print('Случайный символ')  # В блок-схеме не отражен данный вывод
num_start = ord(input('Начало диапазона: '))
num_end = ord(input('Конец диапазона: '))
# result = int(random.random() * (num_end - num_start + 1)) + num_start
result = random.randint(num_start, num_end)
print(chr(result))
