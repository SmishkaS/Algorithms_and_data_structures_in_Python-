# Написать два алгоритма нахождения i-го по счёту простого числа.
# Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
# Проанализировать скорость и сложность алгоритмов.
#
# Первый — с помощью алгоритма «Решето Эратосфена».
# Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков.
# Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.
#
# Второй — без использования «Решета Эратосфена».
# Примечание. Вспомните классический способ проверки числа на простоту.
# Пример работы программ:
#
# sieve(2)
# 3
# prime(4)
# 7
# sieve(5)
# 11
# prime(1)
# 2

import cProfile
import timeit
import math

# Вариант 1
"""
def prime(num, HOLE=None):
    # size = num ** 2 + 3
    global size
    assert num <= 5_761_455, 'Слишком большой аргумент'
    # if num > 5761455:
    #     raise Exception('Слишком большой аргумент')
    pi_func = {4: 10,
               25: 10 ** 2,
               168: 10 ** 3,
               1_229: 10 ** 4,
               9_592: 10 ** 5,
               78_498: 10 ** 6,
               664_579: 10 ** 7,
               5_761_455: 10 ** 8,
               }
    for key in pi_func:
        if num <= key:
            size = pi_func[key]
            break

    array = [i for i in range(size)]

    array[1] = HOLE
    for i in range(2, size):
        if array[i] != HOLE:
            # j = i + i
            j = i ** 2
            while j < size:
                array[j] = HOLE
                j += i

    res = [i for i in array if i != HOLE]
    return res[num - 1]


def test_prime(func):
    real_prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101,
                  103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199,
                  211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317,
                  331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443,
                  449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577,
                  587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701,
                  709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839,
                  853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983,
                  991, 997, 1009, 1013]

    for i, item in enumerate(real_prime, start=1):
        assert func(i) == item, f'Test {i} fail\t func({i}) = {func(i)}'
        print(f'Test {i} OK')


test_prime(prime)
print(prime(10))

number = 1
while number < 4000:
    number *= 2
    t_it = timeit.timeit('prime(number)', number=1000, globals=globals())
    print(f"{number}\t{t_it}\t{t_it / number}")

# number=2	    t_it=0.003825800000000004	t_it / number =0.001912900000000002
# number=4	    t_it=0.0029166999999999943	t_it / number =0.0007291749999999986
# number=8	    t_it=0.02392430000000001	t_it / number =0.002990537500000001
# number=16	    t_it=0.028611000000000025	t_it / number =0.0017881875000000016
# number=32	    t_it=0.24387409999999998	t_it / number =0.0076210656249999995
# number=64	    t_it=0.23843159999999997	t_it / number =0.0037254937499999995
# number=128	t_it=0.23993849999999994	t_it / number =0.0018745195312499996
# number=256	t_it=2.4913249	            t_it / number =0.009731737890625
# number=512	t_it=2.5026221000000004	    t_it / number =0.004887933789062501
# number=1024	t_it=2.556224900000001	    t_it / number =0.002496313378906251
# number=2048	t_it=31.9847047	            t_it / number =0.015617531591796876
# number=4096	t_it=30.311263299999993	    t_it / number =0.007400210766601561


cProfile.run('prime(5000)')

#       6 function calls in 0.039 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.039    0.039 <string>:1(<module>)
#      1    0.004    0.004    0.004    0.004 sieve.py:28(<listcomp>)
#      1    0.003    0.003    0.003    0.003 sieve.py:39(<listcomp>)
#      1    0.032    0.032    0.039    0.039 sieve.py:9(prime)
#      1    0.000    0.000    0.039    0.039 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


print(timeit.timeit('prime(1228)', number=1000, globals=globals()))
# 2.5282643000000036

print(timeit.timeit('prime(1230)', number=1000, globals=globals()))
# 32.095177899999996
"""

# Вариант 2

HOLE = False


def prime(num):
    multiplier = 1.3
    size = int(num * math.log(num) * multiplier) if num > 10 else 30

    array = [True for _ in range(size)]
    array[:2] = [HOLE, HOLE]
    count = 0

    for i in range(2, size):
        if array[i]:

            count += 1
            if count == num:
                return i

            for j in range(i ** 2, size, i):
                array[j] = HOLE


def test_prime(func):
    real_prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101,
                  103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199,
                  211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317,
                  331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443,
                  449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577,
                  587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701,
                  709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839,
                  853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983,
                  991, 997, 1009, 1013]

    for i, item in enumerate(real_prime, start=1):
        assert func(i) == item, f'Test {i} fail\t func({i}) = {func(i)}'
        print(f'Test {i} OK')


