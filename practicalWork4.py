# PracticalWork4.
# Применение операторов ветвления и циклов

# 1. код, реализующий ядро игры
from random import randint
import time

totalScore1 = 0
totalScore2 = 0
# Ввод имен играющих
igrok1: str = input('Введите имя 1-го играющего ')
igrok2: str = input('Введите имя 2-го играющего ')
for i in range(5):
    # Моделирование бросания кубика первым играющим
    print('Кубик бросает', igrok1)
    time.sleep(2)
    n1 = randint(1, 6)
    print('Выпало:', n1)
    totalScore1 += n1

    # Моделирование бросания кубика вторым играющим
    print('Кубик бросает', igrok2)
    time.sleep(2)
    n2 = randint(1, 6)
    print('Выпало:', n2)
    totalScore2 += n2

# 2. определение победителя игры
print('Итого очков ', igrok1, ': ', totalScore1)
print('Итого очков ', igrok2, ': ', totalScore2)
if totalScore1 > totalScore2:
    print('Выиграл ', igrok1)
elif totalScore1 < totalScore2:
    print('Выиграл ', igrok2)
else:
    print('Ничья')