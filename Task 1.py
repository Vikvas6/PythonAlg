# 1. Подсчитать, сколько было выделено памяти под переменные в ранее
# разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее
# эффективным использованием памяти.
# Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
# вариантов кода для одной и той же задачи. Результаты анализа вставьте в виде
# комментариев к коду. Также укажите в комментариях версию Python и
# разрядность вашей ОС.

# Я взял ту же задачу, что и для ДЗ урока 4, информационные комментарии оттуда
# оставил, но комментарии по поводу использования памати я удалил.
# Разрядность моей системы - 64 бита.
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
# Новое дополнение для выполнения ДЗ урока 6:
# 1) n будет всё время равно 100
# 2) все функции переписаны для использования переменных из одного глобального
# списка - чтобы можно было один раз посчитать затраченную память
#
# Я использую глобально определённый список, в который и буду загонять свои
# переменные, в функции test_func я так же добавил подсчёт количества памати,
# занятого переменными в этом массиве.
# Важное замечание - я не учитываю переменную, которую передают
# на вход функции (статически +28 байт).

import sys

# Я заранее заполнил этот массив каким-то количество пустых значений
# (память на None объекты я не учитываю), не хотелось сохранять
# так же указатель на конец массива в начале каждого алгоритма
# (в одном всё же пришлось сохранить).
variables_list = []
for i in range(5):
    variables_list.append(None)


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
    print(f'Total size: {show_size(variables_list)}')


def show_size(x, level=0):
    size = 0
    if level > 0 and x is not None:
        size = sys.getsizeof(x)
    print('\t' * level,
          f'type = {type(x)}, size = {sys.getsizeof(x)}, object = {x}')
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items:
                size += show_size(key, level + 1)
                size += show_size(value, level + 1)
        elif not isinstance(x, str):
            for item in x:
                size += show_size(item, level + 1)
    return size


# =====================
# Первоначальный вариант с 2мя вложенными циклами
def func_classic(n=99):
    variables_list[0] = [0] * 8
    for variables_list[1] in range(2, n+1):
        for variables_list[2] in range(2, 10):
            if variables_list[1] % variables_list[2] == 0:
                variables_list[0][variables_list[2]-2] += 1
    return variables_list[0]

# test_func(func_classic)
# Создаётся массив на 8 объектов типа int, а так же 2 счётчика циклов,
# тоже типа int, что в сумме дало 408 байт.


# =====================
# Модифицированный вариант, где внутренний цикл раскрыт
def func_onecycle(n=99):
    variables_list[0] = [0] * 8
    for variables_list[1] in range(2, n+1):
        if variables_list[1] % 2 == 0:
            variables_list[0][0] += 1
        if variables_list[1] % 3 == 0:
            variables_list[0][1] += 1
        if variables_list[1] % 4 == 0:
            variables_list[0][2] += 1
        if variables_list[1] % 5 == 0:
            variables_list[0][3] += 1
        if variables_list[1] % 6 == 0:
            variables_list[0][4] += 1
        if variables_list[1] % 7 == 0:
            variables_list[0][5] += 1
        if variables_list[1] % 8 == 0:
            variables_list[0][6] += 1
        if variables_list[1] % 9 == 0:
            variables_list[0][7] += 1
    return variables_list[0]

# test_func(func_onecycle)
# Так же создаётся массив на 8 объектов типа int,но счётчик только один,
# в сумме дало 380 байт.


# =====================
# Алгоритм с рекурсией и циклом
# import sys # - для проверки при n>1000
# sys.setrecursionlimit(3000)
def func_hentai(n=99):
    if n == 1:
        return [0] * 8
    davaite_predstavim_chto_tyt_pusto_ya_ne_hochu_uchitivat_etu_peremennuyu = len(variables_list)
    variables_list.append(func_hentai(n-1))
    variables_list.append(None)
    for variables_list[davaite_predstavim_chto_tyt_pusto_ya_ne_hochu_uchitivat_etu_peremennuyu+1] in range(2, 10):
        if n % variables_list[davaite_predstavim_chto_tyt_pusto_ya_ne_hochu_uchitivat_etu_peremennuyu+1] == 0:
            variables_list[davaite_predstavim_chto_tyt_pusto_ya_ne_hochu_uchitivat_etu_peremennuyu][variables_list[davaite_predstavim_chto_tyt_pusto_ya_ne_hochu_uchitivat_etu_peremennuyu+1]-2] += 1
    return variables_list[davaite_predstavim_chto_tyt_pusto_ya_ne_hochu_uchitivat_etu_peremennuyu]

# test_func(func_hentai)
# ОООООООООчень много переменных, 34 тысячи байт!!! (34524).
# Итого, я рекурсию люблю все меньше и меньше (до Вашего курса я её любил...)


# =====================
# Создадим алгоритм, похожий на классический, но с другим порядком циклов
def func_notbest(n=99):
    variables_list[0] = [0] * 8
    for variables_list[1] in range(2, 10):
        for variables_list[2] in range(2, n+1):
            if variables_list[2] % variables_list[1] == 0:
                variables_list[0][variables_list[1]-2] += 1
    return variables_list[0]

# test_func(func_notbest)
# То же самое, что и в первой функции - 408 байт.


# =====================
# Создадим плохой алгоритм, где сложность будет другой
def func_hochu_kvadrat(n=99):
    variables_list[0] = [0] * 8
    for variables_list[1] in range(2, n+1):
        for variables_list[2] in range(2, n+1):
            for i in range(2, 10):
                if variables_list[2] % i == 0:
                    variables_list[0][i-2] += 1
        for i in range(2, 10):
            if variables_list[1] % i == 0:
                variables_list[0][i-2] += 1
    for i in range(len(variables_list[0])):
        variables_list[0][i] = int(variables_list[0][i] / n)
    return variables_list[0]

# test_func(func_hochu_kvadrat)
# Не смотря на другую сложность алгоритма, счётчиков циклов используется
# столько же, поэтому всё те же 408 байт.

# На основании моей работы можно сделать вывод, что если Вы не используете
# рекурсию, то у вас отличный с точки зрения памяти алгоритм.
# P.S.: Вывод делаю чисто на основании выбранной задачи, лично я не настолько
# категоричен - думаю, есть много способов оптимизации в том числе и рекурсии.
