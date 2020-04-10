from commons import AlphaBot
import time

def main():
    bot = AlphaBot()
    bot.debug = True
    while True:
        print("new Read --> ")
        time.sleep(2)
        print(bot.lineAngle())
        print("<-- end Read \n ")



if __name__ == '__main__':
    main()
