import random
import time
from os import system, name

target = ""
dialarray = list("0123456789")

userIn = ""


def sleep(n):
    time.sleep(n)


def genTarget():
    global target
    for x in range(0, 10):
        n = random.randint(0,9)
        target += str(n)


def numberLint(num):
    spaced_num = num + "??????????"
    lintx = ""
    lintx += "("
    lintx += spaced_num[0:3] + ") "
    lintx += spaced_num[3:6] + "-"
    lintx += spaced_num[6:10]
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
        dial()


def validator(n):
    if str(n) in dialarray:
        return True
    else:
        return False


def setup():
    genTarget()
    random.shuffle(dialarray)


def debugprinter():
    print(target)
    print(numberLint(target))
    print(dialarray)


def thegame():
    global userIn
    global dialarray

    digit = getin()
    userIn += dialarray[int(digit)]


def getin():
    inp = str(input())
    if validator(inp):
        return inp
    else:
        print("Please input a valid single digit.\n")
        return getin()


def main():
    global target
    global dialarray

    setup()
    debugprinter()
    print(numberLint("69"))

    dial()
    print(userIn)
    # sleep(3)
    # clear()


if __name__ == '__main__':
    main()