test_prime(prime)

# Поиск большого простого числа на 32х Python выдал ошибку MemoryError
# Но на 64х версии интерпретатора код успешно завершился
# print(timeit.timeit('prime(10_000_000)', globals=globals(), number=1))
# # Ответ: 179424673 Время: 54.154248359339334


number = 1
while number < 16000:
    number *= 2
    t_it = timeit.timeit('prime(number)', number=1000, globals=globals())
    print(f"{number}\t{t_it}\t{t_it / number}")

# number=2	    t_it=0.004134799999999994	t_it / number =0.002067399999999997
# number=4	    t_it=0.0060433000000000014	t_it / number =0.0015108250000000004
# number=8	    t_it=0.004758999999999999	t_it / number =0.0005948749999999999
# number=16	    t_it=0.012488699999999991	t_it / number =0.0007805437499999995
# number=32	    t_it=0.023932199999999987	t_it / number =0.0007478812499999996
# number=64	    t_it=0.055452	            t_it / number =0.0008664375
# number=128	t_it=0.14081200000000002	t_it / number =0.0011000937500000002
# number=256	t_it=0.3485395	            t_it / number =0.001361482421875
# number=512	t_it=0.7077077	            t_it / number =0.0013822416015625
# number=1024	t_it=1.5482496000000001	    t_it / number =0.0015119625000000001
# number=2048	t_it=3.5068982999999996	    t_it / number =0.0017123526855468748
# number=4096	t_it=7.4202434	            t_it / number =0.001811582861328125
# number=8192	t_it=16.532505399999998	    t_it / number =0.0020181281005859373
# number=16384	t_it=40.1398753	            t_it / number =0.0024499435607910156


cProfile.run('prime(5000)')

#       6 function calls in 0.013 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.013    0.013 <string>:1(<module>)
#      1    0.002    0.002    0.002    0.002 sieve_plus.py:12(<listcomp>)
#      1    0.011    0.011    0.013    0.013 sieve_plus.py:8(prime)
#      1    0.000    0.000    0.013    0.013 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {built-in method math.log}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# Вариант 3
"""
def prime(num):
    count = 1
    current_prime = 2

    while count < num:
        current_prime += 1
        # for i in range(2, current_prime):
        for i in range(2, int(current_prime ** 0.5) + 1):
            if current_prime % i == 0:
                break
        else:
            count += 1

    return current_prime


def test_prime(func):
    real_prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101,
                  103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199,
                  211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317,
                  331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443,
                  449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577,
                  587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701,
                  709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839,
                  853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983,
                  991, 997, 1009, 1013]

    for i, item in enumerate(real_prime, start=1):
        assert func(i) == item, f'Test {i} fail\t func({i}) = {func(i)}'
        print(f'Test {i} OK')


test_prime(prime)
print(prime(1))

number = 1
while number < 4000:
    number *= 2
    t_it = timeit.timeit('prime(number)', number=1000, globals=globals())
    print(f"{number=}\t{t_it=}\t{t_it / number =}")

# number=2	    t_it=0.0005367000000000011	t_it / number =0.00026835000000000053
# number=4	    t_it=0.0029206999999999983	t_it / number =0.0007301749999999996
# number=8	    t_it=0.013426099999999996	t_it / number =0.0016782624999999995
# number=16	    t_it=0.04451730000000001	t_it / number =0.0027823312500000006
# number=32	    t_it=0.082261	            t_it / number =0.00257065625
# number=64	    t_it=0.22009230000000002	t_it / number =0.0034389421875000003
# number=128	t_it=0.5136050999999999	    t_it / number =0.004012539843749999
# number=256	t_it=1.2283394999999997	    t_it / number =0.004798201171874999
# number=512	t_it=2.8059278	            t_it / number =0.005480327734375
# number=1024	t_it=7.440694399999999	    t_it / number =0.007266303124999999
# number=2048	t_it=18.4085388	            t_it / number =0.0089885443359375
# number=4096	t_it=52.09239900000001	    t_it / number =0.012717870849609377


cProfile.run('prime(5000)')

#       4 function calls in 0.136 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.136    0.136 <string>:1(<module>)
#      1    0.136    0.136    0.136    0.136 without_sieve.py:5(prime)
#      1    0.000    0.000    0.136    0.136 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""
