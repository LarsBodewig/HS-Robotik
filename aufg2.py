from commons import AlphaBot
import random

def main():
    bot = AlphaBot()
    #bot.calibrateSensor()
    while True:
        time = random.random() * 10
        turn(bot, time)
        bot.forwardUntilOnLine(time)        
        if bot.isOnLine():
            print(bot.lineAngle())
            goBack(bot)

def turn(bot, timeToTurn):
    turnIt = random.random()
    if turnIt < 0.5:
        bot.leftFor(timeToTurn)
    else:
        bot.rightFor(timeToTurn)

def goBack(bot):
    bot.rightFor(4)
    bot.forwardFor(0.3)

if __name__ == '__main__':
    main()
