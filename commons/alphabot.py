import Servo
import Sensor
import Camera
import time

class AlphaBot(object):

	def __init__(self):
		self.SERVO = Servo()
        self.SENSOR = Sensor()
        self.CAMERA = Camera()
        self.calibrateSensor()

    def forwardFor(self, time):
        self.SERVO.forward()
        time.sleep(time)
        self.SERVO.stop()

    def leftFor(self, time):
        self.SERVO.left()
        time.sleep(time)
        self.SERVO.stop()

    def rightFor(self, time):
        self.SERVO.right()
        time.sleep(time)
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
