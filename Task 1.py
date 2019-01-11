# Задание номер 1 из урока номер 3 (с дополнением)
# Оригинальная задача:
#   В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны
#   любому из чисел в диапазоне от 2 до 9.
# Дополнение функционала:
#   На вход функции будем передавать число n, и будем определять в диапазоне
#   от 2 до n сколько из них кратны любому из чисел в диапазоне от 2 до 9.
# Дополнение вывода:
#   Уберём из функции print и вместо этого будем возвращать список с
#   результатами, в списке по порядку содержатся количества чисел
#   кратных от 2х до 9ти.

import cProfile


def print_result(n, result):
    print(f'Количество чисел из диапазона 2-{n},'
          'кратных числам из диапазона 2-9:')
    for i in range(2, 10):
        print(f'Числу {i} кратно {result[i-2]} чисел из диапазона 2-{n}')


def test_func(func):
    true_result = [49, 33, 24, 19, 16, 14, 12, 11]
    assert_result = func()
    for i, item in enumerate(true_result):
        assert assert_result[i] == item
        print(f'Test for {i+2} OK')


# =====================
# Первоначальный вариант с 2мя вложенными циклами
def func_classic(n=99):
    result = [0] * 8
    for n in range(2, n+1):
        for i in range(2, 10):
            if n % i == 0:
                result[i-2] += 1
    return result

# test_func(func_classic)

# Я не захотел менять имя файла, поэтому вызывать timeit пришлось командой:
# python -m timeit -n 1 -s "tsk=__import__('Task 1')" "tsk.func_classic(10)"
# timeit:
# n = 10        100 loops, best of 3: 6.84 usec per loop
# n = 100       100 loops, best of 3: 72 usec per loop
# n = 1000      100 loops, best of 3: 739 usec per loop
# n = 10000     100 loops, best of 3: 7.57 msec per loop
# n = 100000    100 loops, best of 3: 76 msec per loop
# Вывод - похоже, что сложность алгоритма О(n)

# cProfile.run('func_classic(100000)')
# Нет рекурсии => не очень интересно
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.083    0.083 <string>:1(<module>)
#        1    0.083    0.083    0.083    0.083 Task 1.py:22(func_classic)
#        1    0.000    0.000    0.083    0.083 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of
#                                               '_lsprof.Profiler' objects}


# =====================
# Модифицированный вариант, где внутренний цикл раскрыт
def func_onecycle(n=99):
    result = [0] * 8
    for n in range(2, n+1):
        if n % 2 == 0:
            result[0] += 1
        if n % 3 == 0:
            result[1] += 1
        if n % 4 == 0:
            result[2] += 1
        if n % 5 == 0:
            result[3] += 1
        if n % 6 == 0:
            result[4] += 1
        if n % 7 == 0:
            result[5] += 1
        if n % 8 == 0:
            result[6] += 1
        if n % 9 == 0:
            result[7] += 1
    return result

# test_func(func_onecycle)

# timeit:
# n = 10        100 loops, best of 3: 4.25 usec per loop
# n = 100       100 loops, best of 3: 38.3 usec per loop
# n = 1000      100 loops, best of 3: 423 usec per loop
# n = 10000     100 loops, best of 3: 4.45 msec per loop
# n = 100000    100 loops, best of 3: 45.4 msec per loop
# Вывод: сложность алгоритма так же O(n), но меньше накладных расходов
# на создание внутреннего цикла

# cProfile.run('func_onecycle(100000)')
# Нет рекурсии => не очень интересно
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.047    0.047 <string>:1(<module>)
#        1    0.047    0.047    0.047    0.047 Task 1.py:59(func_onecycle)
#        1    0.000    0.000    0.047    0.047 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of
#                                               '_lsprof.Profiler' objects}


# =====================
# Алгоритм с рекурсией и циклом
# import sys # - для проверки при n>1000
# sys.setrecursionlimit(3000)
def func_hentai(n=99):
    if n == 1:
        return [0] * 8
    result = func_hentai(n-1)
    for i in range(2, 10):
        if n % i == 0:
            result[i-2] += 1
    return result

# test_func(func_hentai)

# Примечание: пришлось увеличить максимальную глубину рекурсии
# Но вызвать для числа больше 3000 не удалось
# Я увелчил глубину с помощью sys.setrecursionlimit(10000)
# Но, видимо, у меня переполняется максимальный размер стека
# Выделенного под Python
# Я пытался увеличить его с помощью threading.stack_size
# Но успехом это не увенчалось =(
# timeit:
# n = 10        100 loops, best of 3: 7.48 usec per loop
# n = 100       100 loops, best of 3: 80.5 usec per loop
# n = 1000      100 loops, best of 3: 949 usec per loop
# n = 2000      100 loops, best of 3: 2.02 msec per loop
# Вывод: и тут O(n), но накладные расходы ещё выше классического
# и по памяти ограничения присутствуют

# cProfile.run('func_hentai(1000)')
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.002    0.002 <string>:1(<module>)
#   1000/1    0.002    0.000    0.002    0.002 Task 1.py:106(func_hentai)
#        1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of
#                                               '_lsprof.Profiler' objects}
# Глубина рекурсии линейно зависит от переданного числа


# =====================
# Создадим алгоритм, похожий на классический, но с другим порядком циклов
def func_notbest(n=99):
    result = [0] * 8
    for i in range(2, 10):
        for num in range(2, n+1):
            if num % i == 0:
                result[i-2] += 1
    return result

# test_func(func_notbest)

# timeit:
# n = 10        100 loops, best of 3: 6.27 usec per loop
# n = 100       100 loops, best of 3: 45.7 usec per loop
# n = 1000      100 loops, best of 3: 546 usec per loop
# n = 10000     100 loops, best of 3: 5.54 msec per loop
# n = 100000    100 loops, best of 3: 56.1 msec per loop
# Вывод: алгоритм так же со сложностью O(n), только мы пробегаем
# по большому массиву (2, n) восемь раз, что менее выгодно по сравнению
# с классическим вариантом

# cProfile.run('func_notbest(100000)')
# Нет рекурсии => не очень интересно
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.056    0.056 <string>:1(<module>)
#        1    0.056    0.056    0.056    0.056 Task 1.py:144(func_notbest)
#        1    0.000    0.000    0.056    0.056 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of
#                                               '_lsprof.Profiler' objects}


# =====================
# Создадим плохой алгоритм, где сложность будет другой
def func_hochu_kvadrat(n=99):
    result = [0] * 8
    for num1 in range(2, n+1):
        for num2 in range(2, n+1):
            for i in range(2, 10):
                if num2 % i == 0:
                    result[i-2] += 1
        for i in range(2, 10):
            if num1 % i == 0:
                result[i-2] += 1
    for i in range(len(result)):
        result[i] = int(result[i] / n)
    return result

# test_func(func_hochu_kvadrat)

# timeit:
# n = 10        100 loops, best of 3: 107 usec per loop
# n = 100       100 loops, best of 3: 7.53 msec per loop
# n = 1000      100 loops, best of 3: 770 msec per loop
# n = 10000     1 loops, best of 3: 82.6 sec per loop
# Вывод: неожиданно оказалось, что этот алгоритм не просто плох,
# но и его сложность, судя по оценкам, O(n*n)

cProfile.run('func_notbest(100000)')
# Нет рекурсии => не очень интересно
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.063    0.063 <string>:1(<module>)
#        1    0.063    0.063    0.063    0.063 Task 1.py:143(func_notbest)
#        1    0.000    0.000    0.063    0.063 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of
#                                               '_lsprof.Profiler' objects}
