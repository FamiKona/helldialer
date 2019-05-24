import random

target = ""

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

def main():
    global target
    genTarget()
    print(target)
    print(numberLint(target))

if __name__ == '__main__':
    main()