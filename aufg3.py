from commons import AlphaBot

def main():
    bot = AlphaBot()
    for i in range(0, 10):
        result = bot.CAMERA.searchCorners()
        print(result)
        bot.leftFor(1)
    for i in range(0, 10):
        result = bot.CAMERA.searchCorners()
        print(result)
        bot.rightFor(1)



if __name__ == '__main__':
    main()
