print("Введите три различных числа")
a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
c = float(input("Введите третье число: "))
if ((a > b) and (b > c)) or ((a < b) and (b < c)):
    print(b)
elif ((b > a) and (a > c)) or ((b < a) and (a < c)):
    print(a)
else:
    print(c)