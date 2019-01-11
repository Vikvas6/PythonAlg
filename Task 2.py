# 2. Написать два алгоритма нахождения i-го по счёту простого числа.
#
#    Без использования «Решета Эратосфена»;
#    Используя алгоритм «Решето Эратосфена»
#
# Примечание ко всему домашнему заданию: Проанализировать скорость и сложность
# алгоритмов. Результаты анализа сохранить в виде комментариев в файле с кодом.


import cProfile
import math


# Функция нахождения i-того по счёту простого числа
# Единицу не считаем простым числом
def find_prime(i):
    def is_prime(n):
        for i in range(2, n // 2 + 1):
            if n % i == 0:
                return False
        return True
    cur_num = 1
    cnt = 0
    while True:
        cur_num += 1
        if (is_prime(cur_num)):
            cnt += 1
            if cnt == i:
                return cur_num


def test_find_prime(func):
    results = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    for i in range(len(results)):
        assert results[i] == func(i+1)
        print(f'Test {i+1} OK')

# test_find_prime(find_prime)

# timeit:
# i = 1         100 loops, best of 3: 0.47 usec per loop
# i = 5         100 loops, best of 3: 4.89 usec per loop
# i = 10        100 loops, best of 3: 13.9 usec per loop
# i = 50        100 loops, best of 3: 205 usec per loop
# i = 100       100 loops, best of 3: 853 usec per loop
# i = 500       100 loops, best of 3: 22.2 msec per loop
# i = 1000      100 loops, best of 3: 107 msec per loop
# Вывод - очень похоже, что сложность алгоритма О(n*n),
# во всяком случае на каком-то сайте я смог эти точки
# вполне приемлимым образом аппроксимировать квадратичной
# функцией

# cProfile.run('find_prime(100)')
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#        1    0.000    0.000    0.001    0.001 Task 2.py:15(find_prime)
#      540    0.001    0.000    0.001    0.000 Task 2.py:16(is_prime)
#        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of
#                                               '_lsprof.Profiler' objects}
# Много-много раз вызывается функция проверки простоты
# (100е простое 541, поэтому внутрянняя функция вызвалась 540 раз)


# А теперь алгоритм с применением решета Эратосфена
# В интернете нашёл оценки на i-тое по счёту простое число,
# чтобы не генерить слишком большую решётку
def find_prime_as_Eratosthenes(i):
    if i == 1:
        return 2
    if i == 2:
        return 3
    if i == 3:
        return 5
    if i == 4:
        return 7
    if i == 5:
        return 11
    t = list(range(int(i*(1 + math.log(i) + math.log(math.log(i))))))
    t[1] = 0
    for k in t:
        if k > 1:
            for j in range(2*k, len(t), k):
                t[j] = 0

    for k in t:
        if t[k] != 0:
            i -= 1
            if i == 0:
                return t[k]

# test_find_prime(find_prime_as_Eratosthenes)

# timeit:
# i = 1         100 loops, best of 3: 0.102 usec per loop
# i = 5         100 loops, best of 3: 0.164 usec per loop
# i = 10        100 loops, best of 3: 9.33 usec per loop
# i = 50        100 loops, best of 3: 57.6 usec per loop
# i = 100       100 loops, best of 3: 147 usec per loop
# i = 500       100 loops, best of 3: 950 usec per loop
# i = 1000      100 loops, best of 3: 2.12 msec per loop
# Полагаю, что тут сложность алгоритма O(n*log(n)), это связано
# с размером решета, которое мы строим n*(1 + log(n) + log(log(n))).
# Если использовать другую оценку простых чисел, то и сложность изменится.


# cProfile.run('find_prime_as_Eratosthenes(100)')
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#        1    0.000    0.000    0.000    0.000 Task 2.py:68
#                                              (find_prime_as_Eratosthenes)
#        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#      127    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#        3    0.000    0.000    0.000    0.000 {built-in method math.log}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of
#                                               '_lsprof.Profiler' objects}
# Много раз проверяется размер решета, можно было бы и сохранить в переменную
