class Monster():
    def __init__(self, name, where):
        self.name = name
        self.where = where
    def attack(self):
        pass
    def __str__(self):
        return f"This is {self.name} and it lives in {self.where}"

class Vampire(Monster):
    def __init__(self, name, where):
        super().__init__(name, where)

    def attack():
        return f"Dracula bites  your neck..."

class Troll(Monster):
    def __init__(self, name, where):
        super().__init__(name, where)

    def attack():
        return f"Dave swings his wooden club at your head..."

class Skeleton(Monster):
    def __init__(self, name, where):
        super().__init__(name, where)

    def attack():
        return f"Sam swings at you with his sword..."

class Dragon(Monster):
    def __init__(self, name, where):
        super().__init__(name, where)
        
    def attack():
        return f"Smaug melts yourr armor by breathing fire..."
    
print(Vampire("Dracula", "Pensylvania"))
print(Vampire.attack())
print()

print(Troll("Dave", "Cave"))
print(Troll.attack())
print()

print(Skeleton("Sam", "Dungeon"))
print(Skeleton.attack())
print()

print(Dragon("Smaug", "Lonely Mountain"))
print(Dragon.attack())
print()
