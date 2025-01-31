class NamePerson:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        
    def status(self):
            print(f"Имя персонажа {self.name}. Здоровье персонажа {self.health}")

class Hero(NamePerson):
    def __init__(self, name, health, strength):
        super().__init__(name, health)
        self.strength = strength
    
    def attack(self):
        print(f"Воин атакует с силой {self.strength}")
    
    def status(self):
            print(f"Имя героя {self.name}. Здоровье персонажа {self.health}. Сила персонажа {self.strength}")
        
        
class Magician(NamePerson):
    def __init__(self, name, health, magic):
        super().__init__(name, health)
        self.magic = magic
    
    def spell(self):
        print(f"Маг накидывает заклинание с силой {self.magic}")
        
    def status(self):
            print(f"Имя мага {self.name}. Здоровье персонажа {self.health}. Сила магии мага {self.magic}")
        
namePerson = [NamePerson("Stickman",500), Hero("Геркулес",200,150), Magician("Гарри поттер",350,300)]

for i in namePerson:
    i.status()
    if isinstance(i, Hero):
        i.attack()
    elif isinstance(i, Magician):
        i.spell()
