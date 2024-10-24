from dessert import DessertItem, Candy, Cookie, IceCream, Sundae

def test_candy_init():
    candy = Candy("Chocolate", 3.5, 1.5)
    name = candy.get_name()
    assert name == "Chocolate"