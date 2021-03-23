# Определение количества различных подстрок с использованием хеш-функции.
# Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.
# Примечание: в сумму не включаем пустую строку и строку целиком.
# Пример работы функции:
# # func("papa")
# 6
# func("sova")
# 9

word = input('Введите строку: ')
# word = 'papa'


def func(string):
    result = set()

    for i in range(1, len(string)):
        for j in range(len(string) - i + 1):
            h = hash(string[j:i+j])
            result.add(h)
            # print(string[j:i+j])

    return len(result)


print(f'В данной строке {func(word)} различных подстрок')
