# PracticalWork5.
# Организация многомодульной программы

import practicalWork5OneModul

# Перенос всех созданных функций в отдельный модуль
# Реализация логики игры
name_player1 = practicalWork5OneModul.input_players(1)
name_player2 = practicalWork5OneModul.input_players(2)
total_score = practicalWork5OneModul.game_dice(name_player1, name_player2)
practicalWork5OneModul.winner(name_player1, name_player2, total_score[0], total_score[1])
