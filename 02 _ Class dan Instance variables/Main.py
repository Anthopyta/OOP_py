class Hero:  # template
    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor


hero1 = Hero("Sniper", 100, 10, 4)
hero2 = Hero("Mirana", 100, 15, 1)

print(hero1.__dict__)
print(hero2.__dict__)
