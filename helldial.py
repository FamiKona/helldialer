import random
import time
from os import system, name

target = ""
dialarray = list("0123456789")

userIn = ""


def main():
    clear()
    setup()
    presenttarget()
    debugarray()

    thegame()


def thegame():
    global userIn
    global dialarray
    global target

    dial()
    if wincheck():
        winstate()
    if checkcorrect():
        print(numberLint(target))
        print(numberLint(userIn))
        thegame()
    else:
        lossstate()
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

    print(numberLint(target))
    print(numberLint(userIn))
    sleep(.3)
    print("Incorrect, preparing to clear")
    sleep(2)
    userIn = ""
    clear()

def wincheck():
    global userIn
    global target

    return target is userIn

def winstate():
    global userIn
    global target

    print(numberLint(target))
    print(numberLint(userIn))
    print("You win!")
    exit()

def debugarray():
    print(dialarray)


if __name__ == '__main__':
    main()
