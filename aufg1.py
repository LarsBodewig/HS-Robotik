from commons import AlphaBot


def main():
    bot = AlphaBot()
    while True:
        bot.forwardFor(0.1)
        bot.rightFor(3)

if __name__ == '__main__':
    main()