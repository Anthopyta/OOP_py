class Hero:
  
  def __init__(self, name, health, attackPower):
    self.__name = name
    self.__health = health
    self.__attPower = attackPower
    
  # getter
  def getName(self):
    return self.__name
  
  def getHealth(self):
    return self.__health
  
  # setter
  def attacked(self, attackedPower):
    self.__health -= attackedPower
  
  def setAttPower(self, basicAttack):
    self.__attPower = 50
    basicAttack += self.__attPower
  



# start game
earthShaker = Hero("Earth Shaker", 50, 5)

# workflow
print(earthShaker.getName())
print(earthShaker.getHealth())
earthShaker.attacked(5)
print(earthShaker.getHealth())
