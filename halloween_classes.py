class Monster():
    def __init__(self, name, where):
        self.name = name
        self.where = where
    def attack(self, other):
        if self.attack > other.attack:
            print(f"{self.name} won against {other.name}!")
        elif other.attack > self.attack:
            print(f"{other.name} won against {self.name}!")

class Vampire(Monster):
    def __init__(self, name, where, attack):
        super().__init__(name, where)
        self.attack = attack
    how_attack = "bites neck"

class Troll(Monster):
    def __init__(self, name, where, attack):
        super().__init__(name, where)
        self.attack = attack
    how_attack = "swings with club"

class Skeleton(Monster):
    def __init__(self, name, where, attack):
        super().__init__(name, where)
        self.attack = attack
    how_attack = "swings sword"

class Dragon(Monster):
    def __init__(self, name, where, attack):
        super().__init__(name, where)
        self.attack = attack
    how_attack = "breathes fire"

vampire1 = Vampire("Dracula", "Pensylvania", 15)

troll1 = Troll("Dave", "Cave", 10)

skeleton1 = Skeleton("Sam", "Dungeon", 12)

dragon1 = Dragon("Smaug", "Lonely Mountain", 25)
