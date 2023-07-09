import random

print("\n" + "Welcome to the dice roller!" + "\n")

def dice_input():
    input = raw_input("What dice are we rolling?" + "\n")
    while not "d" in input:
        input = raw_input("Invalid input." + "\n")
    return input.split("d")

dice_user_data = dice_input()

def input_checker(user_input):
    if user_input.isdigit() and int(user_input) != 0:
        return True
    else:
        return False

# roll_dice generates rolls and puts them into a list.
def roll_dice(number_of_dice, size_of_dice):
    if input_checker(number_of_dice) and input_checker(size_of_dice):
        rolls = []
        for i in range(int(number_of_dice)):
            rolls.append(random.randint(1, int(size_of_dice)))
        print rolls
        return rolls
    else:
        print "Invalid input, try again." + "\n" 
        return dice_input()

print sum(roll_dice(dice_user_data[0], dice_user_data[1]))