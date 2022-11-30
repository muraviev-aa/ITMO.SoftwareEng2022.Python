# PracticalWork5.
# Реализация всех функций в одном модуле

from random import randint
import time


# Имена игроков
def input_players(num):
    print('Имя {:d}-го игрока '.format(num))
    return input()


# Бросают кубик
def throws(name_player):
    print('Кубик бросает', name_player)
    time.sleep(2)
    points = randint(1, 6)
    print('Выпало:', points)
    return points


# Функция (ядро игры)
def game_dice(name_player1, name_player2):
    num_of_throws = int(input("Укажите количество бросков\n"))
    total_score1 = 0
    total_score2 = 0
    for i in range(num_of_throws):
        print('Шаг игры ', i + 1)
        total_score1 += throws(name_player1)
        total_score2 += throws(name_player2)
    print(name_player1, 'очки: ', total_score1)
    print(name_player2, 'очки: ', total_score2)
    return [total_score1, total_score2]


# Победитель с помощью функции
def winner(name_player1, name_player2, total_score1, total_score2):
    if total_score1 > total_score2:
        print('Выиграл ', name_player1)
    elif total_score1 < total_score2:
        print('Выиграл ', name_player2)
    else:
        print('Ничья')