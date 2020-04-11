from servo import Servo
from sensor import Sensor
from camera import Camera
import time
import math

sensor_maxs = [934, 545, 953, 932, 781]
sensor_mins = [113, 55, 117, 92, 74]
sensor_threshold = 200
debug = False

class AlphaBot(object):

    def forwardUntilOnLine(self, howLong):
        isCurrentlyOnLine = self.isOnLine()
        if isCurrentlyOnLine == False :
            self.SERVO.forward()
        now = time.time()
        future = now + howLong
        while isCurrentlyOnLine == False and time.time() < future:
            isCurrentlyOnLine = self.isOnLine()
            #do nothing, because not on line
        self.SERVO.stop()

    def __init__(self):
        self.SERVO = Servo()
        self.SENSOR = Sensor()
        self.SENSOR.calibratedMin = sensor_mins
        self.SENSOR.calibratedMax = sensor_maxs
        self.CAMERA = Camera()

    def forwardFor(self, duration):
        self.SERVO.forward()
        time.sleep(duration)
        self.SERVO.stop()

    def leftFor(self, duration):
        self.SERVO.left()
        time.sleep(duration)
        self.SERVO.stop()

    def rightFor(self, duration):
        self.SERVO.right()
        time.sleep(duration)
        self.SERVO.stop()

    def isOnLine(self):
        last_value, sensor_values = self.SENSOR.readLine()
        onLine = False
        for i in range(0, self.SENSOR.numSensors):
            if debug: print(sensor_values[i])
            if sensor_values[i] < sensor_threshold:
                onLine = True
        return onLine
