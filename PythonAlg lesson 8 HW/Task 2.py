# 2. Закодируйте любую строку из трех слов по алгоритму Хаффмана.

from collections import Counter


class MyNode:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def __repr__(self):
        return f"(Node: left {self.left}, right {self.right})"

    def fill_dict(self, path, cdict):
        if type(self.left).__name__ == "str":
            cdict[self.left] = path + '0'
        else:
            self.left.fill_dict(path+'0', cdict)
        if type(self.right).__name__ == "str":
            cdict[self.right] = path + '1'
        else:
            self.right.fill_dict(path+'1', cdict)

s = input("Введите строку (желательно не очень длинную): ")


def code(s):
    cnt = Counter(s)

    while len(cnt) > 1:
        last = cnt.most_common()[:-3:-1][0]
        pre_last = cnt.most_common()[:-3:-1][1]
        node = MyNode(last[0], pre_last[0])
        count = last[1] + pre_last[1]
        cnt.pop(last[0])
        cnt.pop(pre_last[0])
        cnt[node] += count

    code_dict = dict()
    cnt.popitem()[0].fill_dict("", code_dict)

    result = ""
    for i in s:
        result += code_dict[i] + " "

    return code_dict, result


def uncode(code_dict, s):
    uncode_dict = {}
    for key in code_dict.keys():
        uncode_dict[code_dict[key]] = key

    result = ""
    for i in s.split(" ")[:-1]:  # -1 т.к. последний элемент будет ''
        result += uncode_dict[i]

    return result

code_dict, result = code(s)
print(f"Словарь для кодирования: {code_dict}")
print(f"Закодированная строка: {result}")
result = uncode(code_dict, result)
print(f"Раскодированная строка: {result}")
