# 9. Среди натуральных чисел, которые были введены,
# найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.


def dig_sum(m):
    if m > 9:
        return m % 10 + dig_sum(m // 10)
    else:
        return m


result = 0
max_sum = 0

while True:
    n = int(input("Введите натуральное число или 0 для выхода: "))
    if n == 0:
        print(f"Число {result}, сумма цифр {max_sum}")
        break
    else:
        cur_sum = dig_sum(n)
        if cur_sum > max_sum:
            max_sum = cur_sum
            result = n
