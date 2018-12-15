year = int(input("Введите год: "))
if year % 400 == 0:
    print("Этот год високосный")
elif year % 100 == 0:
    print("Этот год не високосный")
elif year % 4 == 0:
    print("Этот год високосный")
else:
    print("Этот год не високосный")