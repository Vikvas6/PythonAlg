# 4. Определить, какое число в массиве встречается чаще всего.

import random

SIZE = 10
min_item = 0
max_item = 3
array = [random.randint(min_item, max_item) for _ in range(SIZE)]

num_counts = {}

for i in array:
    if i in num_counts:
        num_counts[i] += 1
    else:
        num_counts[i] = 1

result_cnt = 0
number = None
for i in num_counts:
    if num_counts[i] > result_cnt:
        result_cnt = num_counts[i]
        number = i

print("Определяем самое частое число в массиве:")
print(array)
# print(num_counts)

# None и 0 - не одно и тоже
if number == 0 or number:
    print(f'В массиве чаще всего встречается число {number}')
else:
    print(f'Похоже, массив пуст')
