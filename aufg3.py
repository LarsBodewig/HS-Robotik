from commons import AlphaBot

def main():
    bot = AlphaBot()
    for i in range(0, 10):
        result = bot.CAMERA.searchCorners()
        print(result)
        bot.leftFor(0.5)



if __name__ == '__main__':
    main()
