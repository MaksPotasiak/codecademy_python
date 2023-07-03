print"""
Welcome to the divisibility calculator.

Please enter an intiger you\'d like to check:"""

check1 = True

while check1:

    number = raw_input()

    if number.isdigit():
        print"Thanks! And what would you like to divide it by?"
        check1 = False

    else:
        print"Sorry, you must enter an integer for me to work, please try again."

check2 = True

while check2:

    divider = raw_input()

    if divider.isdigit() and int(divider) != 0:
        

        if (int(number) % int(divider)) == 0:
            print "Yes, %s is divisible by %s!" % (number, divider)
        
        else:
            print"No, %s is not divisible by %s." % (number, divider)

        check2 = False

    elif int(divider) == 0: 
        print"The divider must not equal 0, please enter a valid integer."

    else:
        print"Sorry, you must enter an integer for the divider, please try again."

