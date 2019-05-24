import random
import time
from os import system, name

target = ""
dialarray = [
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
]

userIn = ""


def sleep(n):
    time.sleep(n)


def genTarget():
    global target
    for x in range(0, 10):
        n = random.randint(0,9)
        target += str(n)


def numberLint(num):
    lintx = ""
    lintx += "("
    lintx += num[0:3] + ") "
    lintx += num[3:6] + "-"
    lintx += num[6:10]
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

def main():
    global target
    global dialarray

    setup()
    debugprinter()

    dial()
    print(userIn)
    # sleep(3)
    # clear()


if __name__ == '__main__':
    main()
