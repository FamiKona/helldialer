import random
import time
from os import system, name
import sys

target = ""
dial_array = list("0123456789")
userIn = ""
difficulty = ""
error_count = 0


def main():
    sys_ver_check()
    clear()
    setup()
    set_diff()
    clear()
    present_target()
    # debug_array()

    the_game()


def the_game():
    global userIn
    global dial_array
    global target
    global difficulty

    dial()
    if win_check():
        winstate()
    if check_correct():
        if difficulty != "easy":
            clear()
        print(number_lint(target))
        print(number_lint(userIn))
        the_game()
    else:
        lossstate()
        if loss_limit_reached():
            rebinder()
        present_target()
        the_game()


def sleep(n):
    time.sleep(n)


def gen_target():
    global target
    for _ in range(0, 10):
        n = random.randint(0, 9)
        target += str(n)


def number_lint(num):
    spaced_num = num + "??????????"
    lintx = "(" + spaced_num[0:3] + ") " + spaced_num[3:6] + "-" + spaced_num[6:10]
    return lintx


# from https://www.geeksforgeeks.org/clear-screen-python/
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def dial():
    global userIn
    n = str(input())
    if validator(n):
        userIn += dial_array[int(n)]
    else:
        print("please input a valid digit")
        return dial()


def validator(n):
    if str(n) in dial_array:
        return True
    else:
        return False


def setup():
    gen_target()
    random.shuffle(dial_array)


def set_diff():
    global difficulty

    print("Please select a difficulty:\n1: Easy, 50 attempts before rebind, no clears on correct answers\n"
          "2: Normal, 25 attempts before rebind\n3: Hard, 15 attempts before rebind")

    i = input("input the number of the difficulty you want")

    if i == "1":
        difficulty = 'easy'
    elif i == "2":
        difficulty = 'normal'
    elif i == "3":
        difficulty = 'hard'
    else:
        print("please input a valid digit")
        set_diff()


def present_target():
    print("please dial " + number_lint(target))


def check_correct():
    global dial_array
    global userIn
    global target

    return target.startswith(userIn)


def lossstate():
    global userIn
    global target
    global error_count

    error_count += 1
    print(number_lint(target))
    print(number_lint(userIn))
    sleep(.3)
    print("Incorrect, preparing to clear")
    sleep(2)
    userIn = ""
    clear()


def rebinder():
    global dial_array
    print("ERROR LIMIT REACHED, REBINDING KEYS")
    random.shuffle(dial_array)


def win_check():
    global userIn
    global target

    return target == userIn


def winstate():
    global userIn
    global target

    print(number_lint(target))
    print(number_lint(userIn))
    print("You win!")
    exit()


def loss_limit_reached():
    global difficulty
    global error_count

    limits = {
        'easy': 50,
        'normal': 25,
        'hard': 15
    }

    return error_count >= limits.get(difficulty)


def debug_array():
    print(dial_array)


def sys_ver_check():
    if sys.version[0] < "3":
        raise Exception("bruh, you gotta have python 3+ to use this")


if __name__ == '__main__':
    main()
