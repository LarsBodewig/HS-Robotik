from commons import AlphaBot
import random

def main():
    bot = AlphaBot()
    while True:
        moveRandom()
        line = bot.isOnLine()
        if line:
            turn()

def moveRandom():
    turn = random()
    time = random() * 10
    if turn < 0.5:
        bot.leftFor(time)
    else:
        bot.rightFor(time)
    bot.forwardFor(0.1)

def turn():
    bot.rightFor(6)
    bot.forwardFor(2)

if __name__ == '__main__':
    main()
