# Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100). Выведите на экран
# исходный и отсортированный массивы. Сортировка должна быть реализована в
# виде функции. По возможности доработайте алгоритм (сделайте его умнее).

import random

SIZE = 100
MIN_VAL = -100  # Включая
MAX_VAL = 99  # Включая

array = [random.randint(MIN_VAL, MAX_VAL) for _ in range(SIZE)]

print(f'Исходный массив:        {array}')


def puzyr_sort(array):
    n = 1
    while n < len(array):
        for i in range(len(array) - n):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]

        n += 1

puzyr_sort(array)
print(f'Отсортированный массив: {array}')
