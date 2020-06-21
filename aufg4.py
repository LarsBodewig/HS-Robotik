from commons import AlphaBot
import time

rotate_for_s = 2
x_max_cm = 100
y_max_cm = 50
pillar_diameter_cm = 3
focal_width = 999
pillar_color_x0_y0 = [1,2,3]
pillar_color_xmax_y0 = [1,2,3]
pillar_color_x0_ymax = [1,2,3]
pillar_color_xmax_ymax = [1,2,3]

def main():
    bot = AlphaBot()
    bot.debug = True
    pillars = getPillars(bot)
    pos = getPos(pillars)
    printPos(pos);

def getPillars(bot):
    pillars = bot.CAMERA.searchCorners()
    if bot.debug:
        print(pillars)
    while len(pillars) < 2:
        bot.rightFor(rotate_for_s)
        pillars = bot.CAMERA.searchCorners()
        if bot.debug:
            print(pillars)
    return pillars

def getPos(pillars):
    distances = []
    colors = []
    for p in pillars:
        width_px = abs(p[3] - p[4])
        distance_cm = pillar_diameter_cm * focal_width / width_px
        distance_tuple = (width_px, distance_cm)
        distances.append(distance_tuple)
    for p in pillars:
        mean_x = (p[3] + p[4]) / 2
        colors.append(getColors(bots, mean_x))
    x = 0
    y = 0
    return x, y

def getColors(bot, mean_x):
    image = bot.CAMERA.captureImage()
    bot.CAMERA.scs.findTreeColorStripesInARow(image.size[1], image, x) 

def printPos(pos, angle = None):
    output = "x:\t{}\ny:\t{}".format(pos[0], pos[1])
    if angle is not None:
        output += "\ndeg:\t{}".format(angle)
    print(output)
 
if __name__ == '__main__':
    main()
    time.sleep(4)