from commons import AlphaBot
from cameraImpl import searchColorStripes

def main():
    bot = AlphaBot()
    stream = bot.CAMERA.captureImage()
    scs = searchColorStripes(newDebug=True)

    result = scs.distanceFromImgCenter(stream)

if __name__ == '__main__':
    main()
