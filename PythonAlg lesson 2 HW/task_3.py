# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр
# и вывести на экран. Например, если введено число 3486,
# то надо вывести число 6843.

n = int(input("Введите натуральное число: "))
result = 0
ostatok = n

while True:
    result = result * 10 + ostatok % 10
    ostatok = ostatok // 10
    if ostatok == 0:
        break

print(f"Число наоборот: {result}")
