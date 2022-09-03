import random
from array import array


class Army:
    class Сharacter:
        """базовый класс персонажа"""

        def __init__(self, name, attack, accuracy, dodge, hp):
            """Constructor"""
            self.name = name
            self.attack = attack
            self.accuracy = accuracy
            self.dodge = dodge
            self.hp = hp

        def say_name(self):
            print(self.name)

        def info(self):
            print('Класс ' + self.name)
            print("Атака: %s" % self.attack)
            print("Меткость: %s" % self.accuracy)
            print("Уклонение: %s" % self.dodge)
            print("HP: %s" % self.hp)

        def attacking(self):
            return self.attack

        def dodging(self):
            return self.dodge


if __name__ == "__main__":
    # Инициализация персонажей
    war = Army.Сharacter("War", 5, 4, 2, 10)
    mag = Army.Сharacter("Mag", 2, 10, 2, 8)
    archer = Army.Сharacter("Archer", 7, 3, 5, 10)

    # Комп выбрал персонажей
    Player1 = [war, mag, archer]
    Comp = [war, mag, archer]

    # Битва

    # Выбор персонажа Player1 (пока он всегда первый)
    warrior_point = Player1[random.randint(0, 2)]
    print('В битву вступает %s' % warrior_point.name)
    # Выбор по кому будет бить
    warrior_point = Comp[random.randint(0, 2)]
    print('Собирается нападать на %s' % warrior_point.name)
    # Вычисляем меткость
    chanse_acc = warrior_point.accuracy
    print(random.randint(2, 5))


    # Если попал - расчёт урона

    # Не попал



    # print('Приветствую! Это игра матч-арена фэнтезийных персонажей. Собери самый эффективный отряд из трёх персонажей '
    #       'и вступи в битву!')
    # print('Доступны следующие персонажи:')
    # war.say_name()
    # mag.say_name()
    # archer.say_name()

# тут будет код выбора персонажей
