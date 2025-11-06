#Исключения и обработка ошибок в ООП-программах

import random

#Пользвательское исключение для проигрыша
class BangExeception(Exception):
    pass

#Class Револьвера

class Revolver:
    def __init__(self , chambers=6):
        self.chambers = chambers
        self.bullet_position = random.randint(1, chambers)
        self.current_position = 1

    def pull_trigger(self):
        if self.current_position == self.bullet_position:
            raise BangExeception('Бум! патрон выстрелил')
        else:
            print('Щелк! Пусто.')
        self.current_position = (self.current_position %  self.chambers) + 1


class Player:
    def __init__(self, name, revolver):
        self.name = name
        self.revolver = revolver
    
    def shoot(self):
        try:
            print(f'{self.name} стреляет....')
            self.revolver.pull_trigger()
        except BangExeception as e:
            print(f'{self.name} проиграл! {e}')
            return True #Проигрыш
        return False #Промах

def play_game(players):
    game_over = False
    while not game_over:
        for player in players:
            game_over = player.shoot()
            if game_over:
                break

revolver = Revolver()
players = [
    Player('Адэлина', revolver),
    Player('Диана', revolver),
    Player('Эльнара', revolver),
    Player('Айгээрим', revolver),
    Player('Аида', revolver),
    Player('Кутман', revolver),
    Player('Батма', revolver),
]

play_game(players)