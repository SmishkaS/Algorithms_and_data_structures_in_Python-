# Найти сумму n элементов следующего ряда чисел:
#  1, -0.5, 0.25, -0.125, ...
# Количество элементов (n) вводится с клавиатуры.

n = int(input('Сколько элементов сложить: '))
item = 1
sum_ = 0
for _ in range(n):
    sum_ += item
    item /= -2      # item *= -0.5
print(sum_)

# вариант с геометрической прогрессией
summa_2 = 1 * (1 - (-0.5) ** n) / (1 - (-0.5))
print(summa_2)


# вариант с рекурсией
def devil_sum(num, start=1.0, step=-0.5):
    if num == 1:
        return start
    if num > 55:
        return 2/3
    return start + devil_sum(num - 1, start * step)


print(devil_sum(n))
# рассказать про плохие имена переменных
b = sum([2, 4, 6])
