import random

print("\n" + "Welcome to the dice roller!")

def input_checker(user_input):
    if user_input.isdigit() and int(user_input) != 0:
        return True
    else:
        return False


def roll_dice(number_of_dice, size_of_dice):
    rolls = []
    for i in range(number_of_dice):
        rolls.append(random.randint(1, size_of_dice))
    overall_result = sum(rolls)
    print rolls
    return overall_result

print roll_dice(2, 8)