import random

print("\n" + "Welcome to the dice roller!" + "\n")

#dice_input takes input from the user and checks for "d" in the input.
def dice_input():
    input = raw_input("What dice are we rolling?" + "\n" + "Use x\"d\"y format, where x and y are integers:" + "\n")
    while not "d" in input:
        input = raw_input("""
Invalid input, please try again.

What dice are we rolling?
Use x\"d\"y format, where x and y are integers:
""")
    return input.split("d")

#input_checker checks if user values are valid.
def input_checker(user_input):
    if user_input.isdigit() and int(user_input) != 0:
        return True
    else:
        return False

# roll_dice generates rolls and puts them into a list. It also prints the values.
def roll_dice(number_of_dice, size_of_dice):
    rolls = []
    for i in range(int(number_of_dice)):
        rolls.append(random.randint(1, int(size_of_dice)))
    print rolls
    return rolls

#total_value prints a sum of the rolled values.
def total_value():
    user_data = dice_input()
    number_of_dice = user_data[0]
    size_of_dice = user_data[1]
    if input_checker(number_of_dice) and input_checker(size_of_dice):
        print sum(roll_dice(number_of_dice, size_of_dice))
    else:
        print "\n" + "Invalid input, please try again." + "\n"
        total_value()
    
total_value()