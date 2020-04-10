from commons import AlphaBot
import random

def main():
    bot = AlphaBot()
    //bot.calibrateSensor()
    while True:
        turn()
        time = random() * 10
        while time > 0 and not bot.isOnLine():
            bot.forwardFor(0.1)
            time -= 0.1
        if bot.isOnLine():
            print(bot.lineAngle())
            goBack()

def turn():
    turn = random()
    if turn < 0.5:
        bot.leftFor(time)
    else:
        bot.rightFor(time)

def goBack():
    bot.rightFor(6)
    bot.forwardFor(2)

if __name__ == '__main__':
    main()
