print("Введите две срочные буквы английского алфавита")
ch1 = input("Введите первую строчную букву английского алфавита: ")
ch2 = input("Введите вторую строчную букву английского алфавита: ")
ch1_ord = ord(ch1)
ch2_ord = ord(ch2)
shift = ord('a') - 1
ch1_num = ch1_ord-shift
ch2_num = ch2_ord-shift
ch1_ch2_dist = abs(ch2_ord - ch1_ord - 1)
print(f"Номер первой буквы в алфавите {ch1_num}")
print(f"Номер второй буквы в алфавите {ch2_num}")
print(f"Количество букв между введёнными буквами {ch1_ch2_dist}")