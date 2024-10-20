class FoodOrder:
    
# instatiates class attributes
    def __init__(self, drink, appt, main, side1, side2, dessert):
        self.drink = drink 
        self.appt = appt
        self. main = main
        self.side1 = side1
        self.side2 = side2
        self.dessert = dessert
        
# prints out attributes of the object
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
# asks user for order and makes it an object
    def order(self):
        print("Drinks: \n", drink_dict, "\n")
        print("Appetizers: \n", appt_dict, "\n")
        print("Main Cousres: \n", main_dict, "\n") 
        print("Sides: \n", side_dict, "\n")
        print("Desserts: \n", destr_dict, "\n")
        ordering = FoodOrder(input("Choose a drink from the menu: "), input("Choose an appetizer from the menu: "), input("Choose a main course from the menu: "), input("Choose a side from the menu: "), input("Choose a second side from the menu: "), input("Choose a dessert from the menu: "))
        
        return ordering
                
            
            
           
    @staticmethod
# returns price of order based on the price of the item in the dictionary
    def total(ordered):
        t = (drink_dict[ordered.drink] + appt_dict[ordered.appt] + main_dict[ordered.main] + side_dict[ordered.side1] + side_dict[ordered.side2] + destr_dict[ordered.dessert])
        t1 = round(t, 2)
        print("Total: $", t1)
        
    def check_order(ordered):
        a = 0
        drinks = drink_dict.keys()
        appts = appt_dict.keys()
        mains = main_dict.keys()
        sides = side_dict.keys()
        destrs = destr_dict.keys()
        if ordered.drink == "" and ordered.appt == "" and ordered.main == "" and ordered.side1 == "" and ordered.side2 == "" and ordered.dessert == "":
            ordered = FoodOrder(input("Choose a drink from the menu: "), input("Choose an appetizer from the menu: "), input("Choose a main course from the menu: "), input("Choose a side from the menu: "), input("Choose a second side from the menu: "), input("Choose a dessert from the menu: "))
        while a < 6:
            if ordered.drink in drinks:
                a += 1
            else:
                ordered.drink = input("Choose a drink from the menu: ")
                
            if ordered.appt in appts:
                a += 1
            else:
                ordered.appt = input("Choose an appetizer from the menu: ")
                
            if ordered.main in mains:
                a += 1
            else:
                ordered.main = input("Choose a main course from the menu: ")
                    
            if ordered.side1 in sides:
                a += 1
            else:
                ordered.side1 = input("Choose a side from the menu: ")
                
            if ordered.side2 in sides:
                a += 1
            else:
                ordered.side2 = input("Choose a second side from the menu: ")
                
            if ordered.dessert in destrs:
                a += 1
            else:
                ordered.dessert = input("Choose a dessert from the menu: ")
        return ordered
        
    def change(ordered):
        ask = input("Do you want to change your order? (Yes or No) ")
        if ask == "Yes":
            ask2 = input("Do you want to change drink, appetizer, main, side 1, side 2, or dessert? ")
            if ask2 == "drink":
                ordered.drink = input("Choose a drink from the menu: ")
            elif ask2 == "appetizer":
                ordered.appt = input("Choose an appetizer from the menu: ")
            elif ask2 == "main":
                ordered.main = input("Choose a main course from the menu: ")
            elif ask2 == "side 1":
                ordered.side1 = input("Choose a side from the menu: ")
            elif ask2 == "side 2":
                ordered.side2 = input("Choose a second side from the menu: ")
            elif ask2 == "dessert":
                ordered.dessert = input("Choose a dessert from the menu: ")
            return ordered
        if ask == "No":
            return ordered
        
                
# tests out the str method
order1 = FoodOrder("Coke", "Crab cakes", "Double cheeseburger", "Fries", "Onion Rings", "Cheesecake")
print(order1)

# dictionaries from which the user should order
drink_dict = {"Coke" : 1.19, "Pepsi" : 1.18, "Sprite" : 1.19, "Oreo Milshake" : 2.99, "Strawberry Milkshake" : 2.99}
appt_dict =  {"Crab cakes" : 5.99, "Chips and dip" : 2.99, "Stuffed Mushroomd" : 3.19, "Cheese stuffed pepper" : 2.99, "Mozarella sticks" : 2.39}
main_dict = {"Fettucine alfredo" : 9.99, "Cheeseburger" : 7.99, "Double cheeseburger" : 9.99, "Burger" : 7.39, "Double Burger" : 9.39, "Lasagna" : 10.99, "Habanero BBQ shrimp" : 12.99, "Lobster tail" : 15.99, "Slow roasted salmon" : 12.99}
side_dict = {"Large fries" : 4.99, "Medium fries" : 3.99, "Small fries" : 2.99, "Onion rings" : 3.99, "Ceasar salad" : 3.99, "Tomato soup" : 3.99, "Baked potato" : 3.99, "Taco soup" : 3.99}
destr_dict = {"Cheesecake" : 4.99, "Creme caramel" : 6.99, "Vanilla icecream" : 1.99, "Chocolate icecream" : 1.99, "Crepes" : 3.99}

# tests out the order method
order2 = FoodOrder.order()
print(order2)

# check_order makes sure the order isn't empty and that its items are in the menu
print(FoodOrder.check_order(order2))

print(FoodOrder.change(order2))


# tests out the total method 
FoodOrder.total(order2)
