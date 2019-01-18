# 1. Пользователь вводит данные о количестве предприятий, их наименования и
# прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
# Программа должна определить среднюю прибыль (за год для всех предприятий) и
# вывести наименования предприятий, чья прибыль выше среднего и отдельно
# вывести наименования предприятий, чья прибыль ниже среднего.

from collections import namedtuple

n = int(input("Введите количество предприятий: "))
Department = namedtuple("Department", "name q1 q2 q3 q4 sum")
departments = []
total_sum = 0
for i in range(n):
    name = input(f"Введите имя предприятия номер {i+1}: ")
    q1, q2, q3, q4 = input("Введите прибыль за 4 квартала "
                           "(через пробел): ").split(" ")
    cur_sum = int(q1) + int(q2) + int(q3) + int(q4)
    department = Department(name, int(q1), int(q2), int(q3), int(q4), cur_sum)
    total_sum += cur_sum
    departments.append(department)

avg_for_all_per_year = total_sum/n
print(f"Средняя прибыль за год для всех предприятий {avg_for_all_per_year}")

b_equals = True
for i in range(len(departments)):
    if departments[i].sum != avg_for_all_per_year:
        b_equals = False
        break

if not b_equals:
    print("Прибыль следующих предприятий выше среднего:")
    for i in range(len(departments)):
        if departments[i].sum > avg_for_all_per_year:
            print(departments[i].name)

    print("*********типа отдельно**********")
    print("Прибыль следующих предприятий ниже среднего:")
    for i in range(len(departments)):
        if departments[i].sum < avg_for_all_per_year:
            print(departments[i].name)
else:
    print("У всех предприятий одинаковая средняя прибыль")
