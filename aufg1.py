from commons import AlphaBot
import time


def main():
    bot = AlphaBot()
    while True:
        bot.SERVO.forward()
        time.sleep(0.1)
        bot.SERVO.right()
        time.sleep(3)

if __name__ == '__main__':
    main()