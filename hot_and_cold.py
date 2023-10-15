import random
import datetime

file_var = open("debug_logger.txt", "w")

def logger(log_str):
    file_var = open("debug_logger.txt", "a")
    dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file_var.write(dt + ": " + str(log_str) + "\n")
    file_var.close()

global x_flag 
x_flag = random.randint(10,1000)
global y_flag 
y_flag= random.randint(10,1000)

logger("X flag location is " + str(x_flag))
logger("Y flag location is " + str(y_flag))

def show_game_instructions():
    print(' Welcome to Hot and Cold!')
    print(' I have Hidden the flag in a secret location.')
    print(' You are starting at position (0, 0).')
    print(' I will ask you, if you want to move Up/Down/Left/Right')
    print(' And then how many steps')
    print(' I will then tell you if you are hotter or colder')

def main():
    x_loc = 0
    y_loc = 0
    found_flag = False
    show_game_instructions()
    while not found_flag:
        direction, steps = ask_user()
        if direction == "U":
            if 0 <= y_loc + steps < 1000:
                old_loc = y_loc
                y_loc += steps
                logger("The user went up from (" + str(x_loc) + ", " + str(old_loc) + ")" + \
                    " to (" + str(x_loc) + ", " + str(y_loc) + ")")
                report_distance(x_loc, y_loc)
                report_y(y_loc, old_loc)
            else:
                invalid()
        elif direction == "D":
            if 0 <= y_loc - steps < 1000:
                old_loc = y_loc
                y_loc -= steps
                logger("The user went down from (" + str(x_loc) + ", " + str(old_loc) + ")" + \
                    " to (" + str(x_loc) + ", " + str(y_loc) + ")")
                report_distance(x_loc, y_loc)
                report_y(y_loc, old_loc)
            else:
                invalid()
        elif direction == "R":
            if 0 <= x_loc + steps < 1000:
                old_loc = x_loc
                x_loc += steps
                logger("The user went right from (" + str(old_loc) + ", " + str(y_loc) + ")" + \
                    " to (" + str(x_loc) + ", " + str(y_loc) + ")")
                report_distance(x_loc, y_loc)
                report_x(x_loc, old_loc)
            else:
                invalid()
        elif direction == "L":
            if 0 <= x_loc - steps < 1000:
                old_loc = x_loc
                x_loc -= steps
                logger("The user went left from (" + str(old_loc) + ", " + str(y_loc) + ")" + \
                    " to (" + str(x_loc) + ", " + str(y_loc) + ")")
                report_distance(x_loc, y_loc)
                report_x(x_loc, old_loc)
            else:
                invalid()
        elif direction == "Q":
            found_flag = True
        if x_loc == x_flag and y_loc == y_flag:
            print("Wait, in fact, you're SO SUPER HOT that you won!!")
            found_flag = True

def ask_user():
    direction = input('Give me direction (U/ D/ R/ L), or type Q to quit: ')
    if direction != "Q":
        steps = int(input('Give me number of steps: '))
    else:
        steps = 0
    return direction, steps

def invalid():
    logger("The user inserted an invalid move.")
    print("Invalid move")

def report_y(y_loc, old_loc):
    if abs(y_flag - old_loc) > abs(y_flag - y_loc):
        print("warmer!")
    elif abs(y_flag - old_loc) == abs(y_flag - y_loc):
        print("not warmer or colder.")
    else:
        print("colder!")

def report_x(x_loc, old_loc):
    if abs(x_flag - old_loc) > abs(x_flag - x_loc):
        print("warmer!")
    elif abs(x_flag - old_loc) == abs(x_flag - x_loc):
        print("not warmer nor colder.")
    else:
        print("colder!")

def report_distance(x_loc, y_loc):
    print("You are ", end="")
    var = abs(x_flag-x_loc) + abs(y_flag-y_loc)
    if var < 10:
        print("SUPER HOT", end="")
    elif var < 100:
        print ("VERY HOT", end="")
    elif var < 300:
        print("hot", end="")
    elif var < 600:
        print("lukewarm", end="")
    elif var < 1000:
        print("cold", end="")
    else:
        print("FREEZING COLD", end="")
    print(", and btw, you are getting ", end="")

try:
    main()
except IOError:
    print("A file error occured :(")