# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными),
# так и различаться.

import random

SIZE = 3
min_item = 0
max_item = 9
array = [random.randint(min_item, max_item) for _ in range(SIZE)]

if SIZE < 2:
    print('В массиве недостаточно элементов')
else:
    print(array)
    result_0 = array[0]
    result_1 = array[1]
    if result_0 > result_1:
        result_0, result_1 = result_1, result_0

    for i in range(2, SIZE):
        if array[i] < result_0:
            result_1 = result_0
            result_0 = array[i]
        elif array[i] < result_1:
            result_1 = array[i]

    print(f'Наименьшее значение {result_0}, следующее за ним {result_1}')
