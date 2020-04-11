from commons import AlphaBot
import time

def main():
    bot = AlphaBot()
    bot.debug = True
    pillars = bot.CAMERA.searchCorners()
    smallest = 1
    for i in range(0, len(pillars)):
        if abs(pillars[i][3]) < smallest:
            smallest = pillars[i][3]
    bot.forwardUntilOnLine(15)
    if smallest > 0:
        bot.rightFor(2)
    else:
        bot.leftFor(2)

if __name__ == '__main__':
    time.sleep(4)
    main()
