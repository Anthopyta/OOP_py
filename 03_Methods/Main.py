class Hero:  # template
    # class variable / static variable
    jumlah = 0

    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        # instance variable
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlah += 1
        
    # void function, methos tanpa return
    def siapa(self):
      print("namaku adalah " + self.name)
    
    # method dengna argumen 
    def healthUp(self, up):
      self.health += up
    
    # method dengan return 
    def getHelth(self):
      return self.health


hero1 = Hero("Sniper", 100, 10, 4)
hero2 = Hero("Mirana", 100, 15, 1)

hero1.siapa()
hero1.healthUp(10)

print(hero1.getHelth())



