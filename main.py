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


if __name__ == "__main__":ч
    war = Сharacter("War", 5, 4, 2, 10)
    mag = Сharacter("Mag", 2, 10, 2, 8)
    archer = Сharacter("Archer", 7, 3, 5, 10)
    print('Приветствую! Это игра матч-арена фэнтезийных персонажей. Собери самый эффективный отряд из трёх персонажей '
          'и вступи в битву!')
    print('Доступны следующие персонажи:')
    war.say_name()
    mag.say_name()
    archer.say_name()

# тут будет код выбора персонажей


