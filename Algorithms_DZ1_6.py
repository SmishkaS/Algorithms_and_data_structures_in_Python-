# Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

print('Введите номер интересующей Вас буквы алфавита от 1 до 26:')

num = int(input())
char = chr(num + 64)

print(f'Это буква "{char}"')

# Вариант Препоавателя:
num = int(input('Номер буквы в алфавите (1-26): '))
num = ord('a') + num - 1
print(f'Это буква {chr(num)}')

# что делать с 96
FIRST_LETTER = 96
num = int(input('Номер буквы в алфавите (1-26): '))
num = FIRST_LETTER + num
print(f'Это буква {chr(num)}')

# Вариант Препоавателя:
num = int(input('Номер буквы в алфавите (1-26): '))
num = ord('a') + num - 1
print(f'Это буква {chr(num)}')

# что делать с 96
FIRST_LETTER = 96
num = int(input('Номер буквы в алфавите (1-26): '))
num = FIRST_LETTER + num
print(f'Это буква {chr(num)}')
