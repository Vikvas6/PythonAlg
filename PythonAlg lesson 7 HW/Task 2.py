# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный
# массив, заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.

import random

SIZE = 10
MIN_VAL = 0  # Включая
MAX_VAL = 50  # Исключая

# array = [random.random()*(MAX_VAL - MIN_VAL)+MIN_VAL for _ in range(SIZE)]
array = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

print(f'Исходный массив:        {array}')


def merge(array1, array2):
    return array1 + array2


def merge_sort(array):
    if len(array) <= 1:
        return array

    s_ar = []
    l_ar = []
    mid = len(array) // 2
    for i in range(mid):
        s_ar.append(array[i])
    i += 1
    while i < len(array):
        l_ar.append(array[i])
        i += 1

    return merge(merge_sort(s_ar), merge_sort(l_ar))

print(merge_sort(array))
