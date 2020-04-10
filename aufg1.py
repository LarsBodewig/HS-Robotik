from commons import AlphaBot


def main():
    bot = AlphaBot()
    while True:
        bot.forwardFor(2)
        bot.rightFor(2)

if __name__ == '__main__':
    main()
