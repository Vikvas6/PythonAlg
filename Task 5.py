# 5. В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.

import random

SIZE = 10
min_item = -10
max_item = 10
array = [random.randint(min_item, max_item) for _ in range(SIZE)]

# Zero-based
pos = -1
result = 0
for i in range(SIZE):
    if array[i] < 0 and (result == 0 or array[i] > result):
        result = array[i]
        pos = i

print("Ищем максимальный отрицательный элемент в массиве:")
print(array)

if pos > -1:
    print(f'Максимальный отрицательный элемент {result} '
          f'находится на позиции {pos} (считая с 0)')
else:
    print('В массиве нет отрицательных чисел')
