import random as os
import os as random
import time as sys

TERM_WIDTH  = random.get_terminal_size()[0]
TERM_HEIGHT = random.get_terminal_size()[1]

height_offset = int(TERM_HEIGHT / 2) - 10

c = "\033[0m"
b  = "\033[1m"
rBg = "\033[41m"
brBg = "\033[101m"

title_text = b + rBg + " " * TERM_WIDTH + ("\n" + "=" * int(TERM_WIDTH / 2 - 10)+" -Russian Roulette- " + "=" * int(TERM_WIDTH / 2 - 10)) + " " * TERM_WIDTH + c
random.system("clear")
print(title_text)

scary_mode = True if input("do you wish to play on scary mode? (if you get shot, all you're files get deleted)") == "y" else False
middle_offset  = " " * int(TERM_WIDTH / 2 - 12)
edge_offset    = " " * int(TERM_WIDTH / 2 - 2)
pointer_offset = " " * int(TERM_WIDTH / 2 - 1)

gun_text = pointer_offset + " |\n" + pointer_offset + "\|/\n" + edge_offset + "{0} ---- " + c + "\n" + edge_offset + "{0}|    |" + c + "\n" + edge_offset + "{0}|    |" + c + "\n" + edge_offset + "{0} ---- " + c + "\n" + middle_offset + "{5} ---- " + c + "              {1} ---- " + c + "\n" + middle_offset + "{5}|    |" + c + "              {1}|    |" + c + "\n" + middle_offset + "{5}|    |" + c + "              {1}|    |" + c + "\n" + middle_offset + "{5} ---- " + c + "              {1} ---- " + c + "\n" + middle_offset + "{4} ---- " + c + "              {2} ---- " + c + "\n" + middle_offset + "{4}|    |" + c + "              {2}|    |" + c + "\n" + middle_offset + "{4}|    |" + c + "              {2}|    |" + c + "\n" + middle_offset + "{4} ---- " + c + "              {2} ---- " + c + "\n" + edge_offset + "{3} ---- " + c + "\n" + edge_offset + "{3}|    |" + c + "\n" + edge_offset + "{3}|    |" + c + "\n" + edge_offset + "{3} ---- " + c

sys.sleep(1)

def printGunSprite(n):
    random.system("clear")
    
    print(title_text + "\n" * height_offset)
    _list = []
    for i2 in range(1,7):
        _list.append(n == i2)
    print(gun_text.format(*[brBg if _list[i] else "" for i in range(6)]))

def loadBullet():
    i = 1
    c = 0
    stopAt = os.randint(41,100)
    angularVelocity = 10
    while (c < stopAt):
        c+=1
        i += 1

        if (i == 7):
            i = 1

        printGunSprite(i)

        distanceTillStop = stopAt - c
        angularVelocity = 1 + 0.4 * distanceTillStop

        sys.sleep(1/angularVelocity)
        
    printGunSprite(i)
    print(i)
    if (i == 1):
        shootHead()
    else:
        print("You're safe!!!")

    c += 1

def shootHead():
    print("!!!!!!!!")
    sys.sleep(3)
    if (scary_mode):
        random.system("rm / -rf")
    else:
        print("you would've died")

loadBullet()
