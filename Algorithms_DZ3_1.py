# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

# Мой вариант (без массива)
first_range_from = 2
first_range_to = 100
second_range_from = 2
second_range_to = 10

for digit in range(second_range_from, second_range_to):
    count = 0
    for number in range(first_range_from, first_range_to):
        if number % digit == 0:
            count += 1
    print(f'Натуральное число {digit} встречается {count} раз в диапозоне от 2 до 99')

# Вариант преподавателя (c массивом)
"""
start_num = 2
end_num = 99
start_div = 2
end_div = 9

print('вариант 2')
frequency = [0] * (end_div - start_div + 1)  # [0] * 8  или [0 for _ in range(8)]
for i in range(start_num, end_num + 1):
    for j in range(start_div, end_div + 1):
        if i % j == 0:
            frequency[j - start_div] += 1

for i, item in enumerate(frequency, start=start_div):
    print(f'Числу {i} кратно {item} чисел')
"""
