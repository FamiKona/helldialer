import random
import time
from os import system, name

target = ""
dialarray = [
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
]

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


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def main():
    global target
    global dialarray
    genTarget()
    random.shuffle(dialarray)
    print(target)
    print(numberLint(target))
    print(dialarray)


if __name__ == '__main__':
    main()