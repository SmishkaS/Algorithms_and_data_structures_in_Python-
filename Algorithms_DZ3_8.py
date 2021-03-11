# Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.

SIZE_LINES = 5
SIZE_COLUMNS = 3
matrix = []

for i in range(SIZE_LINES):
    line = []
    for j in range(SIZE_COLUMNS):
        value = int(input(f'Введите зачение {j+1} строки {i+1}: '))
        line.append(value)
    matrix.append(line)

for i in matrix:
    sum_line = 0
    for line, item in enumerate(i):
        sum_line += item
        print(f'{item:>7}', end='')
    print(f'{sum_line:>10}')
