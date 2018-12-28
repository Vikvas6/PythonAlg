# 3. В массиве случайных целых чисел поменять местами минимальный
# и максимальный элементы.

import random

SIZE = 3
min_item = 0
max_item = 2
array = [random.randint(min_item, max_item) for _ in range(SIZE)]

max_elem = array[0]-1
max_elem_pos = -1
min_elem = array[0]+1
min_elem_pos = -1

for i in range(SIZE):
    if array[i] > max_elem:
        max_elem = array[i]
        max_elem_pos = i
    if array[i] < min_elem:
        min_elem = array[i]
        min_elem_pos = i

if SIZE < 2:
    print('В массиве недостаточно элементов')
else:
    if min_elem == max_elem:
        print('Элементы в массиве равны')
    else:
        print('Изначальный массив:')
        print(array)
        array[min_elem_pos], array[max_elem_pos] = \
            array[max_elem_pos], array[min_elem_pos]
        print('Поменяли местами элементы:')
        print(array)
