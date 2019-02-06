# 2. Закодируйте любую строку из трех слов по алгоритму Хаффмана.

from collections import Counter, OrderedDict


class MyNode:
    def __init__(self, value, left, right, cnt):
        self.value = value
        self.left = left
        self.right = right
        self.cnt = cnt

s = input("Введите строку (желательно не очень длинную): ")

cnt = Counter(s)

print(cnt)
