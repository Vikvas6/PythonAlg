# 8. Посчитать, сколько раз встречается определенная цифра в введенной
# последовательности чисел. Количество вводимых чисел и цифра, которую
# необходимо посчитать, задаются вводом с клавиатуры.


def find_dig(m, dig):
    result = 0
    ostatok = m

    while True:
        if ostatok % 10 == dig:
            result += 1

        ostatok = ostatok // 10

        if ostatok == 0:
            break

    return result


num_cnt = int(input("Сколько чисел Вы хотите ввести? "))
dig_to_find = int(input("Какую цифру Вы хотите найти? "))
loop_cnt = 0
result = 0

while True:
    if loop_cnt < num_cnt:
        n = int(input("Введите натуральное число: "))
        result += find_dig(n, dig_to_find)
        loop_cnt += 1
    else:
        break
print(f"Количество цифр {dig_to_find} равно {result}")
