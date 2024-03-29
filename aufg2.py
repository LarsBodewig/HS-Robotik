from commons import AlphaBot
import random
import time
def main():
    bot = AlphaBot()
    #bot.calibrateSensor()
    while True:
        timeToDrive = random.random() * 10
        turn(bot)
        bot.forwardUntilOnLine(timeToDrive)
        if bot.isOnLine():
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
    time.sleep(4)
    main()
