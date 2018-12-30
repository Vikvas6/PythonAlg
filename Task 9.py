# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random

SIZE_ROWS = 4
SIZE_COLUMNS = 5
min_item = 0
max_item = 9

# Только так у меня IDE перестала ругаться на нарущение PEP8 =(
matrix = [
            [random.randint(min_item, max_item) for _ in range(SIZE_COLUMNS)]
            for _ in range(SIZE_ROWS)]

for i in matrix:
    print(i)

max_elems = [matrix[0][i] for i in range(SIZE_COLUMNS)]
for i in range(SIZE_ROWS):
    for j in range(SIZE_COLUMNS):
        if matrix[i][j] < max_elems[j]:
            max_elems[j] = matrix[i][j]

result = max_elems[0]
for i in max_elems:
    if i > result:
        result = i

print(f"Максимальный среди минимальных элементов столбцов равен {result}")
