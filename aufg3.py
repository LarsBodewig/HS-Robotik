from commons import AlphaBot

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
            if direction > 0:
                bot.rightFor(rotate)
            else:
                bot.leftFor(rotate)
            rotate *= rotate_factor
            pillar_pos = getClosestPillar(bot)
        if bot.debug: 
            print("pillar_pos at %s"%(pillar_pos))
        while rotate <= rotate_max:
            if direction > 0:
                bot.rightFor(rotate)
            else:
                bot.leftFor(rotate)
            rotate /= rotate_factor

def getClosestPillar(bot):
    pillars = bot.CAMERA.searchCorners()
    smallest = 1
    for i in range(0, len(pillars)):
        if abs(pillars[i][3]) < smallest:
            smallest = pillars[i][3]
    return smallest

if __name__ == '__main__':
    time.sleep(4)
    main()
