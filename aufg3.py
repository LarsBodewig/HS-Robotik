from commons import AlphaBot
import time

def main():
    bot = AlphaBot()
    bot.debug = True
    while True:
        time.sleep(2)
        print(bot.lineAngle())



if __name__ == '__main__':
    main()
