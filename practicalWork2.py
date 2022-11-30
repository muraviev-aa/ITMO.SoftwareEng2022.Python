# PracticalWork2.
# Working with data

# Working with strings
# 1.
string1 = 'This is a string.     '
string2 = '     This is another string.'
# 2.
print('Concatenation: ' + string1 + ' ' + string2)
# 3.
print('String1 length: ', len(string1))
print('lower(): ' + string2.lower())
print('title(): ' + string2.title())
print('upper(): ' + string1.upper())
print('rstrip(): ' + string1.rstrip())
print('lstrip(): ' + string2.lstrip())
print('strip()' + string1.strip())
print('strip("0")' + string2.strip('T, g.'))
# Extracting characters and substrings
# 4.
d = 'qwertyuiop[]'

ch = d[2]
print(d[4] + ' ' + ch)
# 5. Slicing
chm = d[1: 3]
print(chm)
# 6.
print(d[1:])
print(d[:3])
print(d[:])
print(d[1:5:2])
# 7.
# d[2] = 'o'    !!! Error: 'str' object does not support item assignment !!!

# Working with numbers
# 1.
a = 251
b = 25
# 2.
print(a / b)
print(a // b)
print(b / a)
print(a % b)
print(b ** a)
# 3.
# param = 'string' + 123    !!! Error: can only concatenate str (not "int") to str !!!
param = 'string' + str(555)
print(param)

# Data Conversion
# 1.
param = 'string' + str(555)
print(param)

# 2.
n1 = input('Enter the first number:')
n2 = input('Enter the second number:')
n3 = float(n1) + float(n2)
print(n1 + ' plus ' + n2 + ' = ', n3)

# String format
# 2.
a = 1 / 3
print("{:7.3f}".format(a))
# 3.
a = 2 / 3
b = 2 / 9
print("{:7.3f} {:7.3f}".format(a, b))
print("{:10.3e} {:10.3e}".format(a, b))
# 4.
print(n1 + ' plus ' + n2 + ' = ', '{:10.3f}'.format(n3))

# Списки

list2 = [82, 8, 23, 97, 92, 44, 17, 39, 11, 12]
# print(dir(list2))
# dir(list2)
#
help(list2.insert)
""" insert(index, object, /) метод экземпляра встроенного списка.
Вставить объект перед индексом.
"""
help(list2.append)
""" append(object, /) метод экземпляра встроенного списка.
Добавить объект в конец списка.
"""
help(list2.sort)
""" sort(*, key=None, reverse=False)
метод экземпляра встроенного списка.
Отсортируйте список в порядке возрастания и верните None.
Сортировка оперативная (т.е. сам список изменяется) и стабильная (т.е.
сохраняется порядок двух равных элементов).
Если дана ключевая функция, примените ее один раз к каждому элементу списка и отсортируйте их,
по возрастанию или по убыванию, в соответствии со значениями их функций.
Флаг реверса может быть установлен для сортировки в порядке убывания.
"""
help(list2.remove)
""" remove(value, /) метод экземпляра встроенного списка.
Удалить первое вхождение значения.
Вызывает ValueError, если значение отсутствует.
"""
help(list2.reverse)
"""reverse() метод экземпляра встроенного списка.
Реверс *НА МЕСТЕ*.
"""
list2 = [82, 8, 23, 97, 92, 44, 17, 39, 11, 12]
list2[4] = 8
# list2 = [82, 8, 23, 97, 8, 44, 17, 39, 11, 12]
list2.append(99)
# list2 = [82, 8, 23, 97, 8, 44, 17, 39, 11, 12, 99]
list2.insert(1, 13)
# list2 = [82, 13, 8, 23, 97, 8, 44, 17, 39, 11, 12, 99]
list2.pop(3)
# list2 = [82, 13, 8, 97, 8, 44, 17, 39, 11, 12, 99]
list2.pop(len(list2) - 1)
# list2 = [82, 13, 8, 97, 8, 44, 17, 39, 11, 12]
print(list2)

# Сортировка элементов списка
list2.sort(reverse=True)
print(list2)
#
list2_2 = [3, 5, 6, 2, 33, 6, 11]
lis = sorted(list2_2)
print(lis)

# Кортежи (tuple)
help(dir(tuple))
help(tuple.index)
"""index(self, value, start=0, stop=9223372036854775807, /)
Возвращает первый индекс значения.
Вызывает ValueError, если значение отсутствует.
"""
help(tuple.count)
"""count(self, value, /)
Возвращает количество вхождений значения.
"""
seq = (2, 8, 23, 97, 92, 44, 17, 39, 11, 12)
print(seq.count(8))
# 1
print(seq.index(44))
# 5
listseq = list(seq)
print(type(listseq))
# <class 'list'>
print(listseq)
listseq.sort()
# [2, 8, 23, 97, 92, 44, 17, 39, 11, 12]
listseq.insert(9, 1)
# [2, 8, 11, 12, 17, 23, 39, 44, 92, 1, 97]
print(listseq)

# Словари
D = {"food": "Apple", "quantity": 4, "color": "Red"}
print(D["food"])
D["quantity"] += 10
print(D["quantity"])
dp = {}
dp["name"] = input("Введите название: ")
dp["age"] = input("Введите возраст: ")
print(dp)

# Вложенность хранения данных
rec = {"name": {"firstname": "Bob", "lastname": "Smith"}, "job": ["dev", "mgr"], "age": 25}
print(rec["name"]["firstname"], rec["name"]["lastname"])
# Bob Smith
print(rec["name"]["firstname"])
# Bob
print(rec["job"])
# ['dev', 'mgr']
rec["job"].append("janitor")
print(rec["name"]["firstname"], rec["name"]["lastname"], rec["job"], rec["age"])
# Bob Smith ['dev', 'mgr', 'janitor'] 25
