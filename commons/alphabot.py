from servo import Servo
from sensor import Sensor
from camera import Camera
import time

class AlphaBot(object):

    def __init__(self):
        self.SERVO = Servo()
        self.SENSOR = Sensor()
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

    def calibrateSensor(self):
        for i in range(0, 15):
            self.SENSOR.calibrate()
            self.forwardFor(0.1)

    def isOnLine(self):
        last_value, sensor_values = self.SENSOR.readLine()
        onLine = False
        for i in range(0, self.SENSOR.numSensors):
            if sensor_values[i] > 200:
                onLine = True
        return onLine
