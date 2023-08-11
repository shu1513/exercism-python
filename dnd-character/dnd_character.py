import random


def modifier(number):
    return (number - 10) // 2


class Character:
    @staticmethod
    def ability():
        dices = []

        for i in range(4):
            dices.append(random.randint(1, 6))
        dices.remove(min(dices))
        return sum(dices)

    def __init__(self):
        self.strength = Character.ability()
        self.dexterity = Character.ability()
        self.constitution = Character.ability()
        self.intelligence = Character.ability()
        self.wisdom = Character.ability()
        self.charisma = Character.ability()
        self.hitpoints = 10 + modifier(self.constitution)
