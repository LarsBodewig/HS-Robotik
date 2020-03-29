from commons.alphabot import alphabot
import time


def main():
    bot = alphabot()
    while(true):
        bot.servo.forward()
        time.sleep(0.5)
        bot.servo.right()
        time.sleep(1)

if __name__ == '__main__':
    main()