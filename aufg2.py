from commons import AlphaBot
import random

def main():
    bot = AlphaBot()
    #bot.calibrateSensor()
    while True:
        time = random() * 10
        turn(time)
        while time > 0 and not bot.isOnLine():
            bot.forwardFor(0.1)
            time -= 0.1
        if bot.isOnLine():
            print(bot.lineAngle())
            goBack()

def turn(timeToTurn):
    turnIt = random()
    if turnIt < 0.5:
        bot.leftFor(timeToTurn)
    else:
        bot.rightFor(timeToTurn)

def goBack():
    bot.rightFor(6)
    bot.forwardFor(2)

if __name__ == '__main__':
    main()
