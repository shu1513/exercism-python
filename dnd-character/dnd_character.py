import random


def modifier(number):
    return (number - 10) // 2


class Character:
    @staticmethod
    def get_trait():
        dices = []

        for i in range(4):
            dices.append(random.randint(1, 6))
        dices.remove(min(dices))
        return sum(dices)

    def __init__(self):
        self.strength = Character.get_trait()
        self.dexterity = Character.get_trait()
        self.constitution = Character.get_trait()
        self.intelligence = Character.get_trait()
        self.wisdom = Character.get_trait()
        self.charisma = Character.get_trait()
        self.hitpoints = 10 + modifier(self.constitution)
