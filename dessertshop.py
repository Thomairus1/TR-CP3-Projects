from dessert import DessertItem, Candy, Cookie, IceCream, Sundae
class Order():
    def __init__(self):
        self.order = []
    def add(self, dessertitem):
        self.order.append(dessertitem)
    def __len__(self):
        return len(self.order)
    
def main():
    order1 = Order()
    order1.add(Candy("Candy Corn", 1.5, .25))
    print("Candy Corn")
    order1.add(Candy("Gummy Bears", .25, .35))
    print("Gummy Bears")
    order1.add(Cookie("Chocolate Chip", 6, 3.99))
    print("Chocolate Chip")
    order1.add(IceCream("Pistachio", 2, .79))
    print("Pistachio")
    order1.add(Sundae("Vanilla", 3, .69, "Hot Fudge", 1.29))
    print("Vanilla")
    order1.add(Cookie("Oatmeal Raisin", 2, 3.45))
    print("Oatmeal Raisin")
    print(f"Total number of items in order: {order1.__len__()}")

main()