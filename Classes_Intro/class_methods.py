
class Pokemon:
    def __init__(self, name, hp, typ, lvl):
        self.name = name
        self.hp = hp
        self.typ = typ
        self.lvl = lvl
    def combat(self, other):
        if self.lvl > other.lvl:
            return f"{self.name} won!"
        elif self.lvl < other.lvl:
            return f"{other.name} has defeated you!"
        else:
            return f"{self.name} and {other.name} are too exhausted to fight. You both lose."    
    def __str__(self):
        return(f"""
               name: {self.name},
               type: {self.typ},
               level: {self.lvl},
               HP: {self.hp}
        """)
    #add @classmethod used to keep method from changing object instances!
    def lvl_up(self):
        self.lvl += 1
        self.hp = int(self.hp*1.5)
    
    @classmethod
    def pikachu(self):
        return Pokemon(input("Give me a name "), 50, "Electric", 1)
    #static methods do not require self or class
    @staticmethod
    def hp_update(poke):
        return poke.hp - 5
    
eevee = Pokemon("Jayrod", 37, "normal", 2)

pika = Pokemon.pikachu()
pika.hp = Pokemon.hp_update(pika)
print(pika)