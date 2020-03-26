from commons import AlphaBot
import time


def main(self):
    bot = AlphaBot()
    while(true):
        bot.servo.forward()
        time.sleep(0.5)
        bot.servo.right()
        time.sleep(1)

if __name__ == '__main__':
    main()