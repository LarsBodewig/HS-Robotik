from commons import AlphaBot
from cameraImpl import searchColorStripes

def main():
    bot = AlphaBot()
    stream = bot.captureImage()
    scs = searchColorStripes()

    result = scs.distanceFromImgCenter(stream)

if __name__ == '__main__':
    main()
