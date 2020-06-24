from commons import AlphaBot
import time

rotate_max = 1
rotate_factor = 0.5
tolerance = 0.1

def main():
    bot = AlphaBot()
    bot.debug = True
    streamImage = bot.CAMERA.captureImage()
    img = bot.CAMERA.scs.drawBlackLinesOnImg(streamImage)
    img[0].save('./cameraTestImages/test_24-06-2020-2.jpg')



if __name__ == '__main__':
    time.sleep(4)
    main()
