from sensor import Sensor
from commons import AlphaBot

bot = AlphaBot()
for i in range(0, 20):
    bot.SENSOR.calibrate()
    bot.rightFor(0.1)
print(bot.SENSOR.calibratedMin)
print(bot.SENSOR.calibratedMax)
