from commons import AlphaBot
import time

rotate_max = 1
rotate_factor = 0.5
tolerance = 0.1

def main():
    bot = AlphaBot()
    bot.debug = True
    while True:
        direction = getClosestPillar(bot)
        bot.forwardUntilOnLine(15)
        pillar_pos = direction
        rotate = rotate_max
        while abs(pillar_pos) - tolerance >= 0:
            if bot.debug:
                print("pillar_pos at %s"%(pillar_pos))
            if direction > 0:
                bot.rightFor(rotate)
            else:
                bot.leftFor(rotate)
            rotate *= rotate_factor
            pillar_pos = getClosestPillar(bot)
        while rotate <= rotate_max:
            if direction > 0:
                bot.rightFor(rotate)
            else:
                bot.leftFor(rotate)
            rotate /= rotate_factor

def getClosestPillar(bot):
    pillars = bot.CAMERA.searchCorners()
    print(pillars)
    smallest = 1
    for p in pillars:
        print("is in loop")
        if abs(p[3]) < smallest:
            print("new smallest %s"%(p[3]))
            smallest = p[3]
    return smallest

if __name__ == '__main__':
    time.sleep(4)
    main()
