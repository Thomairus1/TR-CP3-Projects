import random
while True:
    a = int(input("Pick a starting value for the range: "))
    b = int(input("Pick an ending value for the range: "))
    number = random.randrange(a, b)
    
    guess = int(input(f"Pick a number between {str(a)} and {str(b)}: "))
    
    if guess > b:
        print(f"This is bigger than {str(a)}.")
    if guess < a:
        print(f"This is lower than {str(b)}")






    if guess > number:
        print("Number is too high.")
        continue
    elif guess < number:
        print("Number is too low.")
        continue
    elif guess == number:
        print("This is the correct number!")
        again = input("Would you like to play again? (Yes/No): ")
    if again == "No":
        break
    if again == "Yes":
        number = int(input("Pick a new number: "))
        continue
