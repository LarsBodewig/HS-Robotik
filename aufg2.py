from commons import AlphaBot
import random

def main():
    bot = AlphaBot()
    #bot.calibrateSensor()
    while True:
        time = random.random() * 10
        turn(bot)
        bot.forwardUntilOnLine(time)
        if bot.isOnLine():
            print(bot.lineAngle())
            goBack(bot)

def turn(bot):
    timeToTurn = random.random() * 2
    turnIt = random.random()
    if turnIt < 0.5:
        bot.leftFor(timeToTurn)
    else:
        bot.rightFor(timeToTurn)

def goBack(bot):
    bot.rightFor(2)
    bot.forwardUntilOnLine(0.3)

if __name__ == '__main__':
    time sleep(4)
    main()
