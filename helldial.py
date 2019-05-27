import random
import time
from os import system, name
import sys

target = ""
dialarray = list("0123456789")
userIn = ""
difficulty = ""
errorcount = 0


def main():
    sysvercheck()
    clear()
    setup()
    setdiff()
    clear()
    presenttarget()
    # debugarray()

    thegame()

def thegame():
    global userIn
    global dialarray
    global target
    global difficulty

    dial()
    if wincheck():
        winstate()
    if checkcorrect():
        if difficulty != "easy":
            clear()
        print(numberLint(target))
        print(numberLint(userIn))
        thegame()
    else:
        lossstate()
        if losslimitreached():
            rebinder()
        presenttarget()
        thegame()

def sleep(n):
    time.sleep(n)


def genTarget():
    global target
    for x in range(0, 10):
        n = random.randint(0,9)
        target += str(n)


def numberLint(num):
    spaced_num = num + "??????????"
    lintx =  "(" + spaced_num[0:3] + ") " + spaced_num[3:6] + "-" + spaced_num[6:10]
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
        userIn += dialarray[int(n)]
    else:
        print("please input a valid digit")
        return dial()


def validator(n):
    if str(n) in dialarray:
        return True
    else:
        return False


def setup():
    genTarget()
    random.shuffle(dialarray)


def setdiff():
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
        setdiff()


def presenttarget():
    print("please dial " + numberLint(target))


def checkcorrect():
    global dialarray
    global userIn
    global target

    return target.startswith(userIn)

def lossstate():
    global userIn
    global target
    global errorcount

    errorcount += 1
    print(numberLint(target))
    print(numberLint(userIn))
    sleep(.3)
    print("Incorrect, preparing to clear")
    sleep(2)
    userIn = ""
    clear()
    
def rebinder():
    global dialarray
    print("ERROR LIMIT REACHED, REBINDING KEYS")
    random.shuffle(dialarray)

def wincheck():
    global userIn
    global target

    return target == userIn

def winstate():
    global userIn
    global target

    print(numberLint(target))
    print(numberLint(userIn))
    print("You win!")
    exit()

def losslimitreached():
    global difficulty
    global errorcount

    limits = {
        'easy': 50,
        'normal': 25,
        'hard': 15
    }

    return errorcount >= limits.get(difficulty)

def debugarray():
    print(dialarray)


def sysvercheck():
    if sys.version[0] < "3":
        raise Exception("bruh, you gotta have python 3+ to use this")


if __name__ == '__main__':
    main()
