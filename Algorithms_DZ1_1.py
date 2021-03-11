# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

# https://drive.google.com/file/d/1ygKoi9rE88TrLVFnFjhuGaYjJwSPcssa/view?usp=sharing
# Налекции сказанно для решения не забегать вперед (т.е. не пользоваться циклами, функциями, списками и т.п.)
# Как не забегая вперед проверить, что нам ввели именно 3-х значное число?
# Мой вариант решения:
while True:
    number = input("Введите трехзначное число:")
    if 100 <= int(number) <= 999:
        break
    print('Число не трехзначное!!!')

summa = 0
composition = 1

for i in number:
    summa += int(i)
    composition *= int(i)
print(f"Сумма цифр числа {number}: {summa}")
print(f"Произведение цифр: {number}: {composition}")


# Вариант решения Преподавателя:
# Проверки на то что пользователь ввел 3-х значное число НЕТу ни в одном из вариантов.
num = input('Введите натуральное трёхзначное число: ')

# решение через долнительные переменные
num = int(num)
a = num // 100
b = num % 100 // 10
c = num % 10
summary = a + b + c
# mult = a * b * c
print(f'Сумма = {summary}')
print(f'Произведение = {a * b * c}')


# решение через цикл для темы урока 2
num = str(num)
summary = 0
mult = 1
for i in num:
    summary += int(i)
    mult *= int(i)
print(f'Сумма = {summary}')
print(f'Произведение = {mult}')


