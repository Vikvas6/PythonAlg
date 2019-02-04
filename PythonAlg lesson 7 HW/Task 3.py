# 3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным
# образом. Найдите в массиве медиану. Медианой называется элемент ряда,
# делящий его на две равные части: в одной находятся элементы, которые
# не меньше медианы, в другой – не больше медианы. Задачу можно решить
# без сортировки исходного массива. Но если это слишком сложно, то используйте
# метод сортировки, который не рассматривался на уроках.


import random

M_SIZE = 3
MIN_VAL = 0  # Включая
MAX_VAL = 10  # Включая

# Т.к. разницы особой нет, для наглядности заполним целыми числами
array = [random.randint(MIN_VAL, MAX_VAL) for _ in range(2 * M_SIZE + 1)]
print(f"Исходный массив {array}")

# Идея в том, что нам надо найти m'ый по величине элемент массива
# (считая от 0), поэтому полную сортировку проводить не надо
# Возьмём случайный элемент, создадим массивы из элементов больше и меньше
# выбранного, а затем будем в этих массивах искать нужный по порядку элемент


def get_nth_value(array, n):
    if len(array) == 1:
        return array[0]
    item_rnd = random.choice(array)
    s_ar = []
    l_ar = []
    m_ar = []
    for item in array:
        if item < item_rnd:
            s_ar.append(item)
        elif item > item_rnd:
            l_ar.append(item)
        else:
            m_ar.append(item)
    if len(s_ar) - 1 < n and len(s_ar) + len(m_ar) > n:
        return item_rnd
    elif len(s_ar) > n:
        return get_nth_value(s_ar, n)
    else:
        return get_nth_value(l_ar, n - len(s_ar) - len(m_ar))

print(f"Медиана {get_nth_value(array, M_SIZE)}")
