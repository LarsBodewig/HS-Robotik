from commons import AlphaBot
from time import gmtime, strftime
import paho.mqtt.client as mqtt

movement_topic = "ss20_robotik_t01/+/movement"
camera_topic = "ss20_robotik_t01/+/camera"
speed_topic = "ss20_robotik_t01/+/speed"

def handleIncomingMessage(messageTopic, payLoad, timeStamp):
    try:
        print("Received Message... "+ messageTopic + ", " +payLoad +", "+ timeStamp)
        topicType =  messageTopic.split('/')[2]
        if topicType == "movement":
            processMovement (payLoad)
        if topicType == "camera":
            processCamera (payLoad)
        if topicType == "speed":
            processSpeed (payLoad)

    except Exception as ex:
        print("FAIL")
        print(ex)

def processMovement(payLoad):
    print ("Moveeeiiiing")
    if payLoad == "F":
        bot.SERVO.forward()
    if payLoad == "B":
        bot.SERVO.backward()
    if payLoad == "S":
        bot.SERVO.stop()
    if payLoad == "L":
        bot.SERVO.left()
    if payLoad == "R":
        bot.SERVO.right()

def processCamera(payLoad):
    print ("Cameraaa")
    if payLoad == "U":
        #move Camera Up
        print ("Cameraaa")
    if payLoad == "D":
        #move Camera Down
        print ("Cameraaa")
    if payLoad == "S":
        #stop camera movement
        print ("Cameraaa")

def processSpeed(payLoad):
    print ("Speeeeed")
    payLoadInt = safeCast(payLoad, int, 0)
    if payLoadInt > 0 and payLoadInt <= 100:
        bot.SERVO.setPWMA(payLoadInt)
        bot.SERVO.setPWMB(payLoadInt)


def safe_cast(val, to_type, default=None):
    try:
        return to_type(val)
    except (ValueError, TypeError):
        return default

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(movement_topic)
    client.subscribe(camera_topic)
    client.subscribe(speed_topic)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    theTime = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    msg.payload = msg.payload.decode("utf-8")
    handleIncomingMessage(msg.topic, str(msg.payload), theTime)
    return


def main():
    bot = AlphaBot()
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect("raspberrypi", 1883, 60)

    client.loop_forever()


if __name__ == '__main__':
    main()
