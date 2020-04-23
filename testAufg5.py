import paho.mqtt.client as mqtt
import time
# "ss20_robotik_t01/+/movement"
# "ss20_robotik_t01/+/camera"
# "ss20_robotik_t01/+/speed"

MQTT_SERVER = "localhost"
client = mqtt.Client("Test1", 1883) #create new instance
client.connect(MQTT_SERVER) #connect to broker

client.publish("ss20_robotik_t01/testscript/movement","F")
time.sleep(3) # 3 seconds forward
client.publish("ss20_robotik_t01/testscript/movement","S") # stop

client.publish("ss20_robotik_t01/testscript/movement","L") # Turn left
time.sleep(2) # lefties for 2 seconds
client.publish("ss20_robotik_t01/testscript/movement","S") # stop again
