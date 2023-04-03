class Hero:
  
  # class variabel 
  jumlab = 0
  def __init__(self, name, health):
    self.name = name
    self.health = health
    
    # variabel instance private
    self.__private = "private"
    # variabel instance protected
    self._protected = "protected"
    
lina = Hero("lina", 100)

print(lina.__dict__)
print(Hero.__dict__)
print(Hero.__privateJumlah__)