class FoodOrder:
    def __init__(self, drink, appt, main, side1, side2, dessert):
        self.drink = drink 
        self.appt = appt
        self. main = main
        self.side1 = side1
        self.side2 = side2
        self.dessert = dessert
    def __str__(self):
        return (f"""
                Drink: {self.drink} 
                Appetizer: {self.appt}
                Main Course: {self.main}
                Side One: {self.side1}
                Side Two: {self.side2}
                Dessert: {self.dessert}
        """)
    
order1 = FoodOrder("Coke", "Crab cakes", "Double cheeseburger", "Fries", "Onion Rings", "Cheesecake")

print(order1)

menu_dict = {"Coke" : 1.19, "Pepsi" : 1.18, "Sprite" : 1.19, "Oreo Milshake" : 2.99, "Strawberry Milkshake" : 2.99,
             "Crab cakes" : 5.99, "Chips and dip" : 2.99, "Stuffed Mushroomd" : 3.19, "Cheese stuffed pepper" : 2.99, "Mozarella sticks" : 2.39,
             "Fettucine alfredo" : 9.99, "Cheeseburger" : 7.99, "Double cheeseburger" : 9.99, "Burger" : 7.39, "Double Burger" : 9.39, "Lasagna" : 10.99, "Habanero BBQ shrimp" : 12.99, "Lobster tail" : 15.99, "Slow roasted salmon" : 12.99,
             "Large fries" : 4.99, "Medium fries" : 3.99, "Small fries" : 2.99, "Onion rings" : 3.99, "Ceasar salad" : 3.99
             }