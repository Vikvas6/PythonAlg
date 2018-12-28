# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны
# любому из чисел в диапазоне от 2 до 9.

result = [0] * 8
for n in range(2, 100):
    for i in range(2, 10):
        if n % i == 0:
            result[i-2] += 1

print('Количество чисел из диапазона 2-99, кратных числам из диапазона 2-9:')
for i in range(2, 10):
    print(f'Числу {i} кратно {result[i-2]} чисел из диапазона 2-99')
