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

    @classmethod
    def order(self):
        print("Drinks: \n", drink_dict, "\n")
        print("Appetizers: \n", appt_dict, "\n")
        print("Main Cousres: \n", main_dict, "\n")
        print("Sides: \n", side_dict, "\n")
        print("Desserts: \n", destr_dict, "\n")
        return FoodOrder(input("Choose a drink from the menu: "), input("Choose an appetizer from the menu: "), input("Choose a main course from the menu: "), input("Choose a side from the menu: "), input("Choose a second side from the menu: "), input("Choose a dessert from the menu: "))
        
    @staticmethod
    def total(ordered):
        print("Total: $", drink_dict[ordered.drink] + appt_dict[ordered.appt] + main_dict[ordered.main] + side_dict[ordered.side1] + side_dict[ordered.side2] + destr_dict[ordered.dessert])

        
    
order1 = FoodOrder("Coke", "Crab cakes", "Double cheeseburger", "Fries", "Onion Rings", "Cheesecake")

print(order1)

drink_dict = {"Coke" : 1.19, "Pepsi" : 1.18, "Sprite" : 1.19, "Oreo Milshake" : 2.99, "Strawberry Milkshake" : 2.99}
appt_dict =  {"Crab cakes" : 5.99, "Chips and dip" : 2.99, "Stuffed Mushroomd" : 3.19, "Cheese stuffed pepper" : 2.99, "Mozarella sticks" : 2.39}
main_dict = {"Fettucine alfredo" : 9.99, "Cheeseburger" : 7.99, "Double cheeseburger" : 9.99, "Burger" : 7.39, "Double Burger" : 9.39, "Lasagna" : 10.99, "Habanero BBQ shrimp" : 12.99, "Lobster tail" : 15.99, "Slow roasted salmon" : 12.99}
side_dict = {"Large fries" : 4.99, "Medium fries" : 3.99, "Small fries" : 2.99, "Onion rings" : 3.99, "Ceasar salad" : 3.99, "Tomato soup" : 3.99, "Baked potato" : 3.99, "Taco soup" : 3.99}
destr_dict = {"Cheesecake" : 4.99, "Creme caramel" : 6.99, "Vanilla icecream" : 1.99, "Chocolate icecream" : 1.99, "Crepes" : 3.99}

order2 = FoodOrder.order()
print(order2)

FoodOrder.total(order2)
