import random

print("\n" + "Welcome to the dice roller!")

def input_checker(user_input):
    if user_input.isdigit() and int(user_input) != 0:
        return True
    else:
        return False

# roll_dice generates rolls nad puts them into a list.
def roll_dice(number_of_dice, size_of_dice):
    while input_checker(number_of_dice) and input_checker(size_of_dice):
        rolls = []
        for i in range(int(number_of_dice)):
            rolls.append(random.randint(1, int(size_of_dice)))
        return rolls 
    return "Invalid input"

print roll_dice("4", "8")
